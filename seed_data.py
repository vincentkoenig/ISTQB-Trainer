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


def seed_lo2(app):
    """LO2 - Testen im Softwareentwicklungslebenszyklus (Kapitel 3.1 - 3.10)"""
    with app.app_context():
        lo2 = LearningObjective.query.filter_by(code="LO2").first()
        if not lo2:
            lo2 = LearningObjective(code="LO2", title="Testen im Softwareentwicklungslebenszyklus")
            db.session.add(lo2)
            db.session.commit()

        chapters_data = [
            {
                "number": "3.1",
                "title": "Auswirkungen des SDLC auf das Testen",
                "questions": [
                    {
                        "prompt": "Welches Entwicklungsmodell erfordert die detaillierteste Testdokumentation?",
                        "options": {
                            "A": "Agile Modelle",
                            "B": "Iterative und inkrementelle Modelle",
                            "C": "Sequenzielle Modelle",
                            "D": "Alle Modelle erfordern den gleichen Dokumentationsgrad",
                        },
                        "correct": "C",
                        "explanation": "Sequenzielle Modelle erfordern detaillierte und kostspielige Testdokumentation.",
                    },
                    {
                        "prompt": "In welchem Modell erfolgt dynamisches Testen erst nach der Erstellung des Codes?",
                        "options": {
                            "A": "Agile Modelle",
                            "B": "Iterative und inkrementelle Modelle",
                            "C": "Sequenzielle Modelle",
                            "D": "In keinem Modell",
                        },
                        "correct": "C",
                        "explanation": "Bei sequenziellen Modellen wird der Code zuerst vollständig erstellt, danach beginnt das dynamische Testen.",
                    },
                    {
                        "prompt": "Welches Modell legt den größten Fokus auf Testautomatisierung?",
                        "options": {
                            "A": "Sequenzielle Modelle",
                            "B": "Iterative und inkrementelle Modelle",
                            "C": "Agile Modelle",
                            "D": "Alle Modelle gleichermaßen",
                        },
                        "correct": "C",
                        "explanation": "Agile Modelle setzen auf vollständige Automatisierung und kontinuierliches Regressionstesting.",
                    },
                    {
                        "prompt": "Warum sind Regressionstests besonders wichtig bei iterativen und agilen Modellen?",
                        "options": {
                            "A": "Weil die Testdokumentation minimal ist",
                            "B": "Weil jede Iteration/Änderung neue Defekte in bestehender Funktionalität verursachen kann",
                            "C": "Weil die Tester weniger erfahren sind",
                            "D": "Weil sequenzielle Modelle keine Regressionstests benötigen",
                        },
                        "correct": "B",
                        "explanation": "Bei jeder Iteration können Änderungen bestehende Funktionalität beeinflussen.",
                    },
                    {
                        "prompt": "Welche Aussage über die Rolle des Testers in agilen Modellen ist korrekt?",
                        "options": {
                            "A": "Tester haben streng formale Rollen und Aufgaben",
                            "B": "Tester konzentrieren sich ausschließlich auf manuelle Tests",
                            "C": "Tester agieren als Testexperten und reagieren schnell auf Änderungen",
                            "D": "Tester sind nur am Ende des Projekts beteiligt",
                        },
                        "correct": "C",
                        "explanation": "In agilen Modellen sind Tester flexible Experten, die schnell auf Änderungen reagieren.",
                    },
                    {
                        "prompt": "Was ist ein Merkmal agiler Modelle im Hinblick auf Testtechniken?",
                        "options": {
                            "A": "Klassischer Ansatz mit hoher Kontrolle",
                            "B": "Fokus auf erfahrungsbasierte Testtechniken",
                            "C": "Ausschließlich automatisierte Testtechniken ohne manuelle Tests",
                            "D": "Keine spezifischen Testtechniken erforderlich",
                        },
                        "correct": "B",
                        "explanation": "Agile Modelle setzen auf erfahrungsbasierte Testtechniken neben der Automatisierung.",
                    },
                ],
            },
            {
                "number": "3.2",
                "title": "SDLC und gute Praktiken für das Testen",
                "questions": [
                    {
                        "prompt": "Welche der folgenden ist KEINE der genannten guten Testpraktiken?",
                        "options": {
                            "A": "Zuweisung geeigneter Testaktivitäten zu jeder Entwicklungsaktivität",
                            "B": "Teilnahme der Tester an Reviews",
                            "C": "Vollständige Testautomatisierung aller Testfälle vor Projektbeginn",
                            "D": "Einhaltung des Prinzips der frühen Tests",
                        },
                        "correct": "C",
                        "explanation": "Vollständige Testautomatisierung aller Testfälle vor Projektbeginn ist keine der genannten guten Testpraktiken.",
                    },
                    {
                        "prompt": "Warum sollten Tester an Reviews teilnehmen?",
                        "options": {
                            "A": "Um die Entwickler bei der Programmierung zu unterstützen",
                            "B": "Um die frühzeitige Fehlererkennung zu unterstützen und die Qualität der Testbasis zu verbessern",
                            "C": "Um die Testdokumentation zu reduzieren",
                            "D": "Um die Projektkosten zu erhöhen",
                        },
                        "correct": "B",
                        "explanation": "Durch die Teilnahme an Reviews können Tester Defekte in der Testbasis frühzeitig erkennen.",
                    },
                    {
                        "prompt": "Was bedeutet das Prinzip der frühen Tests in Bezug auf gute Testpraktiken?",
                        "options": {
                            "A": "Alle Tests sollten vor der Entwicklung abgeschlossen sein",
                            "B": "Testanalyse und Testentwurf sollten bereits in der entsprechenden Entwicklungsphase beginnen",
                            "C": "Nur automatisierte Tests sollten früh durchgeführt werden",
                            "D": "Frühes Testen ist nur bei agilen Modellen relevant",
                        },
                        "correct": "B",
                        "explanation": "Testanalyse und Testentwurf beginnen parallel zur jeweiligen Entwicklungsphase, nicht erst am Ende.",
                    },
                    {
                        "prompt": "Warum haben verschiedene Teststufen spezifische Ziele?",
                        "options": {
                            "A": "Um die Testdokumentation zu vereinfachen",
                            "B": "Um eine fokussierte und effiziente Testdurchführung zu ermöglichen",
                            "C": "Um die Anzahl der Tester zu reduzieren",
                            "D": "Um nur funktionale Anforderungen zu testen",
                        },
                        "correct": "B",
                        "explanation": "Spezifische Ziele pro Teststufe sorgen für Fokus und Effizienz.",
                    },
                    {
                        "prompt": "Was ist der Hauptnutzen guter Testpraktiken laut dieser Präsentation?",
                        "options": {
                            "A": "Sie ersetzen die Notwendigkeit eines Softwareentwicklungsmodells",
                            "B": "Sie unterstützen die hohe Produktqualität und verkürzen die Zeit zur Fehlerbehebung",
                            "C": "Sie eliminieren alle Defekte vor dem Release",
                            "D": "Sie sind nur bei sequenziellen Modellen anwendbar",
                        },
                        "correct": "B",
                        "explanation": "Hohe Qualität und schnellere Fehlerbehebung sind die zentralen Vorteile.",
                    },
                ],
            },
            {
                "number": "3.3",
                "title": "Testen als Treiber für die Softwareentwicklung",
                "questions": [
                    {
                        "prompt": "Was ist das zentrale Prinzip von TDD (Testgetriebene Entwicklung)?",
                        "options": {
                            "A": "Tests werden nach dem Code geschrieben, um Fehler zu finden",
                            "B": "Tests werden vor dem Code geschrieben und der Code wird geschrieben, um die Tests zu bestehen",
                            "C": "Tests werden nur für kritische Funktionen geschrieben",
                            "D": "Tests werden ausschließlich von unabhängigen Testern erstellt",
                        },
                        "correct": "B",
                        "explanation": "Bei TDD gilt: erst der Test, dann der Code (Red-Green-Refactor-Zyklus).",
                    },
                    {
                        "prompt": "Worauf basieren die Tests bei ATDD?",
                        "options": {
                            "A": "Auf der technischen Architektur des Systems",
                            "B": "Auf den im Systemdesign definierten Abnahmekriterien",
                            "C": "Auf den Erfahrungen der Tester",
                            "D": "Auf den Ergebnissen vorheriger Testzyklen",
                        },
                        "correct": "B",
                        "explanation": "ATDD leitet die Tests direkt aus den Abnahmekriterien ab.",
                    },
                    {
                        "prompt": "Was unterscheidet BDD von den anderen testgetriebenen Ansätzen?",
                        "options": {
                            "A": "BDD verwendet ausschließlich manuelle Tests",
                            "B": "BDD beschreibt das gewünschte Verhalten in natürlicher Sprache, die für Stakeholder verständlich ist",
                            "C": "BDD erfordert keine Testautomatisierung",
                            "D": "BDD wird nur bei sequenziellen Entwicklungsmodellen eingesetzt",
                        },
                        "correct": "B",
                        "explanation": "BDD nutzt natürliche Sprache (z.B. Given-When-Then), damit auch nicht-technische Stakeholder die Tests verstehen.",
                    },
                    {
                        "prompt": "Was haben TDD, ATDD und BDD gemeinsam?",
                        "options": {
                            "A": "Sie alle verwenden ausschließlich manuelle Testtechniken",
                            "B": "Sie alle legen großen Wert auf frühes Testen und Testautomatisierung",
                            "C": "Sie alle erfordern detaillierte Testdokumentation",
                            "D": "Sie alle werden nur in agilen Projekten eingesetzt",
                        },
                        "correct": "B",
                        "explanation": "Frühes Testen und Automatisierung sind die gemeinsamen Stärken aller drei Ansätze.",
                    },
                    {
                        "prompt": "Welche Aktivität gehört zum TDD-Prozess neben dem Schreiben von Tests und Code?",
                        "options": {
                            "A": "Erstellung von Testdokumentation",
                            "B": "Refaktorisierung von Code und Tests",
                            "C": "Durchführung von Abnahmetests",
                            "D": "Erstellung von Risikoverzeichnissen",
                        },
                        "correct": "B",
                        "explanation": "Refaktorisierung ist ein wesentlicher Bestandteil von TDD, um Qualität und Flexibilität langfristig zu erhalten.",
                    },
                ],
            },
            {
                "number": "3.4",
                "title": "DevOps und Testen",
                "questions": [
                    {
                        "prompt": "Was ist das Hauptziel der DevOps-Methodik?",
                        "options": {
                            "A": "Vollständige Ersetzung manueller Tests durch Automatisierung",
                            "B": "Synergien und Effizienz durch enge Zusammenarbeit zwischen Entwicklung und Betrieb",
                            "C": "Ausschließliche Fokussierung auf die Testdokumentation",
                            "D": "Verzicht auf kontinuierliche Integration",
                        },
                        "correct": "B",
                        "explanation": "DevOps zielt auf Synergien und Effizienz durch enge Zusammenarbeit zwischen Entwicklung und Betrieb ab.",
                    },
                    {
                        "prompt": "Welcher der folgenden ist KEIN genannter Vorteil von DevOps für das Testen?",
                        "options": {
                            "A": "Schnelles Feedback",
                            "B": "Automatisierte Prozesse",
                            "C": "Vollständige Abschaffung des manuellen Testens",
                            "D": "Sichtbarkeit von nicht-funktionalen Qualitätsmerkmalen",
                        },
                        "correct": "C",
                        "explanation": "Manuelles Testen bleibt wichtig, besonders aus Benutzerperspektive - eine Abschaffung wurde nicht genannt.",
                    },
                    {
                        "prompt": "Warum ist manuelles Testen auch in DevOps-Umgebungen weiterhin notwendig?",
                        "options": {
                            "A": "Weil Automatisierung zu teuer ist",
                            "B": "Weil es insbesondere aus der Benutzerperspektive weiterhin wichtig ist",
                            "C": "Weil CI/CD-Tools nicht zuverlässig sind",
                            "D": "Weil DevOps keine Automatisierung unterstützt",
                        },
                        "correct": "B",
                        "explanation": "Automatisierte Tests können nicht alles abdecken, was ein Mensch aus Nutzersicht beurteilen kann.",
                    },
                    {
                        "prompt": "Was gehört zu den Herausforderungen von DevOps im Hinblick auf das Testen?",
                        "options": {
                            "A": "Zu viel manuelles Testen",
                            "B": "Die Notwendigkeit einer definierten Bereitstellungspipeline sowie geeigneter CI/CD-Tools und Ressourcen",
                            "C": "Fehlende Automatisierung ist niemals ein Problem",
                            "D": "DevOps benötigt keine Werkzeuge",
                        },
                        "correct": "B",
                        "explanation": "Eine definierte Pipeline sowie passende CI/CD-Tools und Ressourcen sind zentrale Herausforderungen.",
                    },
                    {
                        "prompt": "Welchen Effekt hat DevOps laut Fazit auf die Fehlererkennung?",
                        "options": {
                            "A": "Fehlererkennung wird langsamer",
                            "B": "Fehlererkennung erfolgt schneller durch frühere Integration von Tests",
                            "C": "DevOps hat keinen Einfluss auf die Fehlererkennung",
                            "D": "Fehler werden erst am Ende des Projekts erkannt",
                        },
                        "correct": "B",
                        "explanation": "Durch frühere Integration von Tests werden Fehler schneller erkannt.",
                    },
                ],
            },
            {
                "number": "3.5",
                "title": "Shift-Left-Ansatz",
                "questions": [
                    {
                        "prompt": "Was bedeutet der 'Shift-Left'-Ansatz im Softwaretest?",
                        "options": {
                            "A": "Tests werden in früheren Phasen des Entwicklungszyklus durchgeführt",
                            "B": "Tests werden ausschließlich am Ende des Projekts durchgeführt",
                            "C": "Tests werden komplett automatisiert und benötigen keine manuelle Prüfung mehr",
                            "D": "Tests werden nur bei sequenziellen Modellen eingesetzt",
                        },
                        "correct": "A",
                        "explanation": "Shift-Left bedeutet, Tests in frühere Phasen des Entwicklungszyklus zu verschieben.",
                    },
                    {
                        "prompt": "Bedeutet 'Shift-Left', dass Testen in späteren Phasen übersprungen wird?",
                        "options": {
                            "A": "Ja, spätere Testphasen entfallen komplett",
                            "B": "Ja, aber nur bei agilen Projekten",
                            "C": "Nein, der Fokus liegt zusätzlich auf der frühzeitigen Erkennung und Behebung von Defekten",
                            "D": "Ja, Shift-Left ersetzt alle anderen Testaktivitäten",
                        },
                        "correct": "C",
                        "explanation": "Spätere Testphasen entfallen nicht, es kommt lediglich ein zusätzlicher Fokus auf frühe Fehlererkennung hinzu.",
                    },
                    {
                        "prompt": "Welche der folgenden Herausforderungen wird beim Shift-Left-Ansatz genannt?",
                        "options": {
                            "A": "Zu wenig Testautomatisierung",
                            "B": "Fehlende gesetzliche Vorschriften",
                            "C": "Mangel an Testtechniken",
                            "D": "Zusätzliche Aufwendungen für Schulungen und Ressourcen in frühen Phasen",
                        },
                        "correct": "D",
                        "explanation": "Zusätzliche Schulungs- und Ressourcenaufwände in frühen Phasen sind eine typische Herausforderung.",
                    },
                    {
                        "prompt": "Welcher Vorteil wird dem Shift-Left-Ansatz zugeschrieben?",
                        "options": {
                            "A": "Vollständige Elimination aller Defekte",
                            "B": "Kostenersparnis in späteren Phasen",
                            "C": "Wegfall der Notwendigkeit von Stakeholder-Kommunikation",
                            "D": "Verzicht auf statische Code-Analyse",
                        },
                        "correct": "B",
                        "explanation": "Durch frühe Fehlererkennung spart man Kosten, die sonst in späteren Phasen anfallen würden.",
                    },
                    {
                        "prompt": "Was gehört laut Präsentation zu den Gründen, 'Shift-Left' einzuführen?",
                        "options": {
                            "A": "Verzicht auf kontinuierliche Integration",
                            "B": "Reduzierung der Testabdeckung",
                            "C": "Vermeidung nicht-funktionaler Tests",
                            "D": "Statische Code-Analyse und Überprüfung der Spezifikationen",
                        },
                        "correct": "D",
                        "explanation": "Statische Code-Analyse und Spezifikationsüberprüfung gehören zu den genannten Gründen für Shift-Left.",
                    },
                ],
            },
            {
                "number": "3.6",
                "title": "Retrospektiven und Prozessverbesserung",
                "questions": [
                    {
                        "prompt": "Wann werden Retrospektiven typischerweise durchgeführt?",
                        "options": {
                            "A": "Vor Beginn eines Projekts",
                            "B": "Während der Testplanung",
                            "C": "Nach Abschluss eines Projekts, einer Iteration oder eines wichtigen Meilensteins",
                            "D": "Ausschließlich bei sequenziellen Entwicklungsmodellen",
                        },
                        "correct": "C",
                        "explanation": "Retrospektiven finden nach Abschluss eines Projekts, einer Iteration oder eines wichtigen Meilensteins statt.",
                    },
                    {
                        "prompt": "Welche Frage wird in einer Retrospektive NICHT typischerweise gestellt?",
                        "options": {
                            "A": "Was hat gut funktioniert und sollte beibehalten werden?",
                            "B": "Welche Aktivitäten sind gescheitert und erfordern Verbesserung?",
                            "C": "Wie können Verbesserungen für die Zukunft umgesetzt werden?",
                            "D": "Welcher Mitarbeiter ist für Fehler verantwortlich zu machen?",
                        },
                        "correct": "D",
                        "explanation": "Bei Retrospektiven geht es nicht um Schuldzuweisungen, sondern um konstruktive Prozessanalyse.",
                    },
                    {
                        "prompt": "Was gehört zu den Vorteilen von Retrospektiven für das Testen?",
                        "options": {
                            "A": "Stärkung des Teamzusammenhalts und Optimierung der Zusammenarbeit",
                            "B": "Vollständige Automatisierung aller Testfälle",
                            "C": "Wegfall der Notwendigkeit von Testdokumentation",
                            "D": "Verzicht auf Testgrundlagen",
                        },
                        "correct": "A",
                        "explanation": "Teamzusammenhalt und Zusammenarbeit gehören zu den genannten Vorteilen.",
                    },
                    {
                        "prompt": "Wovon hängt die Effektivität von Retrospektiven laut Präsentation ab?",
                        "options": {
                            "A": "Ausschließlich von der Teamgröße",
                            "B": "Von der Anzahl der durchgeführten Testfälle",
                            "C": "Von der Wahl des Entwicklungsmodells",
                            "D": "Von Implementierung der Empfehlungen, Änderungsmanagement und Engagement des Teams",
                        },
                        "correct": "D",
                        "explanation": "Alle drei Faktoren bestimmen die Effektivität von Retrospektiven.",
                    },
                    {
                        "prompt": "Was ist das übergeordnete Ziel von Retrospektiven laut Fazit?",
                        "options": {
                            "A": "Kontinuierliche Verbesserung des Softwareentwicklungsprozesses",
                            "B": "Reduzierung der Teamgröße",
                            "C": "Vollständige Vermeidung von Fehlern",
                            "D": "Ersatz der Testdokumentation durch mündliche Absprachen",
                        },
                        "correct": "A",
                        "explanation": "Kontinuierliche Verbesserung ist das übergeordnete Ziel.",
                    },
                ],
            },
            {
                "number": "3.7",
                "title": "Teststufen",
                "questions": [
                    {
                        "prompt": "Welche Teststufe konzentriert sich auf das Testen einzelner Module durch Entwickler mithilfe von Test-Frameworks?",
                        "options": {
                            "A": "Systemtest",
                            "B": "Komponententest",
                            "C": "Abnahmetest",
                            "D": "Systemintegrationstest",
                        },
                        "correct": "B",
                        "explanation": "Der Komponententest (Unit-Test) prüft einzelne Module mithilfe von Test-Frameworks, meist durch Entwickler.",
                    },
                    {
                        "prompt": "Welche Integrationsstrategien werden im Zusammenhang mit Komponentenintegrationstests genannt?",
                        "options": {
                            "A": "Nur Bottom-up",
                            "B": "Nur Top-down",
                            "C": "Top-down, Bottom-up und Big-Bang",
                            "D": "Nur Big-Bang",
                        },
                        "correct": "C",
                        "explanation": "Top-down, Bottom-up und Big-Bang sind die genannten Integrationsstrategien.",
                    },
                    {
                        "prompt": "Wer führt den Abnahmetest typischerweise durch?",
                        "options": {
                            "A": "Entwickler mit Unit-Test-Frameworks",
                            "B": "Ein unabhängiges Testteam ausschließlich im Testlabor",
                            "C": "Endbenutzer oder ein Team, das ihre Interessen vertritt",
                            "D": "Ausschließlich automatisierte Testskripte ohne menschliche Beteiligung",
                        },
                        "correct": "C",
                        "explanation": "Der Abnahmetest wird typischerweise von Endbenutzern oder einem Team, das ihre Interessen vertritt, durchgeführt.",
                    },
                    {
                        "prompt": "Worauf konzentriert sich der Systemintegrationstest?",
                        "options": {
                            "A": "Auf einzelne Codefragmente",
                            "B": "Auf die Schnittstellen zwischen dem getesteten System und anderen Systemen oder externen Diensten",
                            "C": "Auf die Zusammenarbeit einzelner Module innerhalb derselben Anwendung",
                            "D": "Auf die Validierung geschäftlicher Anforderungen der Endbenutzer",
                        },
                        "correct": "B",
                        "explanation": "Der Systemintegrationstest prüft die Schnittstellen zu anderen Systemen oder externen Diensten.",
                    },
                    {
                        "prompt": "Wodurch unterscheiden sich die verschiedenen Teststufen laut Präsentation?",
                        "options": {
                            "A": "Ausschließlich durch die Anzahl der Tester",
                            "B": "Durch Testobjekt, Ziele, Basis, Fehlerhandling und Ansatz",
                            "C": "Ausschließlich durch die verwendete Programmiersprache",
                            "D": "Ausschließlich durch die Projektdauer",
                        },
                        "correct": "B",
                        "explanation": "Testobjekt, Ziele, Basis, Fehlerhandling und Ansatz sind die unterscheidenden Merkmale der Teststufen.",
                    },
                ],
            },
            {
                "number": "3.8",
                "title": "Testarten",
                "questions": [
                    {
                        "prompt": "Welche Frage beantworten funktionale Tests?",
                        "options": {
                            "A": "'Wie schnell' arbeitet das System?",
                            "B": "'Was' soll das System tun?",
                            "C": "'Wie sicher' ist das System?",
                            "D": "'Wie wartbar' ist das System?",
                        },
                        "correct": "B",
                        "explanation": "Funktionale Tests beantworten die Frage 'Was soll das System tun?'.",
                    },
                    {
                        "prompt": "Welche der folgenden Eigenschaften gehört zu den nicht-funktionalen Tests?",
                        "options": {
                            "A": "Funktionale Vollständigkeit",
                            "B": "Funktionale Korrektheit",
                            "C": "IT-Sicherheit",
                            "D": "Funktionale Angemessenheit",
                        },
                        "correct": "C",
                        "explanation": "IT-Sicherheit gehört zu den nicht-funktionalen Qualitätsmerkmalen.",
                    },
                    {
                        "prompt": "Worauf basiert ein Black-Box-Test?",
                        "options": {
                            "A": "Auf der internen Struktur des Systems",
                            "B": "Auf dem Quellcode",
                            "C": "Auf externer Dokumentation bzw. der Spezifikation",
                            "D": "Auf der Testabdeckung des Codes",
                        },
                        "correct": "C",
                        "explanation": "Black-Box-Tests basieren auf externer Dokumentation bzw. der Spezifikation.",
                    },
                    {
                        "prompt": "Was ist das Ziel des White-Box-Tests?",
                        "options": {
                            "A": "Überprüfung der Übereinstimmung mit externer Dokumentation",
                            "B": "Erzielung eines akzeptablen Testabdeckungsgrads basierend auf der internen Struktur",
                            "C": "Bewertung der Gebrauchstauglichkeit",
                            "D": "Prüfung der IT-Sicherheit",
                        },
                        "correct": "B",
                        "explanation": "White-Box-Tests zielen auf einen akzeptablen Testabdeckungsgrad basierend auf der internen Struktur ab.",
                    },
                    {
                        "prompt": "Wie lassen sich funktionale Tests, nicht-funktionale Tests, Black-Box- und White-Box-Tests auf die Teststufen anwenden?",
                        "options": {
                            "A": "Nur funktionale Tests können auf allen Teststufen angewendet werden",
                            "B": "Sie können nur auf dem Systemtest angewendet werden",
                            "C": "Alle vier Testarten können auf allen Teststufen angewendet werden",
                            "D": "Nur White-Box-Tests sind auf allen Teststufen anwendbar",
                        },
                        "correct": "C",
                        "explanation": "Alle vier Testarten sind auf jeder Teststufe anwendbar.",
                    },
                ],
            },
            {
                "number": "3.9",
                "title": "Fehlernachtest und Regressionstest",
                "questions": [
                    {
                        "prompt": "Was überprüft der Fehlernachtest?",
                        "options": {
                            "A": "Ob andere, nicht geänderte Teile des Systems noch funktionieren",
                            "B": "Die Behebung des ursprünglichen Fehlers",
                            "C": "Die Performance des gesamten Systems",
                            "D": "Die Benutzerfreundlichkeit neuer Funktionen",
                        },
                        "correct": "B",
                        "explanation": "Der Fehlernachtest überprüft gezielt, ob der ursprünglich gemeldete Fehler tatsächlich behoben wurde.",
                    },
                    {
                        "prompt": "Was ist das Hauptziel des Regressionstests?",
                        "options": {
                            "A": "Sicherstellen, dass ein spezifischer Fehler behoben wurde",
                            "B": "Neue Funktionen zu entwickeln",
                            "C": "Verhindern von Regressionen, also dass Änderungen bestehende Funktionen beeinträchtigen",
                            "D": "Die Testdokumentation zu reduzieren",
                        },
                        "correct": "C",
                        "explanation": "Regressionstests verhindern, dass Änderungen bestehende Funktionen negativ beeinflussen.",
                    },
                    {
                        "prompt": "Warum wird für Regressionstests Automatisierung empfohlen?",
                        "options": {
                            "A": "Weil manuelle Tests generell ungenau sind",
                            "B": "Wegen der Wiederholbarkeit und Skalierbarkeit",
                            "C": "Weil Regressionstests nur einmalig durchgeführt werden",
                            "D": "Weil Automatisierung günstiger ist als Personal",
                        },
                        "correct": "B",
                        "explanation": "Wiederholbarkeit und Skalierbarkeit sind die Hauptgründe für Automatisierung bei Regressionstests.",
                    },
                    {
                        "prompt": "Was gehört zum Umfang eines Regressionstests?",
                        "options": {
                            "A": "Ausschließlich das geänderte Modul",
                            "B": "Ausschließlich Module, die vom Endbenutzer genutzt werden",
                            "C": "Ausschließlich die Testdokumentation",
                            "D": "Das geänderte Modul sowie andere betroffene Module/Systeme",
                        },
                        "correct": "D",
                        "explanation": "Der Regressionstest umfasst sowohl das geänderte Modul als auch andere betroffene Module/Systeme.",
                    },
                    {
                        "prompt": "Was wird auf der Abnahme-Teststufe im Kontext von Fehlernachtest/Regressionstest geprüft?",
                        "options": {
                            "A": "Ob die Änderungen den Erwartungen der Benutzer entsprechen",
                            "B": "Ausschließlich die Codequalität",
                            "C": "Ausschließlich die Schnittstellen zwischen Modulen",
                            "D": "Die interne Struktur des Systems",
                        },
                        "correct": "A",
                        "explanation": "Auf Abnahme-Ebene wird geprüft, ob die Änderungen den Benutzererwartungen entsprechen.",
                    },
                ],
            },
            {
                "number": "3.10",
                "title": "Wartungstest",
                "questions": [
                    {
                        "prompt": "Was ist das Ziel von Wartungstests?",
                        "options": {
                            "A": "Nur Fehler in neu entwickelten Modulen zu finden",
                            "B": "Behebung von Fehlern in laufenden Systemen sowie Anpassung an Änderungen der Betriebsumgebung",
                            "C": "Ausschließlich das Testen vor dem ersten Release",
                            "D": "Ersatz für Systemtests",
                        },
                        "correct": "B",
                        "explanation": "Wartungstests beheben Fehler in laufenden Systemen und passen die Software an Änderungen der Betriebsumgebung an.",
                    },
                    {
                        "prompt": "Welche Kategorie gehört NICHT zu den Wartungstests?",
                        "options": {
                            "A": "Änderungen (Updates, Hotfixes)",
                            "B": "Updates/Migrationen",
                            "C": "Außerbetriebnahme",
                            "D": "Erstinstallation eines komplett neuen Systems",
                        },
                        "correct": "D",
                        "explanation": "Die Erstinstallation eines komplett neuen Systems gehört nicht zu den Wartungstests, da diese erst nach der Einführung ansetzen.",
                    },
                    {
                        "prompt": "Was ist Teil der 'Einflussanalyse der Änderung'?",
                        "options": {
                            "A": "Bewertung des mit der Änderung verbundenen Risikos und Entscheidung über Testumfang",
                            "B": "Automatische Generierung von Testfällen",
                            "C": "Erstellung der ursprünglichen Systemarchitektur",
                            "D": "Schulung der Endbenutzer",
                        },
                        "correct": "A",
                        "explanation": "Bei der Einflussanalyse geht es um Risikobewertung und die Entscheidung über den nötigen Testumfang.",
                    },
                    {
                        "prompt": "Warum wird bei der Außerbetriebnahme eines Systems getestet?",
                        "options": {
                            "A": "Um neue Funktionen einzuführen",
                            "B": "Um die Performance zu steigern",
                            "C": "Im Zusammenhang mit Datenarchivierung und Testen der Wiederherstellung",
                            "D": "Um die Benutzeroberfläche zu verbessern",
                        },
                        "correct": "C",
                        "explanation": "Bei der Außerbetriebnahme spielen Datenarchivierung und das Testen der Wiederherstellung eine zentrale Rolle.",
                    },
                    {
                        "prompt": "Was wird bei der Durchführung der Wartungstests neben der Korrektheit der Änderung noch geprüft?",
                        "options": {
                            "A": "Regressionen in unveränderten Bereichen des Systems",
                            "B": "Ausschließlich die Dokumentation",
                            "C": "Die ursprüngliche Projektplanung",
                            "D": "Die Teamzusammensetzung",
                        },
                        "correct": "A",
                        "explanation": "Neben der Korrektheit der Änderung selbst werden auch Regressionen in unveränderten Bereichen geprüft.",
                    },
                ],
            },
        ]

        _insert_chapters(lo2, chapters_data)


