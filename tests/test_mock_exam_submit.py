"""Aufruf aus dem Projektordner: python -m unittest discover tests"""
import json
import os
import unittest

# Muss vor dem App-Import stehen: load_dotenv überschreibt gesetzte Variablen
# nicht, sonst liefe drop_all() gegen die DATABASE_URL aus der .env.
os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["SECRET_KEY"] = "test"

from app import app
from models import Chapter, LearningObjective, MockExamAttempt, Question, db


class MockExamSubmitTest(unittest.TestCase):
    def setUp(self):
        self.context = app.app_context()
        self.context.push()
        self.assertEqual(app.config["SQLALCHEMY_DATABASE_URI"], "sqlite:///:memory:")
        db.drop_all()
        db.create_all()
        self.client = app.test_client()
        with self.client.session_transaction() as session:
            session["logged_in"] = True

    def tearDown(self):
        db.session.remove()
        self.context.pop()

    def add_question(self, lo_code, lo_title):
        lo = LearningObjective.query.filter_by(code=lo_code).first()
        if not lo:
            lo = LearningObjective(code=lo_code, title=lo_title)
            db.session.add(lo)
            db.session.flush()
        chapter = Chapter(lo_id=lo.id, number="1.1", title="Kapitel")
        db.session.add(chapter)
        db.session.flush()
        question = Question(
            chapter_id=chapter.id, prompt="?", option_a="a", option_b="b",
            option_c="c", option_d="d", correct_option="A",
        )
        db.session.add(question)
        db.session.commit()
        return question

    def submit(self, answers):
        response = self.client.post(
            "/api/mock-exam/submit",
            json={"answers": {str(q.id): selected for q, selected in answers}},
        )
        self.assertEqual(response.status_code, 200)
        return response.get_json()

    def test_one_right_one_wrong_in_same_lo_is_50_percent(self):
        right = self.add_question("LO1", "Grundlagen")
        wrong = self.add_question("LO1", "Grundlagen")

        result = self.submit([(right, "A"), (wrong, "B")])

        self.assertEqual(result["total_correct"], 1)
        self.assertEqual(result["total_questions"], 2)
        self.assertEqual(result["overall_percent"], 50)
        self.assertFalse(result["passed"])
        self.assertEqual(result["lo_results"], [{
            "code": "LO1", "title": "Grundlagen",
            "correct": 1, "total": 2, "percent": 50,
        }])

    def test_results_are_split_by_lo_and_sorted_by_code(self):
        wrong = self.add_question("LO2", "Testen im Lebenszyklus")
        right = self.add_question("LO1", "Grundlagen")

        result = self.submit([(wrong, "B"), (right, "A")])

        self.assertEqual(result["overall_percent"], 50)
        self.assertEqual(result["lo_results"], [
            {"code": "LO1", "title": "Grundlagen", "correct": 1, "total": 1, "percent": 100},
            {"code": "LO2", "title": "Testen im Lebenszyklus", "correct": 0, "total": 1, "percent": 0},
        ])

    def test_saved_attempt_matches_the_response(self):
        right = self.add_question("LO1", "Grundlagen")
        wrong = self.add_question("LO1", "Grundlagen")

        result = self.submit([(right, "A"), (wrong, "B")])

        attempt = MockExamAttempt.query.one()
        self.assertEqual(attempt.total_correct, 1)
        self.assertEqual(attempt.total_questions, 2)
        self.assertEqual(attempt.overall_percent, 50)
        self.assertFalse(attempt.passed)
        self.assertEqual(json.loads(attempt.lo_breakdown_json), result["lo_results"])

    def test_passing_score_is_marked_as_passed(self):
        right = self.add_question("LO1", "Grundlagen")

        result = self.submit([(right, "A")])

        self.assertEqual(result["overall_percent"], 100)
        self.assertTrue(result["passed"])


if __name__ == "__main__":
    unittest.main()
