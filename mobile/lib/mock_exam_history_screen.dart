import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

final supabase = Supabase.instance.client;

class MockExamHistoryScreen extends StatefulWidget {
  const MockExamHistoryScreen({super.key});

  @override
  State<MockExamHistoryScreen> createState() => _MockExamHistoryScreenState();
}

class _MockExamHistoryScreenState extends State<MockExamHistoryScreen> {
  List<Map<String, dynamic>> _attempts = [];
  bool _isLoading = true;
  final Set<int> _expandedIndices = {};

  @override
  void initState() {
    super.initState();
    _loadHistory();
  }

  Future<void> _loadHistory() async {
    final response = await supabase
        .from('mock_exam_attempts')
        .select()
        .order('taken_at', ascending: false);

    setState(() {
      _attempts = List<Map<String, dynamic>>.from(response);
      _isLoading = false;
    });
  }

  String _formatDate(String isoDate) {
    final date = DateTime.parse(isoDate).toLocal();
    return '${date.day.toString().padLeft(2, '0')}.${date.month.toString().padLeft(2, '0')}.${date.year} '
        '${date.hour.toString().padLeft(2, '0')}:${date.minute.toString().padLeft(2, '0')}';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Prüfungsverlauf')),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _attempts.isEmpty
              ? const Center(
                  child: Padding(
                    padding: EdgeInsets.all(24.0),
                    child: Text(
                      'Noch keine Prüfungssimulationen absolviert.',
                      textAlign: TextAlign.center,
                    ),
                  ),
                )
              : RefreshIndicator(
                  onRefresh: _loadHistory,
                  child: ListView.builder(
                    padding: const EdgeInsets.all(16),
                    itemCount: _attempts.length,
                    itemBuilder: (context, index) {
                      final attempt = _attempts[index];
                      final passed = attempt['passed'] as bool;
                      final isExpanded = _expandedIndices.contains(index);
                      final loResults = List<Map<String, dynamic>>.from(
                        attempt['lo_breakdown'] ?? [],
                      );

                      return Card(
                        margin: const EdgeInsets.only(bottom: 12),
                        child: InkWell(
                          onTap: () {
                            setState(() {
                              if (isExpanded) {
                                _expandedIndices.remove(index);
                              } else {
                                _expandedIndices.add(index);
                              }
                            });
                          },
                          child: Padding(
                            padding: const EdgeInsets.all(16),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                  children: [
                                    Column(
                                      crossAxisAlignment: CrossAxisAlignment.start,
                                      children: [
                                        Text(
                                          _formatDate(attempt['taken_at'] as String),
                                          style: const TextStyle(color: Colors.grey, fontSize: 13),
                                        ),
                                        const SizedBox(height: 4),
                                        Text(
                                          '${attempt['overall_percent']}%',
                                          style: TextStyle(
                                            fontSize: 28,
                                            fontWeight: FontWeight.bold,
                                            color: passed ? Colors.green : Colors.red,
                                          ),
                                        ),
                                        Text('${attempt['total_correct']} von ${attempt['total_questions']} richtig'),
                                      ],
                                    ),
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                                      decoration: BoxDecoration(
                                        color: passed ? Colors.green.shade100 : Colors.red.shade100,
                                        borderRadius: BorderRadius.circular(14),
                                      ),
                                      child: Text(
                                        passed ? 'Bestanden' : 'Nicht bestanden',
                                        style: TextStyle(
                                          color: passed ? Colors.green.shade900 : Colors.red.shade900,
                                          fontWeight: FontWeight.w600,
                                          fontSize: 12,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                                if (isExpanded) ...[
                                  const Divider(height: 24),
                                  ...loResults.map((lo) {
                                    final percent = (lo['percent'] as num).toDouble();
                                    final isOk = percent >= 65;
                                    return Padding(
                                      padding: const EdgeInsets.symmetric(vertical: 3),
                                      child: Row(
                                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                        children: [
                                          Expanded(
                                            child: Text(
                                              '${lo['code']} – ${lo['title']}',
                                              style: const TextStyle(fontSize: 13),
                                            ),
                                          ),
                                          Text(
                                            '${lo['correct']}/${lo['total']} ($percent%)',
                                            style: TextStyle(
                                              fontSize: 13,
                                              fontWeight: FontWeight.bold,
                                              color: isOk ? Colors.green : Colors.red,
                                            ),
                                          ),
                                        ],
                                      ),
                                    );
                                  }),
                                ],
                              ],
                            ),
                          ),
                        ),
                      );
                    },
                  ),
                ),
    );
  }
}