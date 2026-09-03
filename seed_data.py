from models import db, LearningObjective, Chapter, Question


def seed_lo1(app):
    """LO1 - Grundlagen des Testens (Kapitel 2.1 - 2.2)"""
    with app.app_context():
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


def seed_lo1_part2(app):
    """LO1 - Grundlagen des Testens (Kapitel 2.3 - 2.7)"""
    with app.app_context():
        lo1 = LearningObjective.query.filter_by(code="LO1").first()
        if not lo1:
            raise RuntimeError("LO1 existiert noch nicht - zuerst seed_lo1() ausführen.")

        chapters_data = [
            {
                "number": "2.3",
                "title": "Grundsätze des Testens",
                "questions": [
                    {
                        "prompt": "Welcher Grundsatz besagt, dass Testen nicht beweisen kann, dass Software fehlerfrei ist?",
                        "options": {
                            "A": "Vollständiges Testen ist unmöglich",
                            "B": "Testen zeigt das Vorhandensein, nicht die Abwesenheit von Fehlerzuständen",
                            "C": "Tests nutzen sich ab",
                            "D": "Testen ist kontextabhängig",
                        },
                        "correct": "B",
                        "explanation": "Testen kann Fehler aufdecken, aber niemals beweisen, dass keine mehr vorhanden sind.",
                    },
                    {
                        "prompt": "Was besagt das Pareto-Prinzip im Zusammenhang mit Softwaretests?",
                        "options": {
                            "A": "80% der Tests sollten automatisiert werden",
                            "B": "80% der Defekte finden sich häufig in 20% der Module",
                            "C": "80% der Testzeit sollte für Regressionstests verwendet werden",
                            "D": "20% der Tester finden 80% aller Defekte",
                        },
                        "correct": "B",
                        "explanation": "Ein Großteil der Defekte konzentriert sich auf wenige Module - wichtig für die Priorisierung.",
                    },
                    {
                        "prompt": "Warum 'nutzen sich Tests ab'?",
                        "options": {
                            "A": "Weil die Testumgebung mit der Zeit langsamer wird",
                            "B": "Weil die Tester mit der Zeit unmotiviert werden",
                            "C": "Weil wiederholte, unveränderte Tests an Effektivität bei der Entdeckung neuer Defekte verlieren",
                            "D": "Weil Testwerkzeuge regelmäßig aktualisiert werden müssen",
                        },
                        "correct": "C",
                        "explanation": "Deshalb müssen Tests und Testdaten regelmäßig angepasst und erweitert werden.",
                    },
                    {
                        "prompt": "Ein System wurde gründlich getestet und es wurden keine Fehler mehr gefunden. Was kann daraus geschlossen werden?",
                        "options": {
                            "A": "Das System ist fehlerfrei und bereit für die Auslieferung",
                            "B": "Das System erfüllt garantiert die Erwartungen der Benutzer",
                            "C": "Es bedeutet nicht automatisch, dass das System brauchbar ist - Validierung ist ebenso wichtig",
                            "D": "Weitere Tests sind überflüssig",
                        },
                        "correct": "C",
                        "explanation": "'Keine Fehler gefunden' heißt nicht 'brauchbares System' - Validierung ist genauso wichtig wie Verifikation.",
                    },
                    {
                        "prompt": "Warum ist frühes Testen so wichtig?",
                        "options": {
                            "A": "Weil in frühen Phasen mehr Tester zur Verfügung stehen",
                            "B": "Weil Defekte in späteren Phasen nicht mehr behoben werden können",
                            "C": "Weil die frühzeitige Erkennung von Defekten die Kosten für deren Behebung in späteren Phasen minimiert",
                            "D": "Weil statisches Testen nur in der Anfangsphase möglich ist",
                        },
                        "correct": "C",
                        "explanation": "Je später ein Defekt gefunden wird, desto teurer die Behebung.",
                    },
                    {
                        "prompt": "Welcher Grundsatz erklärt, warum man Testansätze nicht einfach von einem Projekt auf ein anderes übertragen kann?",
                        "options": {
                            "A": "Tests nutzen sich ab",
                            "B": "Vollständiges Testen ist unmöglich",
                            "C": "Fehlerzustände treten gehäuft auf",
                            "D": "Testen ist kontextabhängig",
                        },
                        "correct": "D",
                        "explanation": "Jedes Projekt hat seinen eigenen Kontext, daher gibt es keinen universellen Testansatz.",
                    },
                ],
            },
            {
                "number": "2.4",
                "title": "Testaktivitäten, Testmittel und Rollen des Testens",
                "questions": [
                    {
                        "prompt": "In welcher Testaktivität werden Testbedingungen aus der Testbasis identifiziert?",
                        "options": {
                            "A": "Testplanung",
                            "B": "Testentwurf",
                            "C": "Testanalyse",
                            "D": "Testrealisierung",
                        },
                        "correct": "C",
                        "explanation": "Die Testanalyse bewertet die Testbasis und identifiziert daraus Testbedingungen ('Was soll getestet werden?').",
                    },
                    {
                        "prompt": "Was ist die Hauptaufgabe der Teststeuerung?",
                        "options": {
                            "A": "Erstellung von Testfällen",
                            "B": "Ergreifen von Korrekturmaßnahmen, um die Testziele zu erreichen",
                            "C": "Archivierung der Testmittel",
                            "D": "Konfiguration der Testumgebung",
                        },
                        "correct": "B",
                        "explanation": "Teststeuerung bedeutet, bei Abweichungen vom Plan korrigierend einzugreifen.",
                    },
                    {
                        "prompt": "In welcher Aktivität werden Testbedingungen in konkrete Testfälle umgewandelt?",
                        "options": {
                            "A": "Testanalyse",
                            "B": "Testplanung",
                            "C": "Testentwurf",
                            "D": "Testdurchführung",
                        },
                        "correct": "C",
                        "explanation": "Der Testentwurf wandelt Testbedingungen in konkrete Testfälle um ('Wie soll getestet werden?').",
                    },
                    {
                        "prompt": "Was gehört NICHT zu den Aufgaben des Testabschlusses?",
                        "options": {
                            "A": "Erstellung von Abschlussberichten",
                            "B": "Archivierung der Testmittel",
                            "C": "Durchführung von Regressionstests",
                            "D": "Weitergabe der Ergebnisse an die Stakeholder",
                        },
                        "correct": "C",
                        "explanation": "Regressionstests gehören zur Testdurchführung, nicht zum Testabschluss.",
                    },
                    {
                        "prompt": "In welcher Reihenfolge finden die Testaktivitäten typischerweise statt?",
                        "options": {
                            "A": "Planung → Analyse → Entwurf → Realisierung → Durchführung → Abschluss",
                            "B": "Analyse → Planung → Durchführung → Entwurf → Realisierung → Abschluss",
                            "C": "Planung → Durchführung → Analyse → Entwurf → Realisierung → Abschluss",
                            "D": "Entwurf → Planung → Analyse → Realisierung → Durchführung → Abschluss",
                        },
                        "correct": "A",
                        "explanation": "Das ist die logische Reihenfolge, auch wenn die Aktivitäten in der Praxis iterativ/parallel ablaufen können.",
                    },
                    {
                        "prompt": "Welche Aussage über Testaktivitäten ist korrekt?",
                        "options": {
                            "A": "Testaktivitäten werden immer streng sequenziell durchgeführt",
                            "B": "Testaktivitäten können iterativ oder parallel ausgeführt werden",
                            "C": "Testaktivitäten sind unabhängig vom Softwareentwicklungsprozess",
                            "D": "Testaktivitäten beginnen erst nach Abschluss der Entwicklung",
                        },
                        "correct": "B",
                        "explanation": "Testaktivitäten werden iterativ oder parallel ausgeführt und an den Projektkontext angepasst.",
                    },
                ],
            },
            {
                "number": "2.5",
                "title": "Testmittel",
                "questions": [
                    {
                        "prompt": "Welches Testmittel entsteht im Rahmen der Testplanung?",
                        "options": {
                            "A": "Testprotokolle",
                            "B": "Testplan und Testzeitplan",
                            "C": "Automatisierte Testskripte",
                            "D": "Zusammenfassender Testbericht",
                        },
                        "correct": "B",
                        "explanation": "Testplan und Testzeitplan sind typische Produkte der Testplanung.",
                    },
                    {
                        "prompt": "In welcher Testaktivität entstehen Fehlerberichte über Defekte in der Testbasis?",
                        "options": {
                            "A": "Testdurchführung",
                            "B": "Testabschluss",
                            "C": "Testanalyse",
                            "D": "Testrealisierung",
                        },
                        "correct": "C",
                        "explanation": "Die Testanalyse bewertet die Testbasis - dabei entstehen Fehlerberichte über Defekte in eben dieser Testbasis.",
                    },
                    {
                        "prompt": "Welches Testmittel gehört zur Testrealisierung (Testimplementierung)?",
                        "options": {
                            "A": "Testbedingungen",
                            "B": "Zusammenfassender Testbericht",
                            "C": "Testfortschrittsberichte",
                            "D": "Test-Suites",
                        },
                        "correct": "D",
                        "explanation": "Test-Suites, Testskripte, Testdaten und Testausführungspläne gehören zur Testrealisierung.",
                    },
                    {
                        "prompt": "Was ist der Hauptzweck von Testfortschrittsberichten?",
                        "options": {
                            "A": "Testfälle nach Prioritäten zu ordnen",
                            "B": "Den tatsächlichen Fortschritt der Tests im Vergleich zu den Planvorgaben zu verfolgen",
                            "C": "Automatisierte Testskripte zu dokumentieren",
                            "D": "Erkenntnisse für zukünftige Projekte festzuhalten",
                        },
                        "correct": "B",
                        "explanation": "Testfortschrittsberichte vergleichen den Ist-Zustand mit dem Plan.",
                    },
                    {
                        "prompt": "Welches Testmittel entsteht beim Testabschluss?",
                        "options": {
                            "A": "Risikoverzeichnis",
                            "B": "Testausführungsplan",
                            "C": "Dokumentierte Erkenntnisse und Änderungsanträge",
                            "D": "Testbeschreibungen",
                        },
                        "correct": "C",
                        "explanation": "Dokumentierte Erkenntnisse und Änderungsanträge sind typische Produkte des Testabschlusses.",
                    },
                    {
                        "prompt": "Wo werden nach Prioritäten geordnete Testfälle erstellt?",
                        "options": {
                            "A": "Testplanung",
                            "B": "Testanalyse",
                            "C": "Testentwurf",
                            "D": "Testdurchführung",
                        },
                        "correct": "C",
                        "explanation": "Der Testentwurf erstellt die konkreten, priorisierten Testfälle.",
                    },
                ],
            },
            {
                "number": "2.6",
                "title": "Verfolgbarkeit zwischen der Testbasis und den Testmitteln",
                "questions": [
                    {
                        "prompt": "Was versteht man unter Verfolgbarkeit (Traceability) im Testprozess?",
                        "options": {
                            "A": "Die automatische Ausführung von Testfällen",
                            "B": "Die Nachverfolgung der Verbindungen zwischen Testbasis und Testmitteln",
                            "C": "Die Dokumentation von Fehlerberichten",
                            "D": "Die Priorisierung von Testfällen nach Schweregrad",
                        },
                        "correct": "B",
                        "explanation": "Verfolgbarkeit bedeutet, die Verbindungen zwischen Testbasis und Testmitteln nachzuverfolgen.",
                    },
                    {
                        "prompt": "Welchen Nutzen bietet die Verknüpfung von Testfällen mit Anforderungen?",
                        "options": {
                            "A": "Sie beschleunigt die Testdurchführung",
                            "B": "Sie ermöglicht die Überprüfung, ob alle Anforderungen getestet wurden",
                            "C": "Sie ersetzt die Notwendigkeit von Regressionstests",
                            "D": "Sie automatisiert den Testentwurf",
                        },
                        "correct": "B",
                        "explanation": "So stellt man sicher, dass keine Anforderung ungetestet bleibt.",
                    },
                    {
                        "prompt": "Warum ist die Verknüpfung von Testergebnissen mit Risiken wichtig?",
                        "options": {
                            "A": "Um die Testdauer zu verkürzen",
                            "B": "Um automatisierte Testskripte zu erstellen",
                            "C": "Um das verbleibende Risiko zu managen",
                            "D": "Um die Anzahl der Testfälle zu reduzieren",
                        },
                        "correct": "C",
                        "explanation": "Durch die Verknüpfung von Testergebnissen mit Risiken kann das verbleibende Risiko gezielt gemanagt werden.",
                    },
                    {
                        "prompt": "Welcher Aspekt wird durch Verfolgbarkeit NICHT direkt unterstützt?",
                        "options": {
                            "A": "Änderungsmanagement",
                            "B": "Audit und Berichtswesen",
                            "C": "Automatische Fehlerbehebung",
                            "D": "Qualitäts- und Leistungsbewertung",
                        },
                        "correct": "C",
                        "explanation": "Automatische Fehlerbehebung ist keine Aufgabe der Verfolgbarkeit - Testen findet Fehler, Debugging behebt sie.",
                    },
                    {
                        "prompt": "Was verbessert eine gute Verfolgbarkeit innerhalb der Organisation?",
                        "options": {
                            "A": "Die Geschwindigkeit der Softwareentwicklung",
                            "B": "Die Transparenz und das Verständnis der Testprozesse",
                            "C": "Die Anzahl der gefundenen Defekte",
                            "D": "Die Motivation der Entwickler",
                        },
                        "correct": "B",
                        "explanation": "Transparenz und Verständnis der Testprozesse sind die zentralen Vorteile guter Verfolgbarkeit.",
                    },
                ],
            },
            {
                "number": "2.7",
                "title": "Wesentliche Kompetenzen und bewährte Praktiken beim Testen",
                "questions": [
                    {
                        "prompt": "Welche Fähigkeit gehört NICHT zu den wesentlichen Kompetenzen eines Testers laut ISTQB?",
                        "options": {
                            "A": "Analytisches und kritisches Denken",
                            "B": "Kommunikationsfähigkeiten und aktives Zuhören",
                            "C": "Fähigkeit, Defekte eigenständig zu beheben (Debugging)",
                            "D": "Sorgfalt, Neugier und Detailgenauigkeit",
                        },
                        "correct": "C",
                        "explanation": "Debugging ist Aufgabe der Entwickler, nicht der Tester. Tester finden Fehler, Entwickler beheben sie.",
                    },
                    {
                        "prompt": "Was bedeutet der Whole-Team-Ansatz?",
                        "options": {
                            "A": "Nur das Testteam ist für die Qualität verantwortlich",
                            "B": "Jedes Teammitglied trägt durch sein Wissen und seine Fähigkeiten zur Verbesserung der Produktqualität bei",
                            "C": "Tester arbeiten unabhängig vom Entwicklungsteam",
                            "D": "Testaktivitäten werden ausschließlich am Ende des Projekts durchgeführt",
                        },
                        "correct": "B",
                        "explanation": "Beim Whole-Team-Ansatz ist Qualität eine gemeinsame Verantwortung des gesamten Teams.",
                    },
                    {
                        "prompt": "Was ist ein Vorteil unabhängiger Tester?",
                        "options": {
                            "A": "Sie können schneller programmieren als Entwickler",
                            "B": "Sie entdecken andere Arten von Defekten als Programmierer",
                            "C": "Sie benötigen keine Kommunikation mit dem Entwicklungsteam",
                            "D": "Sie ersetzen die Notwendigkeit von automatisierten Tests",
                        },
                        "correct": "B",
                        "explanation": "Unabhängige Tester bringen eine andere Perspektive mit und finden dadurch Defekte, die Entwickler übersehen.",
                    },
                    {
                        "prompt": "Was ist eine mögliche Herausforderung bei hoher Unabhängigkeit der Tester?",
                        "options": {
                            "A": "Tester finden weniger Defekte",
                            "B": "Tester verlieren ihr technisches Wissen",
                            "C": "Isolation vom Entwicklungsteam kann zu Kommunikationsproblemen führen",
                            "D": "Die Testkosten sinken zu stark",
                        },
                        "correct": "C",
                        "explanation": "Je unabhängiger die Tester, desto größer das Risiko von Kommunikationsproblemen.",
                    },
                    {
                        "prompt": "Warum ist Fachwissen (Domänenkenntnisse) für Tester wichtig?",
                        "options": {
                            "A": "Um die Software selbst entwickeln zu können",
                            "B": "Um die fachlichen Anforderungen und den Kontext des Testobjekts zu verstehen",
                            "C": "Um das Projektmanagement zu übernehmen",
                            "D": "Um automatisierte Testskripte zu schreiben",
                        },
                        "correct": "B",
                        "explanation": "Ohne Domänenkenntnisse kann ein Tester die fachlichen Anforderungen nicht richtig einordnen und testen.",
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
        db.session.flush()

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
    seed_lo1_part2(app)
    print("LO1 (alle Kapitel 2.1 - 2.7) erfolgreich eingespielt.")