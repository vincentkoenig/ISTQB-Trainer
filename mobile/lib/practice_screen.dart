import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

final supabase = Supabase.instance.client;

// Leitner-Intervalle in Tagen, analog zur Python-Version
const Map<int, int> boxIntervals = {1: 0, 2: 3, 3: 7, 4: 14, 5: 30};
const int maxBox = 5;

class PracticeScreen extends StatefulWidget {
  final int loId;
  final String loTitle;

  const PracticeScreen({super.key, required this.loId, required this.loTitle});

  @override
  State<PracticeScreen> createState() => _PracticeScreenState();
}

class _PracticeScreenState extends State<PracticeScreen> {
  List<Map<String, dynamic>> _questions = [];
  int _currentIndex = 0;
  bool _isLoading = true;
  bool _answered = false;
  String? _selectedLetter;

  @override
  void initState() {
    super.initState();
    _loadQuestions();
  }

  Future<void> _loadQuestions() async {
    final nowIso = DateTime.now().toUtc().toIso8601String();

    final response = await supabase
        .from('questions')
        .select('*, chapters!inner(lo_id)')
        .eq('chapters.lo_id', widget.loId)
        .lte('next_review', nowIso);

    setState(() {
      _questions = List<Map<String, dynamic>>.from(response);
      _isLoading = false;
    });
  }

  Future<void> _submitAnswer(String letter) async {
    if (_answered) return;

    final question = _questions[_currentIndex];
    final correctOption = question['correct_option'] as String;
    final wasCorrect = letter == correctOption;

    int box = question['box'] as int;
    int timesSeen = question['times_seen'] as int;
    int timesCorrect = question['times_correct'] as int;

    timesSeen += 1;
    if (wasCorrect) {
      timesCorrect += 1;
      box = (box + 1) > maxBox ? maxBox : box + 1;
    } else {
      box = 1;
    }

    final days = boxIntervals[box]!;
    final nextReview = DateTime.now().toUtc().add(Duration(days: days));

    try {
      await supabase.from('questions').update({
        'box': box,
        'times_seen': timesSeen,
        'times_correct': timesCorrect,
        'next_review': nextReview.toIso8601String(),
      }).eq('id', question['id']);

      setState(() {
        _selectedLetter = letter;
        _answered = true;
        _questions[_currentIndex]['box'] = box;
      });
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Fehler beim Speichern: $e')),
        );
      }
    }
  }

  void _nextQuestion() {
    if (_currentIndex + 1 < _questions.length) {
      setState(() {
        _currentIndex++;
        _answered = false;
        _selectedLetter = null;
      });
    } else {
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Üben: ${widget.loTitle}')),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _questions.isEmpty
              ? const Center(child: Text('Aktuell sind keine Fragen fällig. 🎉'))
              : _buildQuestionView(),
    );
  }

  Widget _buildQuestionView() {
    final question = _questions[_currentIndex];
    final options = {
      'A': question['option_a'] as String,
      'B': question['option_b'] as String,
      'C': question['option_c'] as String,
      'D': question['option_d'] as String,
    };
    final correctOption = question['correct_option'] as String;

    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Frage ${_currentIndex + 1} von ${_questions.length}',
            style: const TextStyle(color: Colors.grey),
          ),
          const SizedBox(height: 8),
          Text(
            question['prompt'] as String,
            style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w500),
          ),
          const SizedBox(height: 20),
          Expanded(
            child: ListView(
              children: options.entries.map((entry) {
                final letter = entry.key;
                final text = entry.value;

                Color? backgroundColor;
                if (_answered) {
                  if (letter == correctOption) {
                    backgroundColor = Colors.green.shade100;
                  } else if (letter == _selectedLetter) {
                    backgroundColor = Colors.red.shade100;
                  }
                }

                return Padding(
                  padding: const EdgeInsets.only(bottom: 8),
                  child: OutlinedButton(
                    style: OutlinedButton.styleFrom(
                      backgroundColor: backgroundColor,
                      alignment: Alignment.centerLeft,
                      padding: const EdgeInsets.all(14),
                    ),
                    onPressed: _answered ? null : () => _submitAnswer(letter),
                    child: Text('$letter) $text'),
                  ),
                );
              }).toList(),
            ),
          ),
          if (_answered) ...[
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.blue.shade50,
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    _selectedLetter == correctOption ? '✅ Richtig!' : '❌ Falsch.',
                    style: const TextStyle(fontWeight: FontWeight.bold),
                  ),
                  if (question['explanation'] != null) ...[
                    const SizedBox(height: 6),
                    Text(question['explanation'] as String),
                  ],
                ],
              ),
            ),
            const SizedBox(height: 12),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: _nextQuestion,
                child: Text(
                  _currentIndex + 1 < _questions.length ? 'Nächste Frage' : 'Fertig',
                ),
              ),
            ),
          ],
        ],
      ),
    );
  }
}