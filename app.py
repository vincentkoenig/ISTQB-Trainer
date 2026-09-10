import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from models import db, LearningObjective, Question, MockExamAttempt
from datetime import datetime
import random
import json
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///istqb_trainer.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-later")

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

APP_PASSWORD = os.environ.get("APP_PASSWORD")


MOCK_EXAM_DISTRIBUTION = {
    "LO1": 8,
    "LO2": 6,
    "LO3": 4,
    "LO4": 11,
    "LO5": 9,
    "LO6": 2,
}
MOCK_EXAM_DURATION_SECONDS = 60 * 60
MOCK_EXAM_PASS_PERCENT = 65


# ---------- Login ----------

@app.before_request
def require_login():
    # Login-Seite und statische Dateien immer erlauben
    if request.endpoint in ("login", "static"):
        return

    if not session.get("logged_in"):
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        entered_password = request.form.get("password", "")
        if APP_PASSWORD and entered_password == APP_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        error = "Falsches Passwort."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


# ---------- Dashboard ----------

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/dashboard")
def api_dashboard():
    los = LearningObjective.query.order_by(LearningObjective.code).all()

    data = []
    for lo in los:
        questions = [q for chapter in lo.chapters for q in chapter.questions]
        total_questions = len(questions)
        mastered = sum(1 for q in questions if q.box >= 3)
        percent = round((mastered / total_questions) * 100) if total_questions > 0 else 0
        due_count = sum(1 for q in questions if q.next_review <= datetime.utcnow())

        # Verteilung nach Box-Level (1-5)
        box_distribution = {level: 0 for level in range(1, 6)}
        for q in questions:
            box_distribution[q.box] += 1

        not_started = sum(1 for q in questions if q.times_seen == 0)

        data.append({
            "id": lo.id,
            "code": lo.code,
            "title": lo.title,
            "percent": percent,
            "mastered": mastered,
            "total_questions": total_questions,
            "due_count": due_count,
            "box_distribution": box_distribution,
            "not_started": not_started,
        })

    return jsonify(data)


# ---------- Übungsseite ----------

@app.route("/practice/<int:lo_id>")
def practice_page(lo_id):
    return render_template("practice.html", lo_id=lo_id)


@app.route("/api/practice/<int:lo_id>")
def api_practice_questions(lo_id):
    lo = LearningObjective.query.get_or_404(lo_id)

    due_questions = []
    for chapter in lo.chapters:
        for q in chapter.questions:
            if q.next_review <= datetime.utcnow():
                due_questions.append(q)

    data = [
        {
            "id": q.id,
            "prompt": q.prompt,
            "options": {
                "A": q.option_a,
                "B": q.option_b,
                "C": q.option_c,
                "D": q.option_d,
            },
            "box": q.box,
        }
        for q in due_questions
    ]

    return jsonify({"lo_title": lo.title, "questions": data})


@app.route("/api/answer/<int:question_id>", methods=["POST"])
def api_submit_answer(question_id):
    question = Question.query.get_or_404(question_id)
    selected = request.json.get("selected")
    difficulty = request.json.get("difficulty", "einfach")

    was_correct = (selected == question.correct_option)
    question.register_answer(was_correct, difficulty)
    db.session.commit()

    return jsonify({
        "correct": was_correct,
        "correct_option": question.correct_option,
        "explanation": question.explanation,
        "new_box": question.box,
    })


@app.route("/review/<int:lo_id>")
def review_page(lo_id):
    return render_template("review.html", lo_id=lo_id)


@app.route("/api/review/<int:lo_id>")
def api_review_questions(lo_id):
    lo = LearningObjective.query.get_or_404(lo_id)
    filter_mode = request.args.get("filter", "all")  # "all" oder "struggling"

    data = []
    for chapter in sorted(lo.chapters, key=lambda c: c.number):
        chapter_questions = []
        for q in chapter.questions:
            is_struggling = q.box == 1 and q.times_seen > 0
            if filter_mode == "struggling" and not is_struggling:
                continue

            chapter_questions.append({
                "id": q.id,
                "prompt": q.prompt,
                "options": {
                    "A": q.option_a,
                    "B": q.option_b,
                    "C": q.option_c,
                    "D": q.option_d,
                },
                "correct_option": q.correct_option,
                "explanation": q.explanation,
                "box": q.box,
                "times_seen": q.times_seen,
                "times_correct": q.times_correct,
                "is_struggling": is_struggling,
            })

        if chapter_questions:
            data.append({
                "chapter_number": chapter.number,
                "chapter_title": chapter.title,
                "questions": chapter_questions,
            })

    return jsonify({"lo_title": lo.title, "chapters": data})


