import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

final supabase = Supabase.instance.client;

class ReviewScreen extends StatefulWidget {
  final int loId;
  final String loTitle;

  const ReviewScreen({super.key, required this.loId, required this.loTitle});

  @override
  State<ReviewScreen> createState() => _ReviewScreenState();
}

class _ReviewScreenState extends State<ReviewScreen> {
  List<Map<String, dynamic>> _allQuestions = [];
  bool _isLoading = true;
  String _filter = 'all'; // "all" oder "struggling"
  final Set<int> _expandedIds = {};

  @override
  void initState() {
    super.initState();
    _loadQuestions();
  }

  Future<void> _loadQuestions() async {
    final response = await supabase
        .from('questions')
        .select('*, chapters!inner(lo_id, number, title)')
        .eq('chapters.lo_id', widget.loId);

    setState(() {
      _allQuestions = List<Map<String, dynamic>>.from(response);
      _isLoading = false;
    });
  }

  List<Map<String, dynamic>> get _filteredQuestions {
    if (_filter == 'all') return _allQuestions;
    return _allQuestions.where((q) {
      final box = q['box'] as int;
      final timesSeen = q['times_seen'] as int;
      return box == 1 && timesSeen > 0;
    }).toList();
  }

  Map<String, List<Map<String, dynamic>>> get _groupedByChapter {
    final grouped = <String, List<Map<String, dynamic>>>{};
    for (final q in _filteredQuestions) {
      final chapter = q['chapters'];
      final key = '${chapter['number']} – ${chapter['title']}';
      grouped.putIfAbsent(key, () => []).add(q);
    }
    return grouped;
  }

  @override
  Widget build(BuildContext context) {
    final grouped = _groupedByChapter;

    return Scaffold(
      appBar: AppBar(title: Text('Fragen ansehen: ${widget.loTitle}')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12.0),
            child: Row(
              children: [
                Expanded(
                  child: ChoiceChip(
                    label: const Text('Alle Fragen'),
                    selected: _filter == 'all',
                    onSelected: (_) => setState(() => _filter = 'all'),
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: ChoiceChip(
                    label: const Text('Noch nicht gemeistert'),
                    selected: _filter == 'struggling',
                    onSelected: (_) => setState(() => _filter = 'struggling'),
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            child: _isLoading
                ? const Center(child: CircularProgressIndicator())
                : grouped.isEmpty
                    ? const Center(child: Text('Keine Fragen in dieser Ansicht.'))
                    : ListView(
                        padding: const EdgeInsets.symmetric(horizontal: 12),
                        children: grouped.entries.map((entry) {
                          return Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Padding(
                                padding: const EdgeInsets.symmetric(vertical: 10),
                                child: Text(
                                  entry.key,
                                  style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 15),
                                ),
                              ),
                              ...entry.value.map((q) => _buildQuestionCard(q)),
                            ],
                          );
                        }).toList(),
                      ),
          ),
        ],
      ),
    );
  }

  Widget _buildQuestionCard(Map<String, dynamic> q) {
    final id = q['id'] as int;
    final isExpanded = _expandedIds.contains(id);
    final box = q['box'] as int;
    final timesSeen = q['times_seen'] as int;
    final timesCorrect = q['times_correct'] as int;
    final isStruggling = box == 1 && timesSeen > 0;

    final options = {
      'A': q['option_a'] as String,
      'B': q['option_b'] as String,
      'C': q['option_c'] as String,
      'D': q['option_d'] as String,
    };
    final correctOption = q['correct_option'] as String;

    return Card(
      margin: const EdgeInsets.only(bottom: 8),
      child: InkWell(
        onTap: () {
          setState(() {
            if (isExpanded) {
              _expandedIds.remove(id);
            } else {
              _expandedIds.add(id);
            }
          });
        },
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: Text(q['prompt'] as String, style: const TextStyle(fontSize: 14)),
                  ),
                  if (timesSeen > 0)
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                      decoration: BoxDecoration(
                        color: isStruggling ? Colors.red.shade100 : Colors.green.shade100,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(
                        isStruggling ? 'Noch nicht gemeistert' : 'Box $box',
                        style: TextStyle(
                          fontSize: 11,
                          color: isStruggling ? Colors.red.shade900 : Colors.green.shade900,
                        ),
                      ),
                    ),
                ],
              ),
              if (isExpanded) ...[
                const Divider(height: 20),
                ...options.entries.map((entry) {
                  final isCorrect = entry.key == correctOption;
                  return Container(
                    margin: const EdgeInsets.only(bottom: 6),
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: isCorrect ? Colors.green.shade50 : Colors.grey.shade100,
                      borderRadius: BorderRadius.circular(6),
                      border: isCorrect ? Border.all(color: Colors.green, width: 1.5) : null,
                    ),
                    child: Text(
                      '${entry.key}) ${entry.value}',
                      style: TextStyle(
                        fontSize: 13,
                        fontWeight: isCorrect ? FontWeight.bold : FontWeight.normal,
                      ),
                    ),
                  );
                }),
                if (q['explanation'] != null) ...[
                  const SizedBox(height: 6),
                  Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: Colors.blue.shade50,
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(q['explanation'] as String, style: const TextStyle(fontSize: 13)),
                  ),
                ],
                const SizedBox(height: 6),
                Text(
                  'Gesehen: $timesSeen× · Richtig: $timesCorrect×',
                  style: const TextStyle(fontSize: 12, color: Colors.grey),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}