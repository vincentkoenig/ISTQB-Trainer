from flask import Flask, render_template, jsonify, request
from models import db, LearningObjective, Question
from datetime import datetime


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///istqb_trainer.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev-only-change-later"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


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
        total_seen = sum(q.times_seen for q in questions)
        total_correct = sum(q.times_correct for q in questions)
        percent = round((total_correct / total_seen) * 100) if total_seen > 0 else 0
        due_count = sum(1 for q in questions if q.next_review <= datetime.utcnow())

        data.append({
            "id": lo.id,
            "code": lo.code,
            "title": lo.title,
            "percent": percent,
            "due_count": due_count,
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

    was_correct = (selected == question.correct_option)
    question.register_answer(was_correct)
    db.session.commit()

    return jsonify({
        "correct": was_correct,
        "correct_option": question.correct_option,
        "explanation": question.explanation,
        "new_box": question.box,
    })


if __name__ == "__main__":
    app.run(debug=True)