def seed_lo4(app):
    """LO4 - Testanalyse und -entwurf (Kapitel 5.1 - 5.5)"""
    with app.app_context():
        lo4 = LearningObjective.query.filter_by(code="LO4").first()
        if not lo4:
            lo4 = LearningObjective(code="LO4", title="Testanalyse und -entwurf")
            db.session.add(lo4)
            db.session.commit()

        chapters_data = [
            {
                "number": "5.1",
                "title": "Testverfahren im Überblick",
                "questions": [
                    {
                        "prompt": "Was unterstützen Testtechniken laut Präsentation?",
                        "options": {
                            "A": "Ausschließlich die Testdurchführung",
                            "B": "Ausschließlich das Projektmanagement",
                            "C": "Die Testanalyse und das Testdesign",
                            "D": "Ausschließlich die Testautomatisierung",
                        },
                        "correct": "C",
                        "explanation": "Testtechniken unterstützen die Testanalyse (was?) und das Testdesign (wie?).",
                    },
                    {
                        "prompt": "Worauf basiert das Black-Box-Testverfahren?",
                        "options": {
                            "A": "Auf der internen Struktur des Codes",
                            "B": "Auf dem spezifizierten Verhalten, ohne Bezug auf die interne Struktur",
                            "C": "Ausschließlich auf der Erfahrung des Testers",
                            "D": "Auf dem Quellcode-Review",
                        },
                        "correct": "B",
                        "explanation": "Black-Box-Verfahren analysieren das spezifizierte Verhalten, ohne die interne Struktur zu berücksichtigen.",
                    },
                    {
                        "prompt": "Warum bleiben Black-Box-Testfälle auch bei Änderungen der Implementierung nützlich?",
                        "options": {
                            "A": "Weil sie automatisch aktualisiert werden",
                            "B": "Weil sie unabhängig von der Implementierung sind, solange das Verhalten gleich bleibt",
                            "C": "Weil sie nur einmal erstellt werden müssen",
                            "D": "Weil sie keine Testdaten benötigen",
                        },
                        "correct": "B",
                        "explanation": "Solange sich das Verhalten nicht ändert, bleiben Black-Box-Testfälle unabhängig von der konkreten Implementierung gültig.",
                    },
                    {
                        "prompt": "Wovon hängt die Effektivität erfahrungsbasierter Testverfahren ab?",
                        "options": {
                            "A": "Von der Anzahl der Testfälle",
                            "B": "Von der verwendeten Programmiersprache",
                            "C": "Von den Fähigkeiten und der Erfahrung des Testers",
                            "D": "Von der Testautomatisierung",
                        },
                        "correct": "C",
                        "explanation": "Bei erfahrungsbasierten Verfahren hängt alles vom Wissen und der Erfahrung des Testers ab.",
                    },
                    {
                        "prompt": "Wann werden White-Box-Testfälle typischerweise erstellt?",
                        "options": {
                            "A": "Vor der Spezifikation der Anforderungen",
                            "B": "Unabhängig von der Implementierung",
                            "C": "Ausschließlich vom Endbenutzer",
                            "D": "Nach der Planung oder Implementierung des zu testenden Objekts",
                        },
                        "correct": "D",
                        "explanation": "White-Box-Testfälle werden nach der Planung oder Implementierung erstellt, da sie die interne Struktur kennen müssen.",
                    },
                ],
            },
            {
                "number": "5.2",
                "title": "Black-Box-Testverfahren",
                "questions": [
                    {
                        "prompt": "Was ist das Grundprinzip der Äquivalenzklassenbildung?",
                        "options": {
                            "A": "Nur Grenzwerte werden getestet",
                            "B": "Daten werden in Gruppen aufgeteilt, die auf die gleiche Weise verarbeitet werden - ein Defekt in einem Wert gilt für die ganze Klasse",
                            "C": "Jeder einzelne mögliche Wert muss getestet werden",
                            "D": "Nur Ausgabedaten werden klassifiziert",
                        },
                        "correct": "B",
                        "explanation": "Ein Defekt, der bei einem Wert der Klasse entdeckt wird, sollte auch bei anderen Werten dieser Klasse nachweisbar sein.",
                    },
                    {
                        "prompt": "Was ist der Unterschied zwischen der 2-Wert- und der 3-Wert-Grenzwertanalyse?",
                        "options": {
                            "A": "Die 2-Wert-Analyse ist immer genauer",
                            "B": "Die 3-Wert-Analyse testet Grenzwert und zwei benachbarte Werte und ist genauer als die 2-Wert-Variante",
                            "C": "Es gibt keinen Unterschied zwischen beiden",
                            "D": "Die 2-Wert-Analyse wird nur bei Zustandsübergängen verwendet",
                        },
                        "correct": "B",
                        "explanation": "Die 3-Wert-Grenzwertanalyse testet zusätzlich einen weiteren benachbarten Wert und ist dadurch genauer.",
                    },
                    {
                        "prompt": "Ein Eingabefeld akzeptiert ganzzahlige Werte von 10 bis 50 (jeweils gültig). Welche vier Werte werden bei der 2-Wert-Grenzwertanalyse getestet?",
                        "options": {
                            "A": "9, 10, 50, 51",
                            "B": "10, 11, 49, 50",
                            "C": "0, 10, 50, 100",
                            "D": "9, 11, 49, 51",
                        },
                        "correct": "A",
                        "explanation": "Bei der 2-Wert-Grenzwertanalyse testet man jeweils den Grenzwert selbst und den direkten Nachbarn außerhalb: untere Grenze 9 (ungültig) und 10 (gültig), obere Grenze 50 (gültig) und 51 (ungültig).",
                    },
                    {
                        "prompt": "Ein Formularfeld für das Lebensalter unterteilt Eingaben in drei Bereiche: unter 18 (ungültig), 18 bis 65 (gültig), über 65 (ungültig). Wie viele Äquivalenzklassen ergeben sich daraus?",
                        "options": {
                            "A": "Zwei Klassen",
                            "B": "Vier Klassen",
                            "C": "Drei Klassen",
                            "D": "Eine einzige Klasse, da nur der gültige Bereich zählt",
                        },
                        "correct": "C",
                        "explanation": "Es ergeben sich drei Äquivalenzklassen: unter 18, 18-65 und über 65 - jeweils eine für das gültige und die zwei ungültigen Segmente.",
                    },
                    {
                        "prompt": "Was stellt eine Spalte in einer Entscheidungstabelle dar?",
                        "options": {
                            "A": "Eine einzelne Testperson",
                            "B": "Einen Zustand des Systems",
                            "C": "Eine eindeutige Kombination von Bedingungen und Aktionen (Entscheidungsregel)",
                            "D": "Eine Zeitspanne des Tests",
                        },
                        "correct": "C",
                        "explanation": "Jede Spalte in einer Entscheidungstabelle repräsentiert eine eindeutige Entscheidungsregel.",
                    },
                    {
                        "prompt": "Warum ist eine vollständige Abdeckung aller Übergänge beim Zustandsübergangstest besonders bei sicherheitskritischer Software wichtig?",
                        "options": {
                            "A": "Weil dort weniger Tests benötigt werden",
                            "B": "Weil ungültige Übergänge dort ignoriert werden können",
                            "C": "Weil sicherheitskritische Software keine Zustände hat",
                            "D": "Weil auch ungültige Übergänge zu kritischen Fehlern führen können und daher abgedeckt werden müssen",
                        },
                        "correct": "D",
                        "explanation": "Gerade bei sicherheitskritischer Software können auch 'ungültige' Übergänge fatale Folgen haben.",
                    },
                    {
                        "prompt": "Welche Kategorien von Daten können bei der Äquivalenzklassenbildung berücksichtigt werden?",
                        "options": {
                            "A": "Ausschließlich Eingabedaten",
                            "B": "Eingabedaten, Ausgabedaten, zeitabhängige Werte oder Schnittstellenparameter",
                            "C": "Ausschließlich Schnittstellenparameter",
                            "D": "Ausschließlich zeitabhängige Werte",
                        },
                        "correct": "B",
                        "explanation": "Klassen können Eingabedaten, Ausgabedaten, zeitabhängige Werte oder Schnittstellenparameter betreffen.",
                    },
                ],
            },
            {
                "number": "5.3",
                "title": "White-Box-Test",
                "questions": [
                    {
                        "prompt": "Was ist das Ziel des Anweisungstests?",
                        "options": {
                            "A": "Überprüfung aller bedingten Codepfade",
                            "B": "Sicherstellung der Testabdeckung aller Anweisungen im Code",
                            "C": "Bewertung der Benutzerfreundlichkeit",
                            "D": "Testen der externen Schnittstellen",
                        },
                        "correct": "B",
                        "explanation": "Der Anweisungstest zielt darauf ab, alle Anweisungen im Code mindestens einmal auszuführen.",
                    },
                    {
                        "prompt": "Ein Modul besteht aus 40 Anweisungen. Ein Testfall-Set führt 32 davon mindestens einmal aus. Wie hoch ist die Anweisungsabdeckung?",
                        "options": {
                            "A": "40 %",
                            "B": "60 %",
                            "C": "80 %",
                            "D": "32 %",
                        },
                        "correct": "C",
                        "explanation": "Anweisungsabdeckung = ausgeführte Anweisungen / alle Anweisungen × 100 = 32/40 × 100 = 80 %.",
                    },
                    {
                        "prompt": "Ein Codeabschnitt hat 12 Zweige. Um eine Zweigabdeckung von 100 % zu erreichen, wie viele davon müssen mindestens einmal durchlaufen werden?",
                        "options": {
                            "A": "6 Zweige",
                            "B": "10 Zweige",
                            "C": "Alle 12 Zweige",
                            "D": "Nur die Zweige mit Bedingungen, unbedingte Zweige zählen nicht",
                        },
                        "correct": "C",
                        "explanation": "100 % Zweigabdeckung bedeutet, dass jeder der 12 Zweige mindestens einmal durchlaufen werden muss - sowohl bedingte als auch unbedingte.",
                    },
                    {
                        "prompt": "Welchen Nachteil hat der Anweisungstest?",
                        "options": {
                            "A": "Er ist zu teuer in der Durchführung",
                            "B": "Er kann Fehler, die von Daten abhängen, wie z.B. Division durch Null, möglicherweise nicht erkennen",
                            "C": "Er benötigt keine Testwerkzeuge",
                            "D": "Er kann nur bei agilen Projekten angewendet werden",
                        },
                        "correct": "B",
                        "explanation": "Datenabhängige Fehler wie Division durch Null können beim reinen Anweisungstest übersehen werden.",
                    },
                    {
                        "prompt": "Was überprüft der Zweigtest im Gegensatz zum reinen Anweisungstest zusätzlich?",
                        "options": {
                            "A": "Nur unbedingte Codepfade",
                            "B": "Nur die Benutzeroberfläche",
                            "C": "Sowohl bedingungslose als auch bedingte Codepfade",
                            "D": "Ausschließlich die Performance",
                        },
                        "correct": "C",
                        "explanation": "Der Zweigtest deckt zusätzlich auch bedingte Codepfade ab, nicht nur die reine Ausführung jeder Zeile.",
                    },
                    {
                        "prompt": "In welchen Anwendungsbereichen sind White-Box-Testmethoden laut Präsentation besonders wichtig?",
                        "options": {
                            "A": "Nur bei einfachen internen Tools ohne besondere Anforderungen",
                            "B": "In kritischen Systemen mit hohen Anforderungen an Zuverlässigkeit, Integrität und Sicherheit",
                            "C": "Ausschließlich bei mobilen Apps",
                            "D": "Ausschließlich bei Webanwendungen",
                        },
                        "correct": "B",
                        "explanation": "Kritische Systeme mit hohen Anforderungen an Zuverlässigkeit, Integrität und Sicherheit sind der Hauptanwendungsbereich.",
                    },
                ],
            },
            {
                "number": "5.4",
                "title": "Erfahrungsbasierter Test",
                "questions": [
                    {
                        "prompt": "Wann kommen erfahrungsbasierte Testmethoden besonders zum Einsatz?",
                        "options": {
                            "A": "Nur wenn die Spezifikation sehr detailliert ist",
                            "B": "Wenn die Spezifikation unvollständig oder unklar ist und die Zeit für Tests begrenzt ist",
                            "C": "Ausschließlich bei sequenziellen Entwicklungsmodellen",
                            "D": "Nur nach Abschluss aller anderen Testtechniken",
                        },
                        "correct": "B",
                        "explanation": "Gerade bei unvollständiger Spezifikation und Zeitdruck kommen erfahrungsbasierte Methoden zum Tragen.",
                    },
                    {
                        "prompt": "Worauf basiert die intuitive Testfallermittlung (Fehlerraten)?",
                        "options": {
                            "A": "Auf zufällig generierten Testdaten",
                            "B": "Ausschließlich auf automatisierten Tools",
                            "C": "Auf dem Wissen über das bisherige Verhalten der Anwendung und typische Programmierfehler",
                            "D": "Auf der internen Struktur des Quellcodes",
                        },
                        "correct": "C",
                        "explanation": "Die intuitive Testfallermittlung stützt sich auf Wissen über bisheriges Anwendungsverhalten und typische Programmierfehler.",
                    },
                    {
                        "prompt": "Was zeichnet den explorativen Test aus?",
                        "options": {
                            "A": "Tests werden lange im Voraus vollständig dokumentiert",
                            "B": "Tests werden gleichzeitig entworfen, durchgeführt und bewertet, während der Tester die Anwendung erkundet",
                            "C": "Es werden nur automatisierte Skripte verwendet",
                            "D": "Es wird ausschließlich die interne Struktur des Codes betrachtet",
                        },
                        "correct": "B",
                        "explanation": "Beim explorativen Test verschmelzen Testentwurf, -durchführung und -bewertung in einem Schritt während der Erkundung.",
                    },
                    {
                        "prompt": "Worauf basieren Checklisten beim checklistenbasierten Test?",
                        "options": {
                            "A": "Ausschließlich auf gesetzlichen Vorschriften",
                            "B": "Ausschließlich auf der Projektdauer",
                            "C": "Auf Erfahrung, Wissen über Benutzererwartungen und Fehleranalysen",
                            "D": "Ausschließlich auf der Teamgröße",
                        },
                        "correct": "C",
                        "explanation": "Checklisten entstehen aus Erfahrung, Wissen über Benutzererwartungen und Fehleranalysen.",
                    },
                    {
                        "prompt": "Welchen Nutzen bieten erfahrungsbasierte Testmethoden laut Fazit?",
                        "options": {
                            "A": "Sie ersetzen alle anderen Testtechniken vollständig",
                            "B": "Sie ermöglichen eine schnelle Reaktion auf sich ändernde Bedingungen und effektive Fehlererkennung",
                            "C": "Sie eliminieren die Notwendigkeit von Testdokumentation komplett",
                            "D": "Sie funktionieren nur bei vollständig spezifizierten Anforderungen",
                        },
                        "correct": "B",
                        "explanation": "Schnelle Reaktionsfähigkeit und effektive Fehlererkennung sind die zentralen Vorteile.",
                    },
                ],
            },
            {
                "number": "5.5",
                "title": "Auf Zusammenarbeit basierende Testansätze",
                "questions": [
                    {
                        "prompt": "Wofür steht das dritte 'C' im '3 C'-Ansatz bei User Stories?",
                        "options": {
                            "A": "Confirmation (Akzeptanzkriterien)",
                            "B": "Coding (Programmierung der Story)",
                            "C": "Coverage (Testabdeckung der Story)",
                            "D": "Communication (allgemeine Teamkommunikation)",
                        },
                        "correct": "A",
                        "explanation": "Confirmation steht für die Akzeptanzkriterien, das dritte 'C' im 3-C-Ansatz (Card, Conversation, Confirmation).",
                    },
                    {
                        "prompt": "In welcher Reihenfolge werden bei ATDD Testfälle und Implementierung erstellt?",
                        "options": {
                            "A": "Die Reihenfolge spielt bei ATDD keine Rolle, beides läuft parallel",
                            "B": "Zuerst wird die User Story implementiert, danach werden passende Testfälle ergänzt",
                            "C": "Testfälle werden vor der Implementierung der User Story erstellt",
                            "D": "Testfälle entstehen automatisch aus dem fertigen Code",
                        },
                        "correct": "C",
                        "explanation": "Bei ATDD ('Test-First'-Ansatz) werden die Testfälle vor der Implementierung der User Story erstellt.",
                    },
                    {
                        "prompt": "Welches Format wird in der Präsentation genannt, um Abnahmekriterien präzise zu beschreiben?",
                        "options": {
                            "A": "UML-Aktivitätsdiagramme",
                            "B": "Given/When/Then-Szenarien oder Checklisten",
                            "C": "Reine Freitextbeschreibungen ohne festes Format",
                            "D": "Entscheidungstabellen mit Wahrheitswerten",
                        },
                        "correct": "B",
                        "explanation": "Given/When/Then-Szenarien oder Checklisten werden zur präzisen Beschreibung der Abnahmekriterien genutzt.",
                    },
                    {
                        "prompt": "Wer erstellt laut Präsentation die Testfälle im Rahmen von ATDD?",
                        "options": {
                            "A": "Ausschließlich der Product Owner allein",
                            "B": "Ein externes, unabhängiges Testteam nach Projektabschluss",
                            "C": "Teammitglieder mit unterschiedlichen Perspektiven",
                            "D": "Ein automatisiertes Tool ohne menschliches Zutun",
                        },
                        "correct": "C",
                        "explanation": "Teammitglieder mit unterschiedlichen Perspektiven erstellen gemeinsam die Testfälle, was eine umfassendere Abdeckung ermöglicht.",
                    },
                    {
                        "prompt": "Was ist laut Fazit ein zentraler Vorteil zusammenarbeitsbasierter Testansätze?",
                        "options": {
                            "A": "Sie verkürzen ausschließlich die Dauer der Entscheidungstabellentests",
                            "B": "Sie reduzieren den Bedarf an Abnahmekriterien auf ein Minimum",
                            "C": "Sie machen individuelle Reviews durch Gutachter überflüssig",
                            "D": "Sie minimieren das Risiko von Defekten durch frühzeitige Einbindung der Stakeholder",
                        },
                        "correct": "D",
                        "explanation": "Die frühzeitige Einbindung der Stakeholder minimiert das Risiko von Defekten.",
                    },
                ],
            },
        ]

        _insert_chapters(lo4, chapters_data)


