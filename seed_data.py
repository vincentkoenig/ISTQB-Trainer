from models import db, LearningObjective, Chapter, Question


def seed_lo1(app):
    """LO1 - Grundlagen des Testens (Kapitel 2.1 - 2.7)"""
    with app.app_context():
        # Learning Objective anlegen, falls noch nicht vorhanden
        lo1 = LearningObjective.query.filter_by(code="LO1").first()
        if not lo1:
            lo1 = LearningObjective(code="LO1", title="Grundlagen des Testens")
            db.session.add(lo1)
            db.session.commit()

        chapters_data = [
            {
                "number": "2.1",
                "title": "Was ist Testen?",
                "questions": [
                    {
                        "prompt": "Was ist der Hauptunterschied zwischen Verifizierung und Validierung?",
                        "options": {
                            "A": "Verifizierung prüft die Bedürfnisse der Benutzer, Validierung prüft die Anforderungen",
                            "B": "Verifizierung prüft, ob die spezifizierten Anforderungen erfüllt sind; Validierung prüft, ob die Bedürfnisse der Benutzer erfüllt werden",
                            "C": "Es gibt keinen Unterschied, beide Begriffe sind Synonyme",
                            "D": "Verifizierung wird nur beim dynamischen Testen verwendet, Validierung nur beim statischen Testen",
                        },
                        "correct": "B",
                        "explanation": "Verifizierung = 'Bauen wir das Produkt richtig?' (gegen Spezifikationen). Validierung = 'Bauen wir das richtige Produkt?' (gegen Benutzerbedürfnisse).",
                    },
                    {
                        "prompt": "Was ist der Unterschied zwischen dynamischem und statischem Testen?",
                        "options": {
                            "A": "Dynamisches Testen ist schneller als statisches Testen",
                            "B": "Statisches Testen erfordert die Ausführung der Software, dynamisches Testen nicht",
                            "C": "Dynamisches Testen beinhaltet die Ausführung der Software, statisches Testen nicht",
                            "D": "Beide erfordern die Ausführung der Software",
                        },
                        "correct": "C",
                        "explanation": "Dynamisches Testen = mit Ausführung, statisches Testen = ohne Ausführung (z.B. Reviews).",
                    },
                    {
                        "prompt": "Welche Aussage beschreibt Debugging korrekt?",
                        "options": {
                            "A": "Debugging ist das Finden von Fehlern durch Testfälle",
                            "B": "Debugging umfasst die Reproduktion, Diagnose und Beseitigung der Ursache eines Defekts",
                            "C": "Debugging wird immer vor dem Testen durchgeführt",
                            "D": "Debugging und Testen sind dasselbe",
                        },
                        "correct": "B",
                        "explanation": "Debugging besteht aus drei Schritten: Reproduktion, Diagnose und Ursachenbeseitigung.",
                    },
                    {
                        "prompt": "Was ist KEIN typisches Testziel laut ISTQB?",
                        "options": {
                            "A": "Bewertung von Arbeitsergebnissen wie Anforderungen und Code",
                            "B": "Sicherstellung der Testabdeckung des Testobjekts",
                            "C": "Automatisches Beheben aller gefundenen Defekte",
                            "D": "Risikoreduktion im Zusammenhang mit unzureichender Softwarequalität",
                        },
                        "correct": "C",
                        "explanation": "Testen findet Defekte, das automatische Beheben ist Aufgabe des Debuggings.",
                    },
                    {
                        "prompt": "Was ist der Zweck von Regressionstests?",
                        "options": {
                            "A": "Sicherstellen, dass neue Features korrekt implementiert wurden",
                            "B": "Sicherstellen, dass vorgenommene Änderungen keine neuen Fehler in anderen Bereichen verursacht haben",
                            "C": "Ersetzen der Abnahmetests nach jeder Fehlerbehebung",
                            "D": "Überprüfung, ob die Software erstmalig korrekt funktioniert",
                        },
                        "correct": "B",
                        "explanation": "Regressionstests prüfen, ob Änderungen keine neuen Fehler an anderer Stelle verursacht haben.",
                    },
                ],
            },
            {
                "number": "2.2",
                "title": "Warum ist Testen notwendig?",
                "questions": [
                    {
                        "prompt": "Warum sollten Defekte möglichst frühzeitig im Entwicklungsprozess gefunden werden?",
                        "options": {
                            "A": "Weil frühzeitig gefundene Defekte einfacher zu dokumentieren sind",
                            "B": "Weil das Risiko von Problemen in späteren Projektphasen dadurch minimiert wird",
                            "C": "Weil Defekte in frühen Phasen weniger kritisch sind",
                            "D": "Weil statisches Testen nur in frühen Phasen möglich ist",
                        },
                        "correct": "B",
                        "explanation": "Je früher ein Defekt gefunden wird, desto geringer das Risiko und desto günstiger die Behebung.",
                    },
                    {
                        "prompt": "Welche Arten von Anforderungen soll das Testen laut ISTQB sicherstellen?",
                        "options": {
                            "A": "Nur funktionale Anforderungen",
                            "B": "Nur nicht-funktionale Anforderungen",
                            "C": "Sowohl funktionale als auch nicht-funktionale Anforderungen",
                            "D": "Nur gesetzliche Anforderungen",
                        },
                        "correct": "C",
                        "explanation": "Testen deckt sowohl funktionale als auch nicht-funktionale Anforderungen ab.",
                    },
                    {
                        "prompt": "Welchen Nutzen bietet Testen für Stakeholder?",
                        "options": {
                            "A": "Es ersetzt die Notwendigkeit von Projektmeetings",
                            "B": "Es liefert notwendige Informationen für fundierte Entscheidungen und schafft Vertrauen in die Qualität",
                            "C": "Es garantiert, dass die Software fehlerfrei ist",
                            "D": "Es übernimmt die Aufgabe des Projektmanagements",
                        },
                        "correct": "B",
                        "explanation": "Testergebnisse liefern Stakeholdern die notwendigen Informationen für fundierte Entscheidungen.",
                    },
                    {
                        "prompt": "Vor welchen negativen Konsequenzen schützt das Testen NICHT direkt?",
                        "options": {
                            "A": "Finanzielle Verluste",
                            "B": "Verlust der Reputation",
                            "C": "Rechtliche Risiken",
                            "D": "Personalfluktuation im Entwicklungsteam",
                        },
                        "correct": "D",
                        "explanation": "Personalfluktuation ist kein direktes Risiko, vor dem Testen schützt.",
                    },
                    {
                        "prompt": "Welche Aussage zum Testen ist korrekt?",
                        "options": {
                            "A": "Testen ist ausschließlich ein Prozess zur Qualitätskontrolle",
                            "B": "Testen ist ein strategisches Schlüsselelement, das Effizienz, Zuverlässigkeit und Zufriedenheit der Endanwender beeinflusst",
                            "C": "Testen ist nur in der letzten Phase vor dem Release notwendig",
                            "D": "Testen dient ausschließlich der Einhaltung rechtlicher Vorschriften",
                        },
                        "correct": "B",
                        "explanation": "Testen ist weit mehr als Qualitätskontrolle - ein strategisches Schlüsselelement.",
                    },
                ],
            },
        ]

        _insert_chapters(lo1, chapters_data)


def _insert_chapters(lo, chapters_data):
    """Hilfsfunktion: legt Kapitel + Fragen an, überspringt bereits vorhandene Kapitel."""
    for chapter_data in chapters_data:
        existing = Chapter.query.filter_by(number=chapter_data["number"]).first()
        if existing:
            continue

        chapter = Chapter(
            lo_id=lo.id,
            number=chapter_data["number"],
            title=chapter_data["title"],
        )
        db.session.add(chapter)
        db.session.flush()  # damit chapter.id verfügbar ist

        for q in chapter_data["questions"]:
            question = Question(
                chapter_id=chapter.id,
                prompt=q["prompt"],
                option_a=q["options"]["A"],
                option_b=q["options"]["B"],
                option_c=q["options"]["C"],
                option_d=q["options"]["D"],
                correct_option=q["correct"],
                explanation=q["explanation"],
            )
            db.session.add(question)

    db.session.commit()


if __name__ == "__main__":
    from app import app
    seed_lo1(app)
    print("LO1 (Kapitel 2.1 - 2.2) erfolgreich eingespielt.")