from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

# Intervalle pro Leitner-Box (in Tagen), bis eine Frage wieder fällig ist
BOX_INTERVALS = {
    1: 0,   # sofort/nächste Session wieder fällig
    2: 3,
    3: 7,
    4: 14,
    5: 30,
}
MAX_BOX = 5


class LearningObjective(db.Model):
    """Repräsentiert LO1-LO6 aus dem ISTQB-Lehrplan."""
    __tablename__ = "learning_objectives"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)   # z.B. "LO1"
    title = db.Column(db.String(200), nullable=False)              # z.B. "Grundlagen des Testens"

    chapters = db.relationship("Chapter", backref="learning_objective", lazy=True)

    def __repr__(self):
        return f"<LO {self.code}: {self.title}>"


class Chapter(db.Model):
    """Ein einzelnes Kapitel/eine Präsentation, z.B. '2.3 Grundsätze des Testens'."""
    __tablename__ = "chapters"

    id = db.Column(db.Integer, primary_key=True)
    lo_id = db.Column(db.Integer, db.ForeignKey("learning_objectives.id"), nullable=False)
    number = db.Column(db.String(10), nullable=False)   # z.B. "2.3"
    title = db.Column(db.String(200), nullable=False)   # z.B. "Grundsätze des Testens"
    content = db.Column(db.Text)                        # aufbereiteter Lerninhalt (Markdown)

    questions = db.relationship("Question", backref="chapter", lazy=True)

    def __repr__(self):
        return f"<Chapter {self.number}: {self.title}>"


class Question(db.Model):
    """Eine einzelne Multiple-Choice-Frage inkl. Leitner-Status."""
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapters.id"), nullable=False)

    prompt = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.Text, nullable=False)
    option_b = db.Column(db.Text, nullable=False)
    option_c = db.Column(db.Text, nullable=False)
    option_d = db.Column(db.Text, nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)  # "A" / "B" / "C" / "D"
    explanation = db.Column(db.Text)
    source = db.Column(db.String(50), default="practice", nullable=False)  # "practice" oder "official_mock"

    # Leitner-System-Felder
    box = db.Column(db.Integer, default=1, nullable=False)
    next_review = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    times_seen = db.Column(db.Integer, default=0, nullable=False)
    times_correct = db.Column(db.Integer, default=0, nullable=False)

    def register_answer(self, was_correct: bool, difficulty: str = "einfach"):
        """Aktualisiert Box-Level und nächsten Wiederholungstermin nach einer Antwort.
        difficulty ist nur bei richtiger Antwort relevant: 'schwer', 'einfach', 'sehr_einfach'."""
        self.times_seen += 1
        if was_correct:
            self.times_correct += 1
            self.box = min(self.box + 1, MAX_BOX)

            if difficulty == "schwer":
                minutes = 5
            elif difficulty == "sehr_einfach":
                minutes = 60 * 24  # 1 Tag
            else:  # "einfach" oder Fallback
                minutes = 10

            self.next_review = datetime.utcnow() + timedelta(minutes=minutes)
        else:
            self.box = 1
            self.next_review = datetime.utcnow() + timedelta(minutes=1)

    def __repr__(self):
        return f"<Question {self.id} (Box {self.box})>"


class MockExamAttempt(db.Model):
    """Ein abgeschlossener Prüfungssimulations-Versuch."""
    __tablename__ = "mock_exam_attempts"

    id = db.Column(db.Integer, primary_key=True)
    taken_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    total_correct = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    overall_percent = db.Column(db.Float, nullable=False)
    passed = db.Column(db.Boolean, nullable=False)
    lo_breakdown_json = db.Column(db.Text, nullable=False)  # JSON-String der lo_results
    question_details_json = db.Column(db.Text)  # JSON: Liste von {prompt, options, selected, correct_option, explanation}

    def __repr__(self):
        return f"<MockExamAttempt {self.taken_at} - {self.overall_percent}%>"