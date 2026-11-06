// FSRS-Einstellungen und Speichern von Antworten.
//
// Das Flask-Backend nutzt dieselbe Logik in scheduling.py. Beide Seiten schreiben
// in dieselbe Datenbank, die Werte müssen also identisch bleiben. Die
// Standardparameter der Python- und Dart-Pakete unterscheiden sich, deshalb stehen
// sie hier ausdrücklich. tests/fsrs_parity.json prüft die Übereinstimmung (die
// Schwierigkeit weicht im Dart-Paket minimal ab, siehe test/scheduling_test.dart).
import 'package:fsrs/fsrs.dart' as fsrs;
import 'package:supabase_flutter/supabase_flutter.dart';

const fsrsParameters = [
  0.212, 1.2931, 2.3065, 8.2956, 6.4133, 0.8334, 3.0194,
  0.001, 1.8722, 0.1666, 0.796, 1.4835, 0.0614, 0.2629,
  1.6483, 0.6014, 1.8729, 0.5425, 0.0912, 0.0658, 0.1542,
];
const desiredRetention = 0.9;
const maximumIntervalDays = 60; // Prüfungsvorbereitung: nichts soll monatelang liegen bleiben
const learningSteps = [Duration(minutes: 1), Duration(minutes: 10)];
const relearningSteps = [Duration(minutes: 10)];

fsrs.Scheduler makeScheduler({bool enableFuzzing = true}) => fsrs.Scheduler(
      parameters: fsrsParameters,
      desiredRetention: desiredRetention,
      learningSteps: learningSteps,
      relearningSteps: relearningSteps,
      maximumInterval: maximumIntervalDays,
      enableFuzzing: enableFuzzing,
    );

final _scheduler = makeScheduler();

/// Die Datenbank liefert UTC-Zeiten ohne Zeitzone, DateTime.parse läse sie sonst als Ortszeit.
DateTime parseUtc(String value) {
  final hasZone = RegExp(r'(Z|[+-]\d{2}(:?\d{2})?)$').hasMatch(value);
  return DateTime.parse(hasZone ? value : '${value}Z').toUtc();
}

fsrs.Rating ratingFor(bool wasCorrect, String? difficulty) {
  if (!wasCorrect) return fsrs.Rating.again;
  if (difficulty == 'schwer') return fsrs.Rating.hard;
  if (difficulty == 'sehr_einfach') return fsrs.Rating.easy;
  return fsrs.Rating.good;
}

/// Leitet die Box-Anzeige (1-5) für Dashboard und Review-Ansicht ab.
int boxFor(fsrs.Rating rating, double stability) {
  if (rating == fsrs.Rating.again) return 1;
  if (stability >= 30) return 5;
  if (stability >= 14) return 4;
  if (stability >= 7) return 3;
  return 2;
}

/// Berechnet die neuen Spaltenwerte einer Frage nach einer Antwort.
Map<String, dynamic> reviewQuestion(
  Map<String, dynamic> question, {
  required bool wasCorrect,
  String? difficulty,
  required DateTime now,
  fsrs.Scheduler? scheduler,
}) {
  final rating = ratingFor(wasCorrect, difficulty);
  final lastReview = question['last_review'] as String?;

  final card = fsrs.Card(
    cardId: question['id'] as int,
    state: fsrs.State.fromValue(question['fsrs_state'] as int),
    step: question['fsrs_step'] as int?,
    stability: (question['fsrs_stability'] as num?)?.toDouble(),
    difficulty: (question['fsrs_difficulty'] as num?)?.toDouble(),
    due: parseUtc(question['next_review'] as String),
    lastReview: lastReview == null ? null : parseUtc(lastReview),
  );

  final reviewed = (scheduler ?? _scheduler)
      .reviewCard(card, rating, reviewDateTime: now)
      .card;

  return {
    'fsrs_state': reviewed.state.value,
    'fsrs_step': reviewed.step,
    'fsrs_stability': reviewed.stability,
    'fsrs_difficulty': reviewed.difficulty,
    'next_review': reviewed.due.toIso8601String(),
    'last_review': now.toIso8601String(),
    'box': boxFor(rating, reviewed.stability!),
    'times_seen': (question['times_seen'] as int) + 1,
    'times_correct': (question['times_correct'] as int) + (wasCorrect ? 1 : 0),
  };
}

/// Plant die nächste Wiederholung, speichert sie und protokolliert die Antwort.
/// Gibt die neuen Spaltenwerte zurück.
Future<Map<String, dynamic>> saveAnswer(
  Map<String, dynamic> question, {
  required bool wasCorrect,
  String? difficulty,
  required String source,
}) async {
  final client = Supabase.instance.client;
  final now = DateTime.now().toUtc();
  final update = reviewQuestion(
    question,
    wasCorrect: wasCorrect,
    difficulty: difficulty,
    now: now,
  );

  await client.from('questions').update(update).eq('id', question['id']);
  await client.from('review_logs').insert({
    'question_id': question['id'],
    'rating': ratingFor(wasCorrect, difficulty).value,
    'source': source,
    'reviewed_at': now.toIso8601String(),
  });

  return update;
}
