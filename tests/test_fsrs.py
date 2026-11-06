"""Aufruf aus dem Projektordner: python -m unittest discover tests"""
import json
import os
import unittest
from datetime import datetime, timedelta
from pathlib import Path

os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["SECRET_KEY"] = "test"

from fsrs import Card, Rating, State

from app import app
from models import Chapter, LearningObjective, Question, ReviewLog, db
from scheduling import box_for, make_scheduler, rating_for

PARITY = json.loads((Path(__file__).parent / "fsrs_parity.json").read_text())


def utc(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")) if value else None


class ParityTest(unittest.TestCase):
    """Dieselbe Datei prüft mobile/test/scheduling_test.dart."""

    def test_matches_fixture(self):
        scheduler = make_scheduler(enable_fuzzing=False)
        for scenario in PARITY:
            start = scenario["start"]
            card = Card(
                card_id=1,
                state=State(start["state"]),
                step=start["step"],
                stability=start["stability"],
                difficulty=start["difficulty"],
                due=utc(start["due"]),
                last_review=utc(start["last_review"]),
            )
            for review in scenario["reviews"]:
                rating = rating_for(review["was_correct"], review["difficulty"])
                card, _ = scheduler.review_card(card, rating, review_datetime=utc(review["at"]))
                expected = review["expected"]
                self.assertEqual(int(card.state), expected["state"], scenario["name"])
                self.assertEqual(card.step, expected["step"], scenario["name"])
                self.assertAlmostEqual(card.stability, expected["stability"], places=9)
                self.assertAlmostEqual(card.difficulty, expected["difficulty"], places=9)
                self.assertEqual(card.due, utc(expected["due"]), scenario["name"])
                self.assertEqual(box_for(rating, card.stability), expected["box"])


class BoxTest(unittest.TestCase):
    def test_wrong_answer_is_always_box_1(self):
        self.assertEqual(box_for(Rating.Again, 100), 1)

    def test_thresholds(self):
        for stability, box in ((0.5, 2), (6.9, 2), (7, 3), (14, 4), (30, 5)):
            self.assertEqual(box_for(Rating.Good, stability), box)


class AnswerRouteTest(unittest.TestCase):
    def setUp(self):
        self.context = app.app_context()
        self.context.push()
        db.drop_all()
        db.create_all()
        lo = LearningObjective(code="LO1", title="Test")
        db.session.add(lo)
        db.session.flush()
        chapter = Chapter(lo_id=lo.id, number="1.1", title="Test")
        db.session.add(chapter)
        db.session.flush()
        self.question = Question(
            chapter_id=chapter.id, prompt="?", option_a="a", option_b="b",
            option_c="c", option_d="d", correct_option="A",
        )
        db.session.add(self.question)
        db.session.commit()
        self.client = app.test_client()
        with self.client.session_transaction() as session:
            session["logged_in"] = True

    def tearDown(self):
        db.session.remove()
        self.context.pop()

    def post(self, **body):
        response = self.client.post(f"/api/answer/{self.question.id}", json=body)
        self.assertEqual(response.status_code, 200)
        db.session.refresh(self.question)
        return response.get_json()

    def test_correct_answer_counts_once(self):
        result = self.post(selected="A")
        self.assertTrue(result["correct"])
        self.assertEqual(self.question.times_seen, 0)
        self.assertEqual(ReviewLog.query.count(), 0)

        self.post(selected="A", difficulty="einfach")
        self.assertEqual(self.question.times_seen, 1)
        self.assertEqual(self.question.times_correct, 1)
        self.assertEqual(ReviewLog.query.one().rating, 3)
        self.assertEqual(self.question.box, 2)
        self.assertIsNotNone(self.question.fsrs_stability)

    def test_wrong_answer_is_saved_immediately(self):
        result = self.post(selected="B")
        self.assertFalse(result["correct"])
        self.assertEqual(self.question.times_seen, 1)
        self.assertEqual(self.question.box, 1)
        self.assertEqual(ReviewLog.query.one().rating, 1)
        self.assertLess(self.question.next_review, datetime.utcnow() + timedelta(minutes=2))

    def test_interval_grows_beyond_one_day(self):
        self.question.fsrs_state = int(State.Review)
        self.question.fsrs_step = None
        self.question.fsrs_stability = 7.0
        self.question.fsrs_difficulty = 5.0
        self.question.last_review = datetime.utcnow() - timedelta(days=7)
        self.question.times_seen = 3
        db.session.commit()

        self.post(selected="A", difficulty="einfach")
        self.assertGreater(self.question.next_review, datetime.utcnow() + timedelta(days=7))

    def test_interval_is_capped(self):
        self.question.fsrs_state = int(State.Review)
        self.question.fsrs_step = None
        self.question.fsrs_stability = 300.0
        self.question.fsrs_difficulty = 3.0
        self.question.last_review = datetime.utcnow() - timedelta(days=60)
        db.session.commit()

        self.post(selected="A", difficulty="sehr_einfach")
        self.assertLessEqual(self.question.next_review, datetime.utcnow() + timedelta(days=61))

    def test_mock_exam_logs_its_source(self):
        response = self.client.post(
            "/api/mock-exam/submit", json={"answers": {str(self.question.id): "A"}}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ReviewLog.query.one().source, "mock_exam")


if __name__ == "__main__":
    unittest.main()
