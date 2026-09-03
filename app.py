from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///istqb_trainer.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev-only-change-later"  # reicht für lokale Nutzung

    db.init_app(app)

    with app.app_context():
        db.create_all()  # legt Tabellen an, falls noch nicht vorhanden

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)