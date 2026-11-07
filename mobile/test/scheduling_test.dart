import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:mobile/scheduling.dart';

void main() {
  test('rechnet genauso wie das Flask-Backend', () {
    // Dieselbe Datei prüft tests/test_fsrs.py
    final scenarios = jsonDecode(File('../tests/fsrs_parity.json').readAsStringSync()) as List;
    final scheduler = makeScheduler(enableFuzzing: false);

    for (final scenario in scenarios) {
      final start = scenario['start'] as Map<String, dynamic>;
      final question = <String, dynamic>{
        'id': 1,
        'fsrs_state': start['state'],
        'fsrs_step': start['step'],
        'fsrs_stability': start['stability'],
        'fsrs_difficulty': start['difficulty'],
        'next_review': start['due'],
        'last_review': start['last_review'],
        'times_seen': 0,
        'times_correct': 0,
      };

      for (final review in scenario['reviews']) {
        final expected = review['expected'] as Map<String, dynamic>;
        final update = reviewQuestion(
          question,
          wasCorrect: review['was_correct'] as bool,
          difficulty: review['difficulty'] as String?,
          now: parseUtc(review['at'] as String),
          scheduler: scheduler,
        );
        final name = scenario['name'];

        expect(update['fsrs_state'], expected['state'], reason: '$name');
        expect(update['fsrs_step'], expected['step'], reason: '$name');
        // fsrs 2.0.1 (Dart) begrenzt das Rückkehrziel der Schwierigkeit auf 1, fsrs 6.3.2 (Python)
        // nicht. Das macht rund 0,006 pro Antwort aus, deshalb hier kleine Toleranzen.
        final stability = expected['stability'] as double;
        expect(update['fsrs_stability'], closeTo(stability, stability * 0.02), reason: '$name');
        expect(update['fsrs_difficulty'], closeTo(expected['difficulty'] as double, 0.05), reason: '$name');
        final dueGap = parseUtc(update['next_review'] as String).difference(parseUtc(expected['due'] as String));
        expect(dueGap.inDays.abs(), lessThanOrEqualTo(1), reason: '$name');
        expect(update['box'], expected['box'], reason: '$name');

        question.addAll(update);
      }
    }
  });

  test('liest Zeiten ohne Zeitzone als UTC', () {
    expect(parseUtc('2026-11-06T10:00:00.5'), DateTime.utc(2026, 11, 6, 10, 0, 0, 500));
    expect(parseUtc('2026-11-06T10:00:00+01:00'), DateTime.utc(2026, 11, 6, 9));
  });

  test('zählt falsche Antworten nicht als richtig', () {
    final question = <String, dynamic>{
      'id': 1,
      'fsrs_state': 1,
      'fsrs_step': 0,
      'fsrs_stability': null,
      'fsrs_difficulty': null,
      'next_review': '2026-11-06T10:00:00',
      'last_review': null,
      'times_seen': 2,
      'times_correct': 1,
    };

    final update = reviewQuestion(question, wasCorrect: false, now: DateTime.utc(2026, 11, 6, 10));

    expect(update['times_seen'], 3);
    expect(update['times_correct'], 1);
    expect(update['box'], 1);
  });
}
