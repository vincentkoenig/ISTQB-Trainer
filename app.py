from flask import Flask, render_template, jsonify
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


app = create_app()   # <-- WICHTIG: das muss VOR den @app.route-Definitionen stehen


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


if __name__ == "__main__":
    app.run(debug=True)