def _get_or_create_lo(code, title):
    lo = LearningObjective.query.filter_by(code=code).first()
    if not lo:
        lo = LearningObjective(code=code, title=title)
        db.session.add(lo)
        db.session.commit()
    return lo


def seed_official_set_a(app):
    """Offizielle ISTQB CTFL v4.0 Sample Exam Paper - SET A (GTB edition), alle 40 Fragen."""
    with app.app_context():
        lo1 = _get_or_create_lo("LO1", "Grundlagen des Testens")
        lo2 = _get_or_create_lo("LO2", "Testen im Softwareentwicklungslebenszyklus")
        lo3 = _get_or_create_lo("LO3", "Statischer Test")
        lo4 = _get_or_create_lo("LO4", "Testanalyse und -entwurf")
        lo5 = _get_or_create_lo("LO5", "Management der Testaktivitäten")
        lo6 = _get_or_create_lo("LO6", "Werkzeugunterstützung für das Testen")

        def q(prompt, a, b, c, d, correct, explanation):
            return {
                "prompt": prompt,
                "options": {"A": a, "B": b, "C": c, "D": d},
                "correct": correct,
                "explanation": explanation,
            }

        # ---------- LO1: Fragen 1-8 ----------
        lo1_questions = [
            q(
                "Welche der folgenden Aussagen beschreibt ein erreichbares Testziel?",
                "Nachweis, dass das zu prüfende System keine Fehlerzustände mehr hat",
                "Nachweis, dass es nach der produktiven Inbetriebnahme keine Fehlerwirkungen geben wird",
                "Verringerung der Risikostufe des Testobjekts und Aufbau von Vertrauen in das Qualitätsniveau",
                "Überprüfung, dass alle Kombinationen von Eingabewerten getestet wurden",
                "C",
                "Man kann nie beweisen, dass ein System fehlerfrei ist (Grundsatz 1) oder dass alle Kombinationen getestet wurden (Grundsatz 2). Ein realistisches Testziel ist stattdessen die Risikoreduktion und der Vertrauensaufbau in die Qualität.",
            ),
            q(
                "Was ist der Hauptunterschied zwischen Testen und Debuggen?",
                "Testen ist der Prozess der Fehlersuche, während Debugging der Prozess der Fehlerbehebung ist.",
                "Beim Testen werden Anforderungen überprüft, während beim Debugging der Entwurf überprüft wird.",
                "Testen ist der Prozess des Ausführens von Software, während Debugging der Prozess der Analyse der Software ist.",
                "Testen ist der Prozess der Fehlervermeidung, während Debugging der Prozess der Fehlerbeseitigung ist.",
                "A",
                "Debugging umfasst das Auffinden, Analysieren und Beseitigen der Ursachen von Fehlern - meist nach einem Test, der den Fehler aufgedeckt hat. Testen sucht die Fehler, Debugging behebt sie.",
            ),
            q(
                "Sie sind Mitglied eines Teams, das ein neues System testet. Seit mehreren Iterationen wurden keine Änderungen an den bestehenden Regressionstestfällen vorgenommen und keine neuen Fehler durch Regressionstests aufgedeckt. Ihr Vorgesetzter ist zufrieden, Sie sind es nicht. Welcher Grundsatz des Testens erklärt Ihre Skepsis am besten?",
                "Alte Tests verlieren an Wirksamkeit",
                "Trugschluss: 'Keine Fehler' bedeutet ein brauchbares System",
                "Häufung von Fehlerzuständen",
                "Vollständiges Testen ist nicht möglich",
                "A",
                "Wenn dieselben Tests immer wieder unverändert wiederholt werden, finden sie irgendwann keine neuen Fehler mehr - genau das ist hier wahrscheinlich der Grund für das 'saubere' Ergebnis, nicht echte Fehlerfreiheit.",
            ),
            q(
                "Ihr Team implementiert die Zahlungsfunktionalität einer mobilen Essensbestellungs-App. Welche der folgenden Aktivitäten gehört zur Testanalyse?",
                "Die Aufwandsschätzung für den Test der Zahlungsdienst-Integration durchführen.",
                "Die Entscheidung treffen, ob getestet wird, inwieweit Zahlungen zwischen mehreren Nutzern aufgeteilt werden können.",
                "Mittels Grenzwertanalyse Testdaten für den zulässigen Mindestbetrag ableiten.",
                "Die Abweichung zwischen tatsächlichem und erwartetem Ergebnis nach Testausführung analysieren.",
                "B",
                "Die Definition von Testbedingungen (was soll geprüft werden?) ist Kernbestandteil der Testanalyse. Aufwandsschätzung gehört zur Planung, Grenzwertanalyse zum Testentwurf, Ergebnisabgleich zur Testdurchführung.",
            ),
            q(
                "Welche der folgenden Aussagen beschreibt AM BESTEN, wie durch Verfolgbarkeit zwischen Testbasis und Testmitteln ein Mehrwert erzielt wird?",
                "Wartungstests können basierend auf Änderungen der Anforderungen vollständig automatisiert werden.",
                "Es kann effizienter bestimmt werden, ob die angestrebte Überdeckung tatsächlich erreicht wurde.",
                "Die Testmanagementrolle kann feststellen, welche Tester die schwerwiegendsten Fehler gefunden haben.",
                "Codebereiche, die durch Seiteneffekte einer Änderung betroffen sein könnten, können gezielt per Regressionstest überprüft werden.",
                "B",
                "Sind Testfälle mit Anforderungen verknüpft, lässt sich bei einem neuen Testfall direkt feststellen, ob eine zuvor nicht abgedeckte Anforderung nun überdeckt wird - das ist der zentrale Nutzen der Verfolgbarkeit für die Überdeckungsbewertung.",
            ),
            q(
                "Welche der folgenden Aussagen vergleicht am BESTEN die verschiedenen Rollen beim Testen?",
                "Die Rolle des Testens führt Testfälle aus; die Testmanagementrolle plant, überwacht und meldet Abweichungen an alle Tester.",
                "Die Rolle des Testens führt Testanalyse und Testentwurf durch, erstellt und führt Testfälle aus; die Testmanagementrolle koordiniert Ressourcen und berichtet an Stakeholder.",
                "Die Rolle des Testens entscheidet über Automatisierung und priorisiert Testfälle; die Testmanagementrolle analysiert Risiken und setzt Prioritäten.",
                "Die Rolle des Testens führt Komponententests durch; die Testmanagementrolle führt System- und Abnahmetests durch.",
                "B",
                "Das beschreibt die Rollenteilung korrekt: Tester führen die operativen Aktivitäten (Analyse, Entwurf, Durchführung, Fehlermeldung) aus, während Testmanagement koordiniert und an Stakeholder berichtet.",
            ),
            q(
                "Welche der folgenden Aussagen erklärt am BESTEN einen Vorteil der Unabhängigkeit des Testens?",
                "Ein unabhängiges Testteam ermöglicht es der Projektleitung, ihm die alleinige Verantwortung für die Produktqualität zu übertragen.",
                "Ein externes Testteam lässt sich weniger leicht von Liefertermin-Druck des Managements beeinflussen.",
                "Ein unabhängiges Testteam kann getrennt von den Entwicklern arbeiten und die Kommunikation auf die Fehlerberichterstattung beschränken.",
                "Enthalten Spezifikationen Mehrdeutigkeiten, treffen Entwickler eigene Annahmen - ein unabhängiges Testteam kann diese Annahmen und Interpretationen kritisch hinterfragen.",
                "D",
                "Spezifikationen sind nie perfekt; Entwickler müssen oft Annahmen treffen. Ein unabhängiges Testteam bringt hier wertvollen Mehrwert, indem es diese Annahmen und Interpretationen unvoreingenommen hinterfragt.",
            ),
            q(
                "Wie zeigt sich der Whole-Team-Ansatz in der Interaktion zwischen Testern und Fachbereichsvertretern?",
                "Fachbereichsvertreter entscheiden gemeinsam mit der Projektleitung über Ansätze zur Testautomatisierung.",
                "Tester helfen Fachbereichsvertretern bei der Festlegung der Teststrategie.",
                "Die Beteiligung von Fachbereichsvertretern ist nicht Teil des Whole-Team-Ansatzes.",
                "Tester helfen Fachbereichsvertretern bei der Erstellung geeigneter Abnahmetests.",
                "D",
                "Tester arbeiten eng mit Fachbereichsvertretern zusammen, um die gewünschten Qualitätsniveaus zu erreichen - dazu gehört insbesondere die Unterstützung bei der Erstellung geeigneter Abnahmetests.",
            ),
        ]

        # ---------- LO2: Fragen 9-14 ----------
        lo2_questions = [
            q(
                "Welche der folgenden Aussagen beschreibt am BESTEN eine gute Praktik für das Testen, die für alle Softwareentwicklungslebenszyklen gilt?",
                "Testen sollte erst nach Abschluss der Entwicklung durchgeführt werden.",
                "Testen sollte unter Federführung der Entwicklung durchgeführt werden.",
                "Testen sollte frühzeitig im Entwicklungsprozess beginnen.",
                "Testen sollte in einer Entwicklungstestumgebung durchgeführt werden.",
                "C",
                "Frühes Testen erkennt Fehler früher und senkt die Kosten ihrer Behebung - das gilt unabhängig vom gewählten Entwicklungsmodell.",
            ),
            q(
                "Welche der folgenden Aussagen beschreibt AM BESTEN den Ansatz der abnahmetestgetriebenen Entwicklung (ATDD)?",
                "In der ATDD werden Abnahmekriterien typischerweise im Format 'GIVEN/WHEN/THEN' erstellt.",
                "Bei ATDD werden zunächst Testfälle entwickelt, dann wird die Software inkrementell gegen Testfälle und Abnahmekriterien implementiert.",
                "Bei ATDD werden Tests aus Abnahmekriterien als Teil des Systementwurfs abgeleitet.",
                "Bei ATDD basieren Tests auf dem gewünschten Verhalten der Software, was Teammitgliedern das Verständnis erleichtert.",
                "C",
                "ATDD leitet Tests direkt aus den im Systementwurf definierten Abnahmekriterien ab. Das Given/When/Then-Format gehört eher zu BDD, ebenso wie die Beschreibung über gewünschtes Verhalten.",
            ),
            q(
                "Welche der folgenden Aussagen ist KEIN Beispiel für den Shift-Left-Ansatz?",
                "Überprüfung der Benutzeranforderungen, bevor sie von den Stakeholdern formell akzeptiert werden.",
                "Erstellen von Komponententestfällen, bevor der zugehörige Code programmiert wird.",
                "Ausführen des Performanztests einer Komponente während des Komponententests.",
                "Durchführung nicht-funktionaler Tests, wenn möglich beginnend erst auf Ebene der Systemtests.",
                "D",
                "Shift-Left bedeutet, Aktivitäten so früh wie möglich zu verschieben. Nicht-funktionale Tests erst ab der Systemtest-Ebene zu beginnen, widerspricht diesem Prinzip - alle anderen Optionen sind echte Shift-Left-Beispiele.",
            ),
            q(
                "Welches Argument ist AM BESTEN geeignet, um den Vorgesetzten von regelmäßigen Retrospektiven am Ende jedes Release-Zyklus zu überzeugen?",
                "Retrospektiven sind heutzutage sehr beliebt und Kunden würden das schätzen.",
                "Retrospektiven sparen Geld, da Endnutzer-Vertreter kein unmittelbares Produktfeedback geben.",
                "Bei der Retrospektive festgestellte Prozessschwächen können direkt analysiert und als Aufgabenliste für die kontinuierliche Prozessverbesserung genutzt werden.",
                "Retrospektiven ermöglichen es dem Team, sich gegenseitig zu loben, was Arbeitsmoral und Produktivität steigert.",
                "C",
                "Regelmäßige Retrospektiven mit konkreten Folgeaktivitäten sind der entscheidende Mechanismus für kontinuierliche Prozessverbesserung - das ist das eigentliche, belastbare Argument.",
            ),
            q(
                "Welche Fehlerzustände (1-4) werden in welchen Teststufen (A-D) am ehesten gefunden? 1) Abweichung von Geschäftsanforderungen, 2) Fehler in der Kommunikation zwischen Komponenten, 3) Fehler in einer isolierten Komponente, 4) Fehler in einer nicht korrekt implementierten User-Story. A) Komponententest, B) Komponentenintegrationstest, C) Systemtest, D) Abnahmetest",
                "1D, 2B, 3A, 4C",
                "1D, 2B, 3C, 4A",
                "1B, 2A, 3D, 4C",
                "1C, 2A, 3B, 4D",
                "A",
                "Abnahmetests prüfen gegen Geschäftsanforderungen (1D), Komponentenintegrationstests decken Kommunikationsfehler zwischen Komponenten auf (2B), Komponententests finden Fehler in isolierten Komponenten (3A), und User-Storys sind Testbasis für Systemtests (4C).",
            ),
            q(
                "Die Teststrategie sieht vor, dass die Datenmigration zum Nachfolgesystem getestet werden muss, sobald ein System außer Betrieb genommen wird. Mit welcher Testaktivität wird diese Anforderung AM EHESTEN erfüllt?",
                "Wartungstest",
                "Regressionstest",
                "Komponententest",
                "Komponentenintegrationstest",
                "A",
                "Die Datenmigration im Zuge einer Systemablösung ist ein klassischer Auslöser für Wartungstests - diese decken genau solche Szenarien wie Migration und Außerbetriebnahme ab.",
            ),
        ]

        # ---------- LO3: Fragen 15-18 ----------
        lo3_questions = [
            q(
                "Welche der folgenden Optionen ist KEIN Vorteil des statischen Testens?",
                "Die Bewertung und Behebung von durch statische Analyse aufgedeckten Anomalien kann erheblichen Zeit- und Ressourcenaufwand erfordern.",
                "Die Behebung von bei statischen Tests gefundenen Fehlern ist meist deutlich kostengünstiger als bei dynamischen Tests.",
                "Das Finden von Programmierfehlern, die bei dynamischen Tests möglicherweise nicht gefunden werden.",
                "Das Aufdecken von Lücken und Unstimmigkeiten in den Anforderungen.",
                "A",
                "Der Aufwand zur Bewertung und Behebung aufgedeckter Anomalien ist tatsächlich eher ein möglicher Nachteil/Herausforderung des statischen Testens, kein Vorteil - vor allem bei sehr komplexen Testobjekten.",
            ),
            q(
                "Welcher der folgenden Punkte ist ein Vorteil von frühem und häufigem Feedback durch Stakeholder?",
                "Es verbessert den Testprozess für zukünftige Projekte.",
                "Es zwingt Kunden, ihre Anforderungen basierend auf abgestimmten Risiken zu priorisieren.",
                "Nur so lässt sich die Qualität der Prozessänderungen messen.",
                "Es hilft, Missverständnisse bei den Anforderungen zu vermeiden.",
                "D",
                "Frühes und häufiges Feedback deckt potenzielle Qualitätsprobleme wie missverstandene Anforderungen frühzeitig auf und ermöglicht so, sie rechtzeitig zu korrigieren.",
            ),
            q(
                "Ein Review in Ihrem Unternehmen hat folgende Eigenschaften: Hauptzweck ist Kommunikation/Schulung der Gutachter, die Sitzung wird vom Autor geleitet, es gibt individuelle Vorbereitung der Reviewer, ein Reviewbericht kann erstellt werden. Welche Review-Art wird am ehesten verwendet?",
                "Informelles Review",
                "Walkthrough",
                "Technisches Review",
                "Inspektion",
                "B",
                "Dass der Autor selbst die Sitzung leitet und der Hauptzweck Kommunikation/Schulung ist, sind typische Merkmale eines Walkthroughs - bei Inspektionen ist das nicht erlaubt, bei technischen Reviews nur ausnahmsweise.",
            ),
            q(
                "Welche der folgenden Aussagen ist KEIN Faktor, der zu einem erfolgreichen Review beiträgt?",
                "Die Teilnehmer sollten sich ausreichend Zeit für das Review nehmen.",
                "Eine Aufteilung großer Arbeitsprodukte in kleine Teile wird empfohlen, damit die Reviewer nicht die Konzentration verlieren.",
                "Die Festlegung klarer Ziele und messbarer Endekriterien für das Review.",
                "Die persönliche Mitwirkung des Managements in der Kommunikation der Befunde.",
                "D",
                "Das Management ist zwar für Budget und Unterstützung des Reviewprozesses verantwortlich, sollte sich aber NICHT persönlich in die Kommunikation der gefundenen Befunde einmischen - das würde die offene Atmosphäre des Reviews gefährden.",
            ),
        ]

        # ---------- LO4: Fragen 19-29 ----------
        lo4_questions = [
            q(
                "Welches der folgenden Punkte ist ein Merkmal erfahrungsbasierter Testverfahren?",
                "Testfälle werden auf Grundlage detaillierter Entwurfsinformationen erstellt.",
                "Zur Messung des Überdeckungsgrads wird die Anzahl der geprüften Schnittstellen verwendet.",
                "Die Verfahren beruhen in hohem Maße auf den Kenntnissen des Testers über Software und Geschäftsdomäne.",
                "Testfälle werden verwendet, um Abweichungen von den Anforderungen zu identifizieren.",
                "C",
                "Erfahrungsbasierte Verfahren nutzen das Wissen und die Erfahrung des Testers - z.B. über erwartete Nutzung, Umgebung und wahrscheinliche Fehlerquellen - zur Definition von Tests. Die anderen Optionen beschreiben White-Box- bzw. Black-Box-Merkmale.",
            ),
            q(
                "Eine unbeaufsichtigte Zapfsäule erlaubt Tankmengen von 0,1 bis 50,0 Gallonen über ein Ziffern-Tastenfeld. Welche minimale Menge an Eingabewerten deckt alle gültigen und ungültigen Äquivalenzklassen für die Kraftstoffmenge ab?",
                "0,0; 20,0; 60,0",
                "0,0; 0,1; 50,0",
                "0,0; 0,1; 50,0; 70,0",
                "-0,1; 0,0; 0,1; 49,9; 50,0; 50,1",
                "B",
                "Es gibt drei Äquivalenzklassen: 0,0 Gallonen (kein Verkauf, ungültig), 0,1-50,0 Gallonen (gültig) und über 50,0 (ungültig). Ein Wert pro Klasse genügt als Minimum: 0,0 / 0,1 / 50,0 deckt genau das ab - mehr Werte wären kein Minimum mehr.",
            ),
            q(
                "Ein E-Commerce-System verkauft Lebensmittel in Gramm/Kilogramm-Mengen von 0,5 bis 25,0 Einheiten (Genauigkeit 0,1). Welche Eingabewerte decken NUR die Grenzwerte mit der 2-Wert-Grenzwertanalyse für die Bestellmenge ab?",
                "0,3; 24,9; 25,2",
                "0,4; 0,5; 0,6; 24,9; 25,0; 25,1",
                "0,4; 0,5; 25,0; 25,1",
                "0,5; 0,6; 24,9; 25,0",
                "C",
                "Bei der 2-Wert-Grenzwertanalyse testet man je Grenze den Grenzwert selbst und den nächsten Nachbarn in der Nachbarklasse: untere Grenze 0,5 (gültig) und 0,4 (ungültig), obere Grenze 25,0 (gültig) und 25,1 (ungültig) - genau vier Werte.",
            ),
            q(
                "Eine Entscheidungstabelle regelt eine Mitarbeiterprämie basierend auf 'Beschäftigung > 1 Jahr?', 'Ziel vereinbart?' und 'Ziel erreicht?'. Welcher der folgenden Testfälle beschreibt eine in der Praxis gültige, durchführbare Situation und fehlt in der Tabelle?",
                "Bedingung1=J, Bedingung2=N, Bedingung3=J, Aktion=N",
                "Bedingung1=J, Bedingung2=J, Bedingung3=N, Aktion=J",
                "Bedingung1=N, Bedingung2=N, Bedingung3=J, Aktion=N",
                "Bedingung1=J, Bedingung2=J, Bedingung3=N, Aktion=N",
                "D",
                "Diese Kombination ist praktisch möglich (länger als 1 Jahr beschäftigt, Ziel vereinbart, aber nicht erreicht) und die korrekte Aktion ist 'keine Auszahlung' - das fehlt in der Tabelle. Die Optionen A und C sind unmöglich, da ein nicht vereinbartes Ziel auch nicht erreicht sein kann; Option B hat die falsche Aktion.",
            ),
            q(
                "Ein Zustandsübergangsdiagramm eines Fernsehers hat die Zustände 'TV Off', 'TV Standby' und 'TV Play'. Fünf Testfälle decken alle fünf gültigen Übergänge ab (S1→S2, S2→S1, S2→S3, S3→S2, S3→S1). Welche Aussage ist WAHR?",
                "Die Testfälle führen alle Übergänge aus, damit wird 100% Überdeckung aller Übergänge (inkl. ungültiger) erreicht.",
                "Die Testfälle führen alle gültigen Übergänge aus. Damit wird 100% 0-Switch-Überdeckung erreicht.",
                "Die Testfälle führen nur einige der gültigen Übergänge aus, die 0-Switch-Überdeckung liegt unter 100%.",
                "Testfall 2 ist für 100% 0-Switch-Überdeckung nicht erforderlich, da Zustand S1 bereits durch Testfall 5 überdeckt wurde.",
                "B",
                "0-Switch-Überdeckung bezieht sich auf alle gültigen Einzelübergänge, nicht auf ungültige Übergänge (die hier nicht getestet wurden) und nicht nur auf Zustände. Da alle 5 gültigen Übergänge abgedeckt sind, ist die 0-Switch-Überdeckung vollständig.",
            ),
            q(
                "Welche der folgenden Aussagen ist eine korrekte Beschreibung für Anweisungsüberdeckung?",
                "Eine Metrik zur Messung des prozentualen Anteils der ausgeführten Testfälle.",
                "Eine Metrik, die den prozentualen Anteil der durch Testfälle bereits ausgeführten Anweisungen im Code angibt.",
                "Eine Metrik zur Messung der Anzahl der ausgeführten Anweisungen, die keine Fehlerwirkung aufgedeckt haben.",
                "Eine Metrik, die eine wahr/falsch-Bestätigung liefert, ob alle Anweisungen abgedeckt sind.",
                "B",
                "Anweisungsüberdeckung = Anzahl ausgeführter Anweisungen / Gesamtzahl ausführbarer Anweisungen, als Prozentsatz. Sie bezieht sich auf Anweisungen im Code, nicht auf die Anzahl der Testfälle, und liefert einen Prozentwert, keine wahr/falsch-Aussage.",
            ),
            q(
                "Welche der folgenden Aussagen trifft NICHT auf White-Box-Test zu?",
                "White-Box-Test basiert auf der Analyse der internen Struktur einer Komponente oder eines Systems.",
                "White-Box-Überdeckungsmetriken können helfen, zusätzliche Tests zur Erhöhung der Codeüberdeckung zu identifizieren.",
                "White-Box-Testverfahren können ergänzend zu Black-Box-Testverfahren eingesetzt werden, um Vertrauen in den Code zu stärken.",
                "White-Box-Tests können helfen, nicht implementierte Anforderungen zu identifizieren.",
                "D",
                "Das ist gerade die Schwäche von White-Box-Verfahren: Da sie nur auf der internen Struktur basieren und nicht auf der Anforderungsspezifikation, können sie fehlende (nicht implementierte) Anforderungen nicht erkennen.",
            ),
            q(
                "Welche der folgenden Aussagen beschreibt AM BESTEN das Konzept der intuitiven Testfallermittlung (Error Guessing)?",
                "Sie nutzt Wissen über und Erfahrung mit in der Vergangenheit gefundenen Fehlerzuständen, -wirkungen und typischen Fehlhandlungen von Entwicklern.",
                "Sie nutzt die eigenen persönlichen Erfahrungen als Entwickler und die dabei selbst gemachten Fehlhandlungen.",
                "Man muss sich als Benutzer des Testobjekts vorstellen und Fehlerwirkungen erraten, die dieser bei der Interaktion machen könnte.",
                "Man muss die Entwicklungsaufgabe selbst schnell durchführen, um mögliche Fehlerzustände zu erkennen.",
                "A",
                "Intuitive Testfallermittlung basiert darauf, aus früheren Erfahrungen mit Fehlerzuständen und typischen Programmierfehlern abzuleiten, welche Fehler im aktuellen Testobjekt vorhanden sein könnten - unabhängig von eigener Entwicklertätigkeit.",
            ),
            q(
                "In Ihrem Projekt hat sich die Freigabe einer brandneuen Anwendung verzögert, die Testdurchführung beginnt spät, aber Sie haben detailliertes Fachwissen und gute analytische Fähigkeiten. Die Anforderungsspezifikation ist noch unvollständig, das Management möchte erste Testergebnisse sehen. Welches Testverfahren ist AM BESTEN geeignet?",
                "Checklistenbasiertes Testen",
                "Intuitive Testfallermittlung",
                "Exploratives Testen",
                "Anweisungstest",
                "C",
                "Exploratives Testen eignet sich besonders, wenn nur wenige Spezifikationen bekannt sind und/oder der Zeitplan eng ist - genau die hier beschriebene Situation. Eine passende Checkliste fehlt für ein neues Produkt, und Anweisungstest ist zu zeitaufwendig.",
            ),
            q(
                "Welche Aktivität beschreibt AM BESTEN, wie Abnahmekriterien für eine User-Story formuliert werden können?",
                "Durchführung von Retrospektiven zur Ermittlung der tatsächlichen Stakeholder-Bedürfnisse.",
                "Verwendung des Formats 'gegeben/wenn/dann' zur Beschreibung einer beispielhaften Testbedingung.",
                "Mündliche Kommunikation, um Missverständnisse der Abnahmekriterien zu vermeiden.",
                "Dokumentieren von Risiken zur User-Story in einem Testkonzept, um risikobasiertes Testen zu erleichtern.",
                "B",
                "Das Given/When/Then-Format ist die Standardmethode zur Dokumentation von Abnahmekriterien für User-Storys. Retrospektiven dienen der Prozessverbesserung, nicht der Kriteriendefinition; rein mündliche Kommunikation erlaubt keine physische Dokumentation.",
            ),
            q(
                "Ihr Team verfolgt ATDD und analysiert die User-Story 'Als registrierter Kunde möchte ich meine bisherigen Bestellungen einsehen können, um einen Überblick zu behalten.' Welcher der folgenden Testfälle ist für diese User-Story NICHT relevant?",
                "Kunde loggt sich ein und klickt auf 'Bestellhistorie anzeigen' - System zeigt alle früheren Bestellungen.",
                "Eingeloggter Kunde klickt auf eine Bestellung - System zeigt die gekauften Artikel mit Preis und Menge.",
                "Eingeloggter Kunde klickt auf 'Aufsteigend sortieren' - System zeigt die Historie sortiert an.",
                "Ein neu registrierter Kunde loggt sich ein und gibt eine erste Bestellung ein - System akzeptiert die Bestellung.",
                "D",
                "Ein neu registrierter Kunde hat per Definition noch keine Bestellhistorie - dieser Testfall betrifft zwar das Bestellsystem allgemein, aber nicht die konkrete User-Story zum Einsehen bestehender Bestellungen.",
            ),
        ]

        # ---------- LO5: Fragen 30-38 ----------
        lo5_questions = [
            q(
                "Wie schaffen Tester einen Mehrwert für die Iterations-Planung?",
                "Die Tester bestimmen die Priorität der zu entwickelnden User-Storys.",
                "Die Tester konzentrieren sich nur auf die Verfeinerung der funktionalen Aspekte.",
                "Die Tester beteiligen sich an der Risikoanalyse und bestimmen die Testbarkeit von User-Storys.",
                "Die Tester ermöglichen die Freigabe hochwertiger Software durch frühzeitigen Testentwurf während der Releaseplanung.",
                "C",
                "Die Beteiligung an der Risikoanalyse und die Bewertung der Testbarkeit von User-Storys ist eine der zentralen Arten, wie Tester Mehrwert für die Iterationsplanung schaffen. Priorisierung liegt beim Fachbereich, und Testentwurf während der Releaseplanung wäre widersprüchlich.",
            ),
            q(
                "Welche der folgenden Optionen sind Endekriterien für den Test eines Systems?",
                "Testumgebung ist einsatzbereit",
                "Anmeldung am Testobjekt durch den Tester ist möglich",
                "Erwartete Fehlerdichte ist erreicht und Fehlerzustände sind berichtet worden",
                "Anforderungen sind in das Format GIVEN/WHEN/THEN übersetzt worden",
                "C",
                "Erwartete Fehlerdichte und vollständige Fehlerberichterstattung sind klassische Abschlusskriterien. Die anderen drei Punkte betreffen die Bereitschaft/Verfügbarkeit von Ressourcen und Testbasis - das sind Eingangskriterien.",
            ),
            q(
                "Ihr Team nutzt die Drei-Punkt-Schätzung für eine risikoreiche Funktion: optimistisch 2 Personenstunden, wahrscheinlichst 11, pessimistisch 14. Wie lautet die endgültige Schätzung (Formel: (optimistisch + 4×wahrscheinlich + pessimistisch) / 6)?",
                "9 Personenstunden",
                "10 Personenstunden",
                "11 Personenstunden",
                "14 Personenstunden",
                "B",
                "(2 + 4×11 + 14) / 6 = (2 + 44 + 14) / 6 = 60 / 6 = 10 Personenstunden.",
            ),
            q(
                "Testfälle mit Prioritäten (kleinere Zahl = höhere Priorität) und Abhängigkeiten: TF001 (Prio 3, keine Abhängigkeit), TF002 (Prio 2, keine Abhängigkeit), TF003 (Prio 1, abhängig von TF001), TF004 (Prio 2, abhängig von TF002), TF005 (Prio 3, abhängig von TF002). Welcher Testfall soll als DRITTER ausgeführt werden?",
                "TF003",
                "TF005",
                "TF002",
                "TF001",
                "A",
                "Reihenfolge unter Berücksichtigung der Abhängigkeiten: TF001 zuerst (Voraussetzung für TF003), dann TF002 (Voraussetzung für TF004/TF005), danach TF003 mit höchster Priorität (1) - also als dritter Testfall.",
            ),
            q(
                "Testarten (1-4) und Testquadranten (A-D): 1) Gebrauchstauglichkeitstest, 2) Komponententest, 3) Funktionaler Test, 4) Zuverlässigkeitstest. A) Q1 Technologie/Team, B) Q2 Geschäftlich/Team, C) Q3 Geschäftlich/Produktkritik, D) Q4 Technologie/Produktkritik. Wie werden sie zugeordnet?",
                "1C, 2A, 3B, 4D",
                "1D, 2A, 3C, 4B",
                "1C, 2B, 3D, 4A",
                "1D, 2B, 3C, 4A",
                "A",
                "Gebrauchstauglichkeitstest gehört zu Q3 (geschäftlich, Produktkritik), Komponententest zu Q1 (technisch, Team-Unterstützung), Funktionaler Test zu Q2 (geschäftlich, Team-Unterstützung), Zuverlässigkeitstest zu Q4 (technisch, Produktkritik).",
            ),
            q(
                "Risiko 'Zu lange Antwortzeit bei Suchergebnissen' (Wahrscheinlichkeit mittel, Schaden hoch). Reaktion: unabhängiges Team führt Performanztest während Systemtests durch, Endnutzer-Stichprobe führt Alpha-/Beta-Tests vor Freigabe durch. Welche Art von Maßnahme wurde vorgeschlagen?",
                "Risikoakzeptanz",
                "Notfallplan",
                "Risikominderung",
                "Risikotransfer",
                "C",
                "Die vorgeschlagenen zusätzlichen Testaktivitäten (Performanztest, Alpha-/Beta-Tests) zielen darauf ab, das Risiko aktiv zu verringern - das ist klassische Risikominderung, nicht Akzeptanz, Notfallplanung oder Übertragung.",
            ),
            q(
                "Welche der folgenden Aussagen zu Zweck und Inhalt von Testberichten ist zutreffend?",
                "Testabschlussberichte werden in regelmäßigen Abständen erstellt, um Stakeholder über den Fortschritt zu informieren.",
                "Ein Testfortschrittsbericht beinhaltet u.a. die Bewertung der Produktqualität sowie Abweichungen vom Zeitplan.",
                "Ein Testabschlussbericht wird erstellt, wenn eine Teststufe abgeschlossen wurde, und baut auf Testfortschrittsberichten und zusätzlichen Daten auf.",
                "Testfortschrittsberichte werden während des Testabschlusses erstellt, um die Erfüllung der Endekriterien zu belegen.",
                "C",
                "Testabschlussberichte entstehen zu bestimmten Meilensteinen (z.B. Abschluss einer Teststufe, eines Projekts) und fassen Testfortschrittsberichte sowie weitere Daten zusammen. Regelmäßige Fortschrittsberichte sind hingegen für die laufende Information gedacht.",
            ),
            q(
                "Sie müssen ein automatisiertes Testskript aktualisieren, um es an eine neue Anforderung anzupassen. Welcher Prozess sorgt dafür, dass eine neue Version des Testskripts in der Versionsverwaltung erstellt wird?",
                "Management der Verfolgbarkeit",
                "Wartungstest",
                "Konfigurationsmanagement",
                "Anforderungsmanagement",
                "C",
                "Konfigurationsmanagement umfasst die Versionsverwaltung aller Testelemente, einschließlich Testskripte - genau das sorgt dafür, dass Änderungen als neue Version erfasst werden.",
            ),
            q(
                "Ein Fehlerbericht beschreibt, dass die Anwendung nach bestimmter Eingabe abstürzt, inklusive Testfall-Referenz, Priorität und Status. Die Entwickler können den Fehler nicht reproduzieren. Welche wichtigen Informationen fehlen im Bericht?",
                "Erwartetes Ergebnis und tatsächliches Ergebnis",
                "Referenzen und Fehlerstatus",
                "Testumgebung und Testobjekt (inkl. Version)",
                "Priorität und Schweregrad",
                "C",
                "Ohne Angabe von Testumgebung und der genauen Version des Testobjekts können Entwickler den Fehler nicht zuverlässig reproduzieren - das ist die entscheidende fehlende Information hier.",
            ),
        ]

        # ---------- LO6: Fragen 39-40 ----------
        lo6_questions = [
            q(
                "Welche Testaktivitäten unterstützt ein Werkzeug zur Erstellung von Testdaten?",
                "Testüberwachung und -steuerung",
                "Testanalyse und Testentwurf",
                "Testentwurf und -realisierung",
                "Testabschluss",
                "C",
                "Werkzeuge zur Testdatenerstellung unterstützen konkret die Testrealisierung (Erstellung von Testdaten als Teil der Testmittel) sowie den Testentwurf, in dem die Anforderungen an Testdaten definiert werden.",
            ),
            q(
                "Welcher Punkt ist ein mögliches Risiko bei der Testautomatisierung?",
                "Es kann zu unbekannten Nebenwirkungen im operativen Betrieb kommen",
                "Unrealistische Erwartungen hinsichtlich der Funktionalität eines Werkzeugs",
                "Testwerkzeuge sind möglicherweise nicht zuverlässig genug",
                "Es kann die verfügbare Zeit für manuelle Tests auf Dauer reduzieren",
                "B",
                "Ein typisches Risiko ist die Annahme, ein Automatisierungswerkzeug würde von sich aus alle Testprobleme lösen - diese unrealistische Erwartungshaltung ist ein zentraler, im Lehrplan genannter Risikopunkt.",
            ),
        ]

        chapter_map = [
            (lo1, "OFF-A-LO1", "Offizielle Prüfung SET A - LO1", lo1_questions),
            (lo2, "OFF-A-LO2", "Offizielle Prüfung SET A - LO2", lo2_questions),
            (lo3, "OFF-A-LO3", "Offizielle Prüfung SET A - LO3", lo3_questions),
            (lo4, "OFF-A-LO4", "Offizielle Prüfung SET A - LO4", lo4_questions),
            (lo5, "OFF-A-LO5", "Offizielle Prüfung SET A - LO5", lo5_questions),
            (lo6, "OFF-A-LO6", "Offizielle Prüfung SET A - LO6", lo6_questions),
        ]

        for lo, number, title, questions in chapter_map:
            existing = Chapter.query.filter_by(number=number).first()
            if existing:
                continue

            chapter = Chapter(lo_id=lo.id, number=number, title=title)
            db.session.add(chapter)
            db.session.flush()

            for qd in questions:
                question = Question(
                    chapter_id=chapter.id,
                    prompt=qd["prompt"],
                    option_a=qd["options"]["A"],
                    option_b=qd["options"]["B"],
                    option_c=qd["options"]["C"],
                    option_d=qd["options"]["D"],
                    correct_option=qd["correct"],
                    explanation=qd["explanation"],
                    source="official_mock",
                )
                db.session.add(question)

        db.session.commit()


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
    seed_lo4(app)
    seed_lo2(app)
    seed_official_set_a(app)
    print("Alle Lernziele inkl. offizieller Prüfung SET A erfolgreich eingespielt.")