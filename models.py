from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from fsrs import Card, State

from scheduling import box_for, make_scheduler, rating_for

db = SQLAlchemy()
scheduler = make_scheduler()


def _as_utc(value):
    """Die Datenbank speichert UTC ohne Zeitzone, FSRS verlangt sie ausdrücklich."""
    return value.replace(tzinfo=timezone.utc) if value else None


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
    """Eine einzelne Multiple-Choice-Frage inkl. FSRS-Status."""
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

    # Box ist seit FSRS nur noch Anzeige und wird aus der Stabilität abgeleitet
    box = db.Column(db.Integer, default=1, nullable=False)
    next_review = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    times_seen = db.Column(db.Integer, default=0, nullable=False)
    times_correct = db.Column(db.Integer, default=0, nullable=False)

    # FSRS-Status
    fsrs_state = db.Column(db.Integer, default=int(State.Learning), nullable=False)
    fsrs_step = db.Column(db.Integer, default=0)
    fsrs_stability = db.Column(db.Float)
    fsrs_difficulty = db.Column(db.Float)
    last_review = db.Column(db.DateTime)

    def register_answer(self, was_correct: bool, difficulty: str = "einfach", source: str = "practice"):
        """Plant die nächste Wiederholung mit FSRS und protokolliert die Antwort.
        difficulty ist nur bei richtiger Antwort relevant: 'schwer', 'einfach', 'sehr_einfach'."""
        now = datetime.now(timezone.utc)
        rating = rating_for(was_correct, difficulty)
        card = Card(
            card_id=self.id,
            state=State(self.fsrs_state),
            step=self.fsrs_step,
            stability=self.fsrs_stability,
            difficulty=self.fsrs_difficulty,
            due=_as_utc(self.next_review),
            last_review=_as_utc(self.last_review),
        )
        card, _ = scheduler.review_card(card, rating, review_datetime=now)

        self.fsrs_state = int(card.state)
        self.fsrs_step = card.step
        self.fsrs_stability = card.stability
        self.fsrs_difficulty = card.difficulty
        self.next_review = card.due.replace(tzinfo=None)
        self.last_review = now.replace(tzinfo=None)
        self.box = box_for(rating, card.stability)
        self.times_seen += 1
        if was_correct:
            self.times_correct += 1

        db.session.add(ReviewLog(
            question_id=self.id,
            rating=int(rating),
            source=source,
            reviewed_at=now.replace(tzinfo=None),
        ))

    def __repr__(self):
        return f"<Question {self.id} (Box {self.box})>"


class ReviewLog(db.Model):
    """Jede beantwortete Frage, als Datenbasis für einen späteren FSRS-Optimizer."""
    __tablename__ = "review_logs"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    rating = db.Column(db.Integer, nullable=False)  # 1 Again, 2 Hard, 3 Good, 4 Easy
    source = db.Column(db.String(20), default="practice", nullable=False)  # "practice" oder "mock_exam"
    reviewed_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


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