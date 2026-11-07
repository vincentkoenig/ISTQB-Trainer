"""FSRS-Einstellungen und Abbildung der App-Bewertungen auf FSRS.

Die Flutter-App nutzt dieselbe Logik in mobile/lib/scheduling.dart. Beide Seiten
schreiben in dieselbe Datenbank, die Werte müssen also identisch bleiben.
Die Standardparameter der Python- und Dart-Pakete unterscheiden sich, deshalb
stehen sie hier ausdrücklich. tests/fsrs_parity.json prüft die Übereinstimmung
(die Schwierigkeit weicht im Dart-Paket minimal ab, siehe mobile/test/scheduling_test.dart).
"""
from datetime import timedelta

from fsrs import Rating, Scheduler

FSRS_PARAMETERS = (
    0.212, 1.2931, 2.3065, 8.2956, 6.4133, 0.8334, 3.0194,
    0.001, 1.8722, 0.1666, 0.796, 1.4835, 0.0614, 0.2629,
    1.6483, 0.6014, 1.8729, 0.5425, 0.0912, 0.0658, 0.1542,
)
DESIRED_RETENTION = 0.9
MAXIMUM_INTERVAL_DAYS = 60  # Prüfungsvorbereitung: nichts soll monatelang liegen bleiben
LEARNING_STEPS = (timedelta(minutes=1), timedelta(minutes=10))
RELEARNING_STEPS = (timedelta(minutes=10),)

# Ab dieser Stabilität (Tage) zählt eine richtig beantwortete Frage zur jeweiligen Box.
BOX_STABILITY_DAYS = ((5, 30), (4, 14), (3, 7))


def make_scheduler(enable_fuzzing: bool = True) -> Scheduler:
    return Scheduler(
        parameters=FSRS_PARAMETERS,
        desired_retention=DESIRED_RETENTION,
        learning_steps=LEARNING_STEPS,
        relearning_steps=RELEARNING_STEPS,
        maximum_interval=MAXIMUM_INTERVAL_DAYS,
        enable_fuzzing=enable_fuzzing,
    )


def rating_for(was_correct: bool, difficulty: str | None) -> Rating:
    if not was_correct:
        return Rating.Again
    if difficulty == "schwer":
        return Rating.Hard
    if difficulty == "sehr_einfach":
        return Rating.Easy
    return Rating.Good


def box_for(rating: Rating, stability: float) -> int:
    """Leitet die Box-Anzeige (1-5) für Dashboard und Review-Ansicht ab."""
    if rating == Rating.Again:
        return 1
    for box, days in BOX_STABILITY_DAYS:
        if stability >= days:
            return box
    return 2
