import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

final supabase = Supabase.instance.client;

const Map<int, int> boxIntervals = {1: 0, 2: 3, 3: 7, 4: 14, 5: 30};
const int maxBox = 5;

const primaryColor = Color(0xFF4F46E5);
const accentColor = Color(0xFF10B981);
const errorColor = Color(0xFFEF4444);

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
              ? _buildEmptyState()
              : _buildQuestionView(),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(32.0),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(Icons.check_circle_outline, size: 56, color: accentColor),
            const SizedBox(height: 16),
            const Text(
              'Aktuell sind keine Fragen fällig.',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
            ),
            const SizedBox(height: 6),
            Text(
              'Schau später wieder vorbei!',
              textAlign: TextAlign.center,
              style: TextStyle(color: Colors.grey.shade600),
            ),
          ],
        ),
      ),
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
            style: TextStyle(color: Colors.grey.shade600, fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 10),
          Text(
            question['prompt'] as String,
            style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 20),
          Expanded(
            child: ListView(
              children: options.entries.map((entry) {
                final letter = entry.key;
                final text = entry.value;

                Color backgroundColor = Colors.grey.shade50;
                Color borderColor = Colors.grey.shade200;
                Color textColor = const Color(0xFF1F2937);

                if (_answered) {
                  if (letter == correctOption) {
                    backgroundColor = accentColor.withValues(alpha: 0.12);
                    borderColor = accentColor;
                    textColor = const Color(0xFF065F46);
                  } else if (letter == _selectedLetter) {
                    backgroundColor = errorColor.withValues(alpha: 0.10);
                    borderColor = errorColor;
                    textColor = const Color(0xFF991B1B);
                  }
                }

                return Padding(
                  padding: const EdgeInsets.only(bottom: 10),
                  child: InkWell(
                    borderRadius: BorderRadius.circular(14),
                    onTap: _answered ? null : () => _submitAnswer(letter),
                    child: Container(
                      width: double.infinity,
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(
                        color: backgroundColor,
                        borderRadius: BorderRadius.circular(14),
                        border: Border.all(color: borderColor, width: 1.4),
                      ),
                      child: Text(
                        '$letter) $text',
                        style: TextStyle(color: textColor, fontWeight: FontWeight.w500),
                      ),
                    ),
                  ),
                );
              }).toList(),
            ),
          ),
          if (_answered) ...[
            Container(
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: primaryColor.withValues(alpha: 0.06),
                borderRadius: BorderRadius.circular(14),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Icon(
                        _selectedLetter == correctOption ? Icons.check_circle : Icons.cancel,
                        color: _selectedLetter == correctOption ? accentColor : errorColor,
                        size: 20,
                      ),
                      const SizedBox(width: 8),
                      Text(
                        _selectedLetter == correctOption ? 'Richtig!' : 'Falsch.',
                        style: const TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ],
                  ),
                  if (question['explanation'] != null) ...[
                    const SizedBox(height: 8),
                    Text(question['explanation'] as String, style: const TextStyle(fontSize: 13.5, height: 1.4)),
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