# ---------- Mock-Exam ----------

@app.route("/mock-exam")
def mock_exam_page():
    return render_template("mock_exam.html")


@app.route("/api/mock-exam/start")
def api_mock_exam_start():
    selected_questions = []
    for lo_code, count in MOCK_EXAM_DISTRIBUTION.items():
        lo = LearningObjective.query.filter_by(code=lo_code).first()
        if not lo:
            continue
        pool = [q for chapter in lo.chapters for q in chapter.questions]
        sample_size = min(count, len(pool))
        selected_questions.extend(random.sample(pool, sample_size))

    random.shuffle(selected_questions)

    data = [
        {
            "id": q.id,
            "prompt": q.prompt,
            "options": {"A": q.option_a, "B": q.option_b, "C": q.option_c, "D": q.option_d},
        }
        for q in selected_questions
    ]

    return jsonify({
        "questions": data,
        "duration_seconds": MOCK_EXAM_DURATION_SECONDS,
        "pass_percent": MOCK_EXAM_PASS_PERCENT,
    })


@app.route("/api/mock-exam/submit", methods=["POST"])
def api_mock_exam_submit():
    payload = request.json
    answers = payload.get("answers", {})

    lo_stats = {}
    total_correct = 0
    total_questions = len(answers)

    question_details = []
    for question_id_str, selected in answers.items():
        question = Question.query.get(int(question_id_str))
        if not question:
            continue

        was_correct = (selected == question.correct_option)
        question.register_answer(was_correct, "einfach")

        question_details.append({
            "prompt": question.prompt,
            "options": {
                "A": question.option_a, "B": question.option_b,
                "C": question.option_c, "D": question.option_d,
            },
            "selected": selected,
            "correct_option": question.correct_option,
            "explanation": question.explanation,
        })

        lo = question.chapter.learning_objective

    lo_results = []
    for code in sorted(lo_stats.keys()):
        stat = lo_stats[code]
        percent = round((stat["correct"] / stat["total"]) * 100, 2) if stat["total"] else 0
        lo_results.append({
            "code": code,
            "title": stat["title"],
            "correct": stat["correct"],
            "total": stat["total"],
            "percent": percent,
        })

    overall_percent = round((total_correct / total_questions) * 100, 2) if total_questions else 0
    passed = overall_percent >= MOCK_EXAM_PASS_PERCENT

    # Versuch in der Datenbank speichern
    attempt = MockExamAttempt(
        total_correct=total_correct,
        total_questions=total_questions,
        overall_percent=overall_percent,
        passed=passed,
        lo_breakdown_json=json.dumps(lo_results),
        question_details_json=json.dumps(question_details),
    )
    db.session.add(attempt)
    db.session.commit()

    return jsonify({
        "total_correct": total_correct,
        "total_questions": total_questions,
        "overall_percent": overall_percent,
        "passed": passed,
        "lo_results": lo_results,
    })


@app.route("/mock-exam/history")
def mock_exam_history_page():
    return render_template("mock_exam_history.html")


@app.route("/api/mock-exam/history")
def api_mock_exam_history():
    attempts = MockExamAttempt.query.order_by(MockExamAttempt.taken_at.desc()).all()

    data = [
        {
            "id": a.id,
            "taken_at": a.taken_at.strftime("%d.%m.%Y %H:%M"),
            "total_correct": a.total_correct,
            "total_questions": a.total_questions,
            "overall_percent": a.overall_percent,
            "passed": a.passed,
            "lo_results": json.loads(a.lo_breakdown_json),
        }
        for a in attempts
    ]

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)