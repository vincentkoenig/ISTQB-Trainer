import 'dart:async';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

final supabase = Supabase.instance.client;

const Map<String, int> mockExamDistribution = {
  'LO1': 8,
  'LO2': 6,
  'LO3': 4,
  'LO4': 11,
  'LO5': 9,
  'LO6': 2,
};
const int mockExamDurationSeconds = 60 * 60;
const int mockExamPassPercent = 65;

class MockExamScreen extends StatefulWidget {
  const MockExamScreen({super.key});

  @override
  State<MockExamScreen> createState() => _MockExamScreenState();
}

class _MockExamScreenState extends State<MockExamScreen> {
  List<Map<String, dynamic>> _questions = [];
  Map<int, String> _answers = {};
  int _currentIndex = 0;
  bool _isLoading = true;
  bool _isSubmitted = false;
  Map<String, dynamic>? _result;

  int _remainingSeconds = mockExamDurationSeconds;
  Timer? _timer;

  @override
  void initState() {
    super.initState();
    _startExam();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  Future<void> _startExam() async {
    final los = await supabase.from('learning_objectives').select();
    final losList = List<Map<String, dynamic>>.from(los);

    final selectedQuestions = <Map<String, dynamic>>[];
    final random = Random();

    for (final entry in mockExamDistribution.entries) {
      final loCode = entry.key;
      final count = entry.value;

      final lo = losList.firstWhere((l) => l['code'] == loCode, orElse: () => {});
      if (lo.isEmpty) continue;

      final questions = await supabase
          .from('questions')
          .select('*, chapters!inner(lo_id)')
          .eq('chapters.lo_id', lo['id']);

      final pool = List<Map<String, dynamic>>.from(questions);
      pool.shuffle(random);
      final sampleSize = min(count, pool.length);
      selectedQuestions.addAll(pool.take(sampleSize));
    }

    selectedQuestions.shuffle(random);

    setState(() {
      _questions = selectedQuestions;
      _isLoading = false;
    });

    _startTimer();
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      setState(() {
        _remainingSeconds--;
      });
      if (_remainingSeconds <= 0) {
        timer.cancel();
        _submitExam();
      }
    });
  }

  String get _timerDisplay {
    final m = _remainingSeconds ~/ 60;
    final s = _remainingSeconds % 60;
    return '$m:${s.toString().padLeft(2, '0')}';
  }

  void _selectAnswer(String letter) {
    setState(() {
      _answers[_questions[_currentIndex]['id'] as int] = letter;
    });
  }

  void _goNext() {
    if (_currentIndex + 1 < _questions.length) {
      setState(() => _currentIndex++);
    }
  }

  void _goPrev() {
    if (_currentIndex > 0) {
      setState(() => _currentIndex--);
    }
  }

  void _goToQuestion(int index) {
    setState(() => _currentIndex = index);
  }

  Future<void> _confirmSubmit() async {
    final unanswered = _questions.length - _answers.length;
    if (unanswered > 0) {
      final proceed = await showDialog<bool>(
        context: context,
        builder: (context) => AlertDialog(
          title: const Text('Prüfung abgeben?'),
          content: Text('Du hast noch $unanswered Frage(n) nicht beantwortet. Trotzdem abgeben?'),
          actions: [
            TextButton(onPressed: () => Navigator.of(context).pop(false), child: const Text('Abbrechen')),
            TextButton(onPressed: () => Navigator.of(context).pop(true), child: const Text('Abgeben')),
          ],
        ),
      );
      if (proceed != true) return;
    }
    _submitExam();
  }

  Future<void> _submitExam() async {
    _timer?.cancel();

    final loStats = <String, Map<String, dynamic>>{};
    int totalCorrect = 0;

    for (final q in _questions) {
      final qId = q['id'] as int;
      final selected = _answers[qId];
      if (selected == null) continue;

      final correctOption = q['correct_option'] as String;
      final wasCorrect = selected == correctOption;

      // Leitner-Box aktualisieren, analog zum Übungsmodus
      int box = q['box'] as int;
      int timesSeen = (q['times_seen'] as int) + 1;
      int timesCorrect = q['times_correct'] as int;

      const boxIntervals = {1: 0, 2: 3, 3: 7, 4: 14, 5: 30};
      if (wasCorrect) {
        timesCorrect += 1;
        box = box + 1 > 5 ? 5 : box + 1;
        totalCorrect++;
      } else {
        box = 1;
      }
      final nextReview = DateTime.now().toUtc().add(Duration(days: boxIntervals[box]!));

      await supabase.from('questions').update({
        'box': box,
        'times_seen': timesSeen,
        'times_correct': timesCorrect,
        'next_review': nextReview.toIso8601String(),
      }).eq('id', qId);

      final loId = q['chapters']['lo_id'];
      // LO-Code und Titel aus der bereits geladenen Frage holen wir separat, da hier nur lo_id vorliegt
      loStats.putIfAbsent(loId.toString(), () => {'correct': 0, 'total': 0});
      loStats[loId.toString()]!['total'] = (loStats[loId.toString()]!['total'] as int) + 1;
      if (wasCorrect) {
        loStats[loId.toString()]!['correct'] = (loStats[loId.toString()]!['correct'] as int) + 1;
      }
    }

    // LO-Titel/Code nachladen für die Ergebnisanzeige
    final los = await supabase.from('learning_objectives').select();
    final losList = List<Map<String, dynamic>>.from(los);

    final loResults = <Map<String, dynamic>>[];
    loStats.forEach((loIdStr, stat) {
      final lo = losList.firstWhere((l) => l['id'].toString() == loIdStr, orElse: () => {});
      final total = stat['total'] as int;
      final correct = stat['correct'] as int;
      final percent = total > 0 ? (correct / total * 100) : 0.0;
      loResults.add({
        'code': lo['code'] ?? '?',
        'title': lo['title'] ?? 'Unbekannt',
        'correct': correct,
        'total': total,
        'percent': double.parse(percent.toStringAsFixed(2)),
      });
    });
    loResults.sort((a, b) => (a['code'] as String).compareTo(b['code'] as String));

    final totalAnswered = _answers.length;
    final overallPercent = totalAnswered > 0
        ? double.parse((totalCorrect / totalAnswered * 100).toStringAsFixed(2))
        : 0.0;
    final passed = overallPercent >= mockExamPassPercent;

    // Versuch in der Datenbank speichern
    await supabase.from('mock_exam_attempts').insert({
      'total_correct': totalCorrect,
      'total_questions': totalAnswered,
      'overall_percent': overallPercent,
      'passed': passed,
      'lo_breakdown': loResults,
    });

    setState(() {
      _isSubmitted = true;
      _result = {
        'total_correct': totalCorrect,
        'total_questions': totalAnswered,
        'overall_percent': overallPercent,
        'passed': passed,
        'lo_results': loResults,
      };
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return Scaffold(
        appBar: AppBar(title: const Text('Prüfungssimulation')),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    if (_isSubmitted) {
      return _buildResultView();
    }

    return _buildExamView();
  }

  Widget _buildExamView() {
    final question = _questions[_currentIndex];
    final options = {
      'A': question['option_a'] as String,
      'B': question['option_b'] as String,
      'C': question['option_c'] as String,
      'D': question['option_d'] as String,
    };
    final selected = _answers[question['id']];

    return Scaffold(
      appBar: AppBar(
        title: Text('Frage ${_currentIndex + 1} von ${_questions.length}'),
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 16),
            child: Center(
              child: Text(
                _timerDisplay,
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: _remainingSeconds < 300 ? Colors.red : Colors.black,
                ),
              ),
            ),
          ),
        ],
      ),
      body: Column(
        children: [
          SizedBox(
            height: 50,
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 8),
              itemCount: _questions.length,
              itemBuilder: (context, index) {
                final isAnswered = _answers.containsKey(_questions[index]['id']);
                final isCurrent = index == _currentIndex;
                return Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 3, vertical: 6),
                  child: InkWell(
                    onTap: () => _goToQuestion(index),
                    child: Container(
                      width: 36,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: isAnswered ? Colors.green.shade100 : Colors.grey.shade100,
                        border: Border.all(
                          color: isCurrent ? Colors.blueGrey.shade800 : Colors.grey.shade400,
                          width: isCurrent ? 2 : 1,
                        ),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text('${index + 1}', style: const TextStyle(fontSize: 12)),
                    ),
                  ),
                );
              },
            ),
          ),
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    question['prompt'] as String,
                    style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w500),
                  ),
                  const SizedBox(height: 20),
                  ...options.entries.map((entry) {
                    final isSelected = selected == entry.key;
                    return Padding(
                      padding: const EdgeInsets.only(bottom: 8),
                      child: OutlinedButton(
                        style: OutlinedButton.styleFrom(
                          backgroundColor: isSelected ? Colors.blue.shade50 : null,
                          side: BorderSide(color: isSelected ? Colors.blueGrey.shade800 : Colors.grey.shade400, width: isSelected ? 2 : 1),
                          alignment: Alignment.centerLeft,
                          padding: const EdgeInsets.all(14),
                        ),
                        onPressed: () => _selectAnswer(entry.key),
                        child: Text('${entry.key}) ${entry.value}'),
                      ),
                    );
                  }),
                ],
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: _currentIndex > 0 ? _goPrev : null,
                    child: const Text('Zurück'),
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(backgroundColor: Colors.red.shade700),
                    onPressed: _confirmSubmit,
                    child: const Text('Abgeben', style: TextStyle(color: Colors.white)),
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: OutlinedButton(
                    onPressed: _currentIndex < _questions.length - 1 ? _goNext : null,
                    child: const Text('Weiter'),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildResultView() {
    final r = _result!;
    final passed = r['passed'] as bool;
    final loResults = List<Map<String, dynamic>>.from(r['lo_results']);

    return Scaffold(
      appBar: AppBar(title: const Text('Prüfungsergebnis')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                children: [
                  Text(
                    '${r['overall_percent']}%',
                    style: TextStyle(
                      fontSize: 48,
                      fontWeight: FontWeight.bold,
                      color: passed ? const Color(0xFF10B981) : const Color(0xFFEF4444),
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text('${r['total_correct']} von ${r['total_questions']} Fragen richtig'),
                  const SizedBox(height: 12),
                  Text(
                    passed ? '✅ Bestanden!' : '❌ Nicht bestanden',
                    style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                  ),
                  const Text('Bestehensgrenze: 65%', style: TextStyle(color: Colors.grey)),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),
          ...loResults.map((lo) {
            final percent = lo['percent'] as double;
            final isOk = percent >= 65;
            return Card(
              margin: const EdgeInsets.only(bottom: 8),
              child: ListTile(
                title: Text('${lo['code']} – ${lo['title']}'),
                subtitle: Text('${lo['correct']} / ${lo['total']}'),
                trailing: Text(
                  '$percent%',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: isOk ? const Color(0xFF10B981) : const Color(0xFFEF4444),
                  ),
                ),
              ),
            );
          }),
          const SizedBox(height: 16),
          ElevatedButton(
            onPressed: () => Navigator.of(context).popUntil((route) => route.isFirst),
            child: const Text('Zurück zum Dashboard'),
          ),
        ],
      ),
    );
  }
}