from models import db, LearningObjective, Chapter, Question


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


def seed_official_set_b(app):
    """Offizielle ISTQB CTFL v4.0 Sample Exam Paper - SET B (GTB edition), alle 40 Fragen."""
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
                "Welche der folgenden Aussagen beschreibt am besten, warum Testen im Softwareentwicklungslebenszyklus notwendig ist?",
                "Dynamisches Testen ist die einzige Möglichkeit, die Qualität eines Testobjekts zu bewerten.",
                "Das Testen stellt sicher, dass die Benutzer die Bedürfnisse der Entwickler verstehen und nachvollziehen können.",
                "Testen wird ausschließlich durchgeführt, um regulatorische Standards zu erfüllen.",
                "Testen hilft, Fehlerzustände aufzudecken und damit die Qualität des Testobjekts zu verbessern.",
                "D",
                "Testen deckt Fehlerzustände auf, die anschließend durch Debugging behoben werden können, was die Qualität des Testobjekts insgesamt erhöht. Dynamisches Testen ist nur eines von mehreren Mitteln (neben Reviews, Inspektionen), nicht das einzige.",
            ),
            q(
                "Welche der folgenden Aussagen ist zutreffend?",
                "Qualitätssicherung ist ein korrektiver Ansatz",
                "Testen ist eine Form der Qualitätssteuerung",
                "Testen ist ein Synonym für Qualitätssteuerung",
                "Qualitätssteuerung ist ein präventiver Ansatz",
                "B",
                "Testen ist eine der wichtigsten Formen der Qualitätssteuerung, aber nicht das einzige Mittel (auch formale Methoden wie Modellprüfung gehören dazu). Qualitätssicherung ist ein präventiver, Qualitätssteuerung ein korrigierender Ansatz - nicht umgekehrt.",
            ),
            q(
                "Ein Tester hat über 5 Jahre Software auf mobilen Geräten getestet, dabei über lange Zeit weder bestehende Testfälle verändert noch neue erstellt. Bei neueren Plattform-Versionen wurden vermehrt Fehlerwirkungen von Nutzern gemeldet. Welchen Grundsatz des Testens hat der Tester nicht beachtet?",
                "Testen ist abhängig vom Umfeld",
                "Vollständiges Testen ist nicht möglich",
                "Tests nutzen sich ab",
                "Häufung von Fehlerzuständen",
                "C",
                "Unveränderte Tests werden mit der Zeit zunehmend ineffektiv beim Auffinden neuer Fehler ('Tests nutzen sich ab'). Um neue Fehlerzustände zu finden, hätten Testfälle und Testdaten regelmäßig angepasst und erweitert werden müssen.",
            ),
            q(
                "Eine Testcharta legt Sitzungsdauer (1h), zu erforschenden Bereich (Registrierungsseite), Vorgehen (verschiedene fehlerhafte Eingabesätze) und zu entdeckende Fehler fest. In welcher Testaktivität wird dieses Testmittel erstellt?",
                "Testplanung",
                "Testüberwachung und -steuerung",
                "Testanalyse",
                "Testentwurf",
                "D",
                "Eine Testcharta ist eine Form des Testentwurfs speziell für exploratives Testen - sie legt fest, was, wie und wonach gesucht werden soll. Sie ist kein Testkonzept (Planung), kein Statusbericht (Überwachung) und keine reine Liste von Testbedingungen (Analyse).",
            ),
            q(
                "Welcher der folgenden Aspekte beeinflusst AM EHESTEN die Durchführung von Tests für ein bestimmtes Testobjekt?",
                "Die durchschnittliche Erfahrung des Marketingteams des Unternehmens",
                "Das Wissen der Benutzer, dass ein neues System für sie entwickelt wird",
                "Die Anzahl der Jahre an Testerfahrung der Mitglieder des Testteams",
                "Die Organisationsstruktur der Benutzer der zu entwickelnden Anwendung",
                "C",
                "Die Testerfahrung des Teams bestimmt direkt die Fähigkeiten und das Wissen (z.B. über Tools und Fehlertypen), die beim eigentlichen Testen angewendet werden. Marketing-Erfahrung, Nutzerwissen über das Projekt und die Nutzer-Organisationsstruktur haben höchstens indirekten Einfluss über Anforderungen, nicht auf die Testdurchführung selbst.",
            ),
            q(
                "Testaktivitäten: 1) Auswahl von Regressionstests, 2) Bewertung der Vollständigkeit der Testdurchführung, 3) Identifizieren, welche User-Storys offene Fehlerberichte haben, 4) Bewertung, ob Qualität/Anzahl der Tests zum Produktrisiko passt. Wie unterstützt Verfolgbarkeit (A-D) jeweils? A) Verständlichkeit von Statusberichten verbessern, B) Testaktivitäten nachvollziehbar machen, C) Informationen zur Prozessqualität liefern, D) Auswirkungen von Änderungen analysieren",
                "1D, 2B, 3C, 4A",
                "1B, 2D, 3A, 4C",
                "1D, 2C, 3A, 4B",
                "1D, 2B, 3A, 4C",
                "D",
                "Regressionstestauswahl basiert auf Änderungsanalyse (1D), Bewertung der Durchführungsvollständigkeit macht Tests nachvollziehbar (2B), das Identifizieren offener Fehlerberichte pro Story verbessert die Verständlichkeit von Statusberichten (3A), und die Risiko-Test-Abstimmung liefert Informationen zur Prozessqualität (4C).",
            ),
            q(
                "Ein erfahrener Hubschrauberpilot wurde als Tester für ein Hubschrauber-Steuerungssystem eingestellt. Welche positive Auswirkung werden seine allgemeinen Kompetenzen AM EHESTEN auf das Testteam haben?",
                "Die Anwendung von 3-Wert-Grenzwertanalyse für gründlicheren Testentwurf im Systemtest.",
                "Inkonsistenzen und Ungenauigkeiten in den fachlichen Anforderungen werden effektiv aufgedeckt.",
                "Einsatz eines Werkzeugs zur Automatisierung von Zustandsübergangstests.",
                "Testergebnisse werden konstruktiver und defensiver an die Entwickler kommuniziert.",
                "B",
                "Das Fachwissen des Piloten (Anwendungsdomäne) hilft besonders dabei, Inkonsistenzen in den fachlichen Anforderungen effektiv zu erkennen. Testverfahren-Wissen, Automatisierungs-Know-how oder Kommunikationsfähigkeit lassen sich aus seiner Pilotenerfahrung nicht automatisch ableiten.",
            ),
            q(
                "Welche der folgenden Aussagen beschreibt einen Vorteil des Whole-Team-Ansatzes?",
                "Er ermöglicht es den Teammitgliedern, jederzeit jede Rolle zu übernehmen.",
                "Es wird nur ein Team benötigt, um das gesamte Entwicklungsprojekt zu unterstützen.",
                "Tester können isoliert arbeiten, ohne Entwickler mit testspezifischen Informationen abzulenken.",
                "Oft ergeben sich Synergien, von denen das gesamte Team und das Projekt profitieren.",
                "D",
                "Der Whole-Team-Ansatz nutzt die unterschiedlichen Fähigkeiten aller Teammitglieder optimal aus und fördert dadurch Teamdynamik, Kommunikation und Synergien, von denen das gesamte Projekt profitiert. Isoliertes Arbeiten der Tester widerspricht dem Grundgedanken.",
            ),
        ]

        # ---------- LO2: Fragen 9-14 ----------
        lo2_questions = [
            q(
                "Welche der folgenden Aussagen über die Wahl des Softwareentwicklungslebenszyklus und dessen Beziehung zum Testen ist KORREKT?",
                "In der agilen Softwareentwicklung ersetzt die Automatisierung von Systemtests die Notwendigkeit von Regressionstests.",
                "Wenn ein sequentielles Entwicklungsmodell verwendet wird, wird dynamisches Testen typischerweise in einer späteren Phase des Lebenszyklus durchgeführt.",
                "Wenn ein iteratives Entwicklungsmodell verwendet wird, werden Komponententests typischerweise manuell von Entwicklern durchgeführt.",
                "Wenn ein inkrementelles Entwicklungsmodell verwendet wird, werden statische Tests in frühen und dynamische Tests in späteren Inkrementen durchgeführt.",
                "B",
                "Bei sequenziellen Modellen steht in frühen Phasen noch kein ausführbarer Code zur Verfügung, weshalb dort statische Tests dominieren und dynamisches Testen erst später erfolgt. Bei agilen/iterativen/inkrementellen Modellen laufen statische und dynamische Tests dagegen in jeder Iteration bzw. jedem Inkrement parallel, nicht strikt getrennt nach Zeitpunkt.",
            ),
            q(
                "Welche der folgenden Optionen ist eine gute Testpraktik, unabhängig vom gewählten Modell des Softwareentwicklungslebenszyklus?",
                "Tester sollten die Arbeitsergebnisse einer Entwicklungsphase in der nächsten Entwicklungsphase überprüfen.",
                "Tester sollten mit der Überprüfung der Arbeitsergebnisse einer Entwicklungsaktivität beginnen, sobald Entwürfe verfügbar sind.",
                "Tester sollten Arbeitsergebnisse nur im Rahmen der Testanalyse und des Testentwurfs überprüfen.",
                "Tester sollten Arbeitsergebnisse prüfen, sobald sie zur Nutzung freigegeben sind.",
                "B",
                "Frühes Prüfen von Arbeitsergebnissen, sobald Entwürfe verfügbar sind, entspricht dem Shift-Left-Prinzip und verhindert Folgefehler in nachgelagerten Aktivitäten - das gilt unabhängig vom SDLC-Modell. Warten bis zur nächsten Phase oder bis zur Freigabe wäre bereits zu spät.",
            ),
            q(
                "Welches der folgenden Beispiele ist ein Test-First-Ansatz für die Entwicklung?",
                "Testgetriebene Entwicklung",
                "Überdeckungsgetriebene Entwicklung",
                "Qualitätsgetriebene Entwicklung",
                "Feature-getriebene Entwicklung",
                "A",
                "Testgetriebene Entwicklung (TDD) ist das klassische Beispiel eines Test-First-Ansatzes. Die anderen Begriffe beziehen sich entweder auf Überdeckungsmessung, allgemeine Qualitätsziele oder eine agile Feature-Liefermethodik - keiner davon ist ein Test-First-Ansatz.",
            ),
            q(
                "Welche der folgenden Aussagen trifft auf DevOps zu?",
                "Kontinuierliche Integration ermöglicht es Entwicklern, Code schnell und ohne Komponententests auszuliefern.",
                "Um Systeme schneller aktualisieren und freigeben zu können, nutzt die DevOps-Lieferkette Automatisierung, um zeitaufwändige manuelle Regressionstests zu reduzieren.",
                "Um die Kluft zwischen Entwicklung und Betrieb zu verringern, priorisiert das Testen mit einem Shift-Right-Ansatz den Abnahmetest parallel zur kontinuierlichen Auslieferung.",
                "Um größere Synergie zwischen Testern, Entwicklern und Betrieb zu schaffen, werden Tests vollständig automatisiert, sodass keine manuellen Tests mehr nötig sind.",
                "B",
                "DevOps nutzt Automatisierung in der Auslieferungskette, um den Bedarf an sich wiederholenden manuellen Regressionstests zu reduzieren und das Regressionsrisiko zu minimieren. Komponententests bleiben trotz CI erforderlich, DevOps setzt eher auf Shift-Left statt Shift-Right, und manuelle Tests bleiben - besonders aus Nutzerperspektive - weiterhin nötig.",
            ),
            q(
                "Welche der folgenden Maßnahmen wird im Rahmen von Systemtests AM EHESTEN durchgeführt?",
                "End-to-End-Tests der IT-Sicherheit eines Kreditmanagementsystems durch ein unabhängiges Testteam.",
                "Test des Zusammenwirkens eines Geldwechselsystems mit dem System einer externen Bank.",
                "Beta-Test einer Lernplattform durch die Trainer eines Schulungsanbieters.",
                "Test der Interaktion zwischen Benutzeroberfläche und Datenbank eines Personalverwaltungssystems.",
                "A",
                "Systemtests prüfen das Verhalten und die Fähigkeiten des gesamten Systems inklusive nicht-funktionaler Aspekte wie IT-Sicherheit, oft durch ein unabhängiges Team. Option B beschreibt einen Systemintegrationstest, C einen Abnahmetest (Beta-Test), D einen Komponentenintegrationstest.",
            ),
            q(
                "Welche der folgenden Entscheidungen sollte KEIN Auslöser für Wartungstests sein?",
                "Die Entscheidung, die Wartbarkeit der Software zu testen",
                "Die Entscheidung, das System nach der Migration auf eine neue Betriebsplattform zu testen",
                "Die Entscheidung, die Wiederherstellbarkeit archivierter Daten nach Außerbetriebnahme zu testen",
                "Die Entscheidung zu testen, nachdem ein Hotfix auf die Produktivversion aufgespielt wurde",
                "A",
                "Wartbarkeit ist ein Qualitätsmerkmal, das nicht von der Codeausführung abhängt und daher kein typischer Auslöser für dynamische Wartungstests ist. Plattformmigration, Datenarchivierung/-wiederherstellung und Hotfixes sind dagegen klassische Auslöser für Wartungstests.",
            ),
        ]

        # ---------- LO3: Fragen 15-18 ----------
        lo3_questions = [
            q(
                "Welche der folgenden Aussagen beschreibt am BESTEN den Einsatz von statischem Test?",
                "Statisches Testen kann Fehlerzustände aufdecken, die durch dynamisches Testen nicht gefunden werden können.",
                "Fehlerzustände im Code können durch dynamische Tests effizienter gefunden werden als durch statische Tests.",
                "Der statische Test kann erst in einer späten Phase des SDLC durchgeführt werden.",
                "Um den statischen Test so effizient wie möglich zu gestalten, sollten so wenig Stakeholder wie möglich involviert sein.",
                "A",
                "Es gibt Fehlerzustände, die nur durch statisches Testen entdeckt werden können - das ist einer seiner zentralen Vorteile. Statische Tests sind oft sogar effizienter als dynamische, können schon sehr früh im SDLC eingesetzt werden, und profitieren von der Einbindung vieler Stakeholder (bessere Kommunikation).",
            ),
            q(
                "Welche der folgenden Aussagen beschreibt einen Vorteil von frühem und häufigem Stakeholder-Feedback?",
                "Es ermöglicht dem Projektmanagement, weniger produktive Entwickler frühzeitig zu identifizieren.",
                "Es ermöglicht Projektmanagern, ihre Interaktionen mit Stakeholdern zu reduzieren.",
                "Es erleichtert die frühzeitige Kommunikation potenzieller Qualitätsprobleme.",
                "Endbenutzer verstehen besser, warum sich die Bereitstellung der Anwendung verzögert.",
                "C",
                "Frühzeitiges und häufiges Feedback erleichtert die frühe Kommunikation potenzieller Qualitätsprobleme und hilft, Missverständnisse bei Anforderungen zu vermeiden. Es geht dabei nicht um Personalbewertung oder Reduzierung von Stakeholder-Kontakt.",
            ),
            q(
                "Review-Aufgaben: 1) Qualitätsmerkmale und Endekriterien festlegen, 2) Arbeitsergebnis allen Beteiligten zugänglich machen, 3) Anomalien im Arbeitsergebnis identifizieren, 4) Anomalien analysieren und diskutieren. Aktivitäten: A) Individuelles Review, B) Reviewbeginn, C) Planung, D) Kommunikation und Analyse. Welche Zuordnung ist korrekt?",
                "1B, 2C, 3D, 4A",
                "1B, 2D, 3C, 4A",
                "1C, 2A, 3B, 4D",
                "1C, 2B, 3A, 4D",
                "D",
                "Festlegung von Qualitätsmerkmalen und Endekriterien gehört zur Planung (1C), Zugänglichmachung des Arbeitsergebnisses zum Reviewbeginn (2B), Identifikation von Anomalien zum individuellen Review (3A), und Diskussion/Analyse der Anomalien zur Kommunikations- und Analysephase (4D).",
            ),
            q(
                "Review-Rollen: 1) Protokollant, 2) Reviewleiter, 3) Moderator, 4) Manager. Verantwortlichkeiten: A) Sorgt für effektive Durchführung inkl. geschützter Umgebung, B) Zeichnet Entscheidungen und neue Anomalien auf, C) Entscheidet was geprüft wird und stellt Ressourcen bereit, D) Übernimmt Gesamtverantwortung, organisiert wann/wo. Welche Zuordnung ist korrekt?",
                "1A, 2B, 3D, 4C",
                "1A, 2C, 3B, 4D",
                "1B, 2D, 3A, 4C",
                "1B, 2D, 3C, 4A",
                "C",
                "Der Protokollant zeichnet Entscheidungen und Anomalien auf (1B), der Reviewleiter trägt die Gesamtverantwortung und organisiert das Review (2D), der Moderator sorgt für eine effektive, geschützte Sitzungsdurchführung (3A), und der Manager entscheidet über Prüfgegenstand und Ressourcen (4C).",
            ),
        ]

        # ---------- LO4: Fragen 19-29 ----------
        lo4_questions = [
            q(
                "Welche der folgenden Aussagen beschreibt KORREKT die Zuordnung von Verfahrensgrundlagen zu Entscheidungstabellen- und Zweigtests?",
                "Beim Entscheidungstabellentest werden Testfälle aus den Entscheidungsergebnissen im Code abgeleitet; beim Zweigtest aus der Kenntnis des Kontrollflusses.",
                "Beim Entscheidungstabellentest werden Testfälle aus der Spezifikation der Geschäftslogik abgeleitet; beim Zweigtest basieren sie auf der Antizipation potenzieller Fehler im Quellcode.",
                "Beim Entscheidungstabellentest werden Testfälle aus der Kenntnis des Kontrollflusses abgeleitet; beim Zweigtest aus der Spezifikation der Geschäftslogik.",
                "Beim Entscheidungstabellentest werden Testfälle unabhängig vom Zustand der Software abgeleitet; beim Zweigtest können Testfälle erst nach Entwurf/Implementierung des Codes erstellt werden.",
                "D",
                "Entscheidungstabellentest ist ein Black-Box-Verfahren (spezifikationsbasiert, implementierungsunabhängig), Zweigtest ein White-Box-Verfahren (strukturbasiert, kann erst nach Entwurf/Implementierung erstellt werden, da er die interne Codestruktur kennen muss).",
            ),
            q(
                "Eine Waschanlagenkarte startet bei 0 Wäschen. Jede zehnte Wäsche gibt 10% Rabatt, jede zwanzigste zusätzlich 40% (insgesamt 50%). Welche Eingaben (Anzahl Wäschen) erreichen die höchste Überdeckung der Äquivalenzklassen?",
                "19, 20, 30",
                "11, 12, 20",
                "1, 10, 50",
                "10, 29, 30, 31",
                "A",
                "19 deckt 'kein Rabatt', 20 deckt '50% Rabatt' und 30 deckt '10% Rabatt' ab - damit sind alle drei Äquivalenzklassen mit nur drei Werten abgedeckt. Die anderen Optionen decken jeweils nur zwei der drei Klassen ab.",
            ),
            q(
                "Ein Weinlager-Kontrollgerät meldet: 11≤T≤13 'optimal', T<11 'zu niedrig', T>13 'zu hoch' (T in ganzen °C). Mit 3-Wert-Grenzwertanalyse: Welche Testeingaben ergeben 100%ige Überdeckung?",
                "11, 12, 13",
                "9, 13, 15",
                "9, 10, 11, 12, 13, 14, 15",
                "10, 11, 12, 13, 14",
                "C",
                "Die Grenzen liegen bei 10/11 und 13/14. Bei der 3-Wert-Methode braucht man jeden Grenzwert plus je einen Nachbarn auf beiden Seiten: 9,10,11 (untere Grenze) und 12,13,14,15 (obere Grenze, da 13 auch Nachbar der unteren Grenze zur mittleren Klasse ist) - zusammen ergibt das genau die Werte 9 bis 15.",
            ),
            q(
                "Eine Entscheidungstabelle zur Arteriosklerose-Risikobewertung hat 5 Regeln (Spalten) basierend auf Cholesterin- und Blutdruckwerten. Fünf Testfälle wurden entworfen. TC1/TC2 decken Regel 4 ab, TC3/TC4 decken Regel 2 ab, TC5 deckt Regel 5 ab. Welche Überdeckung der Entscheidungstabelle wird erreicht?",
                "40%",
                "60%",
                "80%",
                "100%",
                "B",
                "Die fünf Testfälle decken zusammen nur 3 von 5 Regeln (Spalten) ab (Regel 4, Regel 2, Regel 5) - Regel 1 und Regel 3 bleiben ungetestet. 3/5 × 100% = 60% Überdeckung.",
            ),
            q(
                "Ein Zustandsübergangsdiagramm für ein Batterieladegerät hat die Zustände Warten, Erhaltungsladen, Laden (mit Unterzuständen Niedrig/Hoch) und Aus, mit 10 definierten gültigen Übergängen. Welcher Testfall enthält sowohl gültige als auch einen ungültigen Übergang: Start→Warten→Aus→Warten→Laden→Niedrig→Laden?",
                "Start→Warten→Aus→Warten→Erhaltungsladen→Warten",
                "Start→Warten→Erhaltungsladen→Laden→Hoch→Laden",
                "Start→Warten→Erhaltungsladen→Laden→Niedrig→Laden",
                "Start→Warten→Aus→Warten→Laden→Niedrig→Laden",
                "D",
                "Der Übergang Warten→Laden ist im Diagramm nicht als gültiger Übergang definiert - dieser Testfall enthält also neben mehreren gültigen Übergängen auch diesen einen ungültigen. Die anderen drei Testfälle durchlaufen ausschließlich gültige, im Diagramm definierte Übergänge.",
            ),
            q(
                "Zwei Testfälle T1 und T2 für denselben Code: T1 erreicht 40% Anweisungsüberdeckung, T2 erreicht 65%. Welche Aussage ist aufgrund dieser Informationen KORREKT?",
                "Die Testsuite aus T1 und T2 erreicht eine Anweisungsüberdeckung von 105%.",
                "Mindestens eine Anweisung wurde sowohl von T1 als auch von T2 ausgeführt.",
                "Mindestens 5% der Anweisungen im getesteten Code sind nicht ausführbar.",
                "Die Testsuite aus T1 und T2 erreicht eine Zweigüberdeckung von 100%.",
                "B",
                "Da Überdeckung nie über 100% liegen kann, müssen sich T1 (40%) und T2 (65%) in mindestens 5 Prozentpunkten überschneiden - also mindestens eine Anweisung von beiden ausgeführt worden sein. Über nicht-ausführbare Anweisungen oder Zweigüberdeckung sagt die Anweisungsüberdeckung nichts aus.",
            ),
            q(
                "Die Formel für Zweigüberdeckung lautet ZÜ = (X/Y) × 100%. Was bedeuten X und Y?",
                "X = Anzahl ausgeführter Entscheidungsergebnisse, Y = Gesamtzahl der Entscheidungsergebnisse im Code",
                "X = Anzahl durch Testfälle ausgeführter bedingter Zweige, Y = Gesamtzahl der Zweige im Code",
                "X = Anzahl der von Testfällen ausgeführten Zweige, Y = Gesamtzahl der Zweige im Code",
                "X = Anzahl ausgeführter bedingter Zweige, Y = Gesamtzahl der Entscheidungsergebnisse im Code",
                "C",
                "Zweigüberdeckung zählt ALLE Zweige (sowohl bedingte als auch unbedingte/geradlinige), nicht nur bedingte Entscheidungsergebnisse. X = ausgeführte Zweige, Y = alle Zweige im Code, als Prozentsatz ausgedrückt.",
            ),
            q(
                "Welche der folgenden Aussagen liefert die BESTE Begründung für den effektiven Einsatz explorativer Tests?",
                "Die bestehende Teststrategie fordert, dass Tester Black-Box-Testverfahren verwenden.",
                "Die Spezifikation ist in einer formalen, werkzeugverarbeitbaren Sprache geschrieben.",
                "Die Tester sind Mitglieder eines agilen Teams und verfügen über gute Programmierkenntnisse.",
                "Die Tester haben Erfahrung in der Anwendungsdomäne und gute analytische Fähigkeiten.",
                "D",
                "Exploratives Testen ist besonders effektiv, wenn Tester über Domänenerfahrung sowie hohe analytische Fähigkeiten, Neugier und Kreativität verfügen. Formale, werkzeugverarbeitbare Spezifikationen sprechen eher für automatisierte/statische Ansätze, und Programmierkenntnisse allein sind kein Grund für explorative Tests.",
            ),
            q(
                "Welches ist das BESTE Beispiel für eine Testbedingung bei checklistenbasierten Tests?",
                "'Der Entwickler hat bei der Implementierung eine Fehlhandlung gemacht.'",
                "'Die erreichte Anweisungsüberdeckung ist größer als 85%'",
                "'Das Programm erfüllt die funktionalen und nicht-funktionalen Anforderungen korrekt'",
                "'Die Fehlermeldungen des Systems sind für die Benutzer verständlich.'",
                "D",
                "Diese Bedingung ist konkret, direkt prüfbar und basiert auf Tester-Erfahrung darüber, was für Benutzer wichtig ist - genau das macht eine gute Checklisten-Testbedingung aus. Die anderen Optionen sind entweder zu vage, ein Endekriterium statt einer Testbedingung, oder eine allgemeine Vermutung ohne konkreten Prüfpunkt.",
            ),
            q(
                "Ein Abnahmekriterium lautet: 'Angenommen der Benutzer ist eingeloggt und auf der Startseite. Wenn er auf Artikel hinzufügen klickt, dann erscheint das Formular Artikel anlegen, und er kann Namen und Preis eingeben.' In welchem Format ist dieses Kriterium geschrieben?",
                "Regelorientiert",
                "Szenario-orientiert",
                "Produktorientiert",
                "Prozessorientiert",
                "B",
                "Das Gegeben/Wenn/Dann-Format beschreibt ein konkretes zu verifizierendes Szenario und ist damit szenario-orientiert. 'Produktorientiert' und 'prozessorientiert' sind keine im Lehrplan definierten Formate für Abnahmekriterien.",
            ),
            q(
                "User-Story: 'Als Trainer möchte ich die Spielberechtigungsliste im DFBNET für einen Spieltag abrufen, um den Kader zusammenzustellen.' Welcher Testfall eignet sich am BESTEN für ATDD dieser Story?",
                "Login als Trainer; wähle die nächsten Spieltage aus; lade die Spielberechtigungslisten.",
                "GEGEBEN: Als Trainer angemeldet UND nächster Spieltag ausgewählt. WENN 'Spielberechtigungsliste laden' gewählt wird, DANN wird die Liste der spielberechtigten Spieler angezeigt.",
                "Login als Mannschaftsverantwortlicher; wähle den nächsten Spieltag; lade Liste; entferne nicht berechtigte Spieler.",
                "GEGEBEN: Spieltage ausgewählt. WENN ein Spieltag gewählt UND die Liste geladen wird, DANN werden alle berechtigten Spieler angezeigt.",
                "B",
                "Dieser Testfall entspricht exakt der Story: Login als Trainer, ein Spieltag, Laden und Anzeigen der Berechtigungsliste. Option A lädt fälschlich mehrere Spieltage, Option C nennt die falsche Rolle (Mannschaftsverantwortlicher statt Trainer), und Option D berücksichtigt nicht die Trainer-Anmeldung, die die Story explizit fordert.",
            ),
        ]

        # ---------- LO5: Fragen 30-38 ----------
        lo5_questions = [
            q(
                "Ein Team nutzt eine CI/CD-Pipeline mit Shift-Left-Ansatz: (1) Code entwickeln/bereitstellen, (2) Code an Versionskontrolle übergeben und in 'Test'-Branch integrieren, (3) automatisierten Komponententest durchführen. Welches Kriterium eignet sich AM BESTEN als Eingangskriterium für Schritt (2)?",
                "Die statische Analyse meldet für den übermittelten Code keine Fehler und keine Warnungen mit hohem Schweregrad.",
                "Die Versionskontrolle meldet keine Konflikte beim Kompilieren und Integrieren in den 'Test'-Branch.",
                "Die Komponententests sind kompiliert und lauffähig für den 'Test'-Branch verfügbar.",
                "Die Anweisungsüberdeckung des Komponententests beträgt mindestens 80%.",
                "A",
                "Als Eingangskriterium VOR der Integration ist eine saubere statische Analyse sinnvoll und messbar, vergleichbar einem Smoke-Test. Konfliktmeldungen der Versionskontrolle können erst NACH der Integration geprüft werden, kompilierte Komponententests betreffen eher Schritt 3, und die Überdeckung ist eher ein Endekriterium für Schritt 3.",
            ),
            q(
                "Bei einer Schätzung basierend auf Verhältniszahlen aus 4 historischen Projekten beträgt der durchschnittliche Entwicklungsaufwand 900.000€ und der durchschnittliche Testaufwand 90.000€ (Verhältnis 1:10). Der geschätzte Entwicklungsaufwand für ein neues Projekt beträgt 800.000€. Wie hoch ist der geschätzte Testaufwand?",
                "40.000€",
                "80.000€",
                "81.250€",
                "82.500€",
                "B",
                "Das Verhältnis Testaufwand:Entwicklungsaufwand beträgt 1:10 (10%). 10% von 800.000€ = 80.000€.",
            ),
            q(
                "Testfälle mit Prioritäten (1=dringlichst) und Abhängigkeiten: T1 (Prio 3, keine), T2 (Prio 1, abhängig von T1), T3 (Prio 3, abhängig von T2), T4 (Prio 3, abhängig von T2), T5 (Prio 1, abhängig von T3), T6 (Prio 2, abhängig von T4). Welche Ausführungsreihenfolge berücksichtigt Abhängigkeiten UND Prioritäten korrekt?",
                "T1→T2→T4→T5→T3→T6",
                "T1→T2→T3→T4→T5→T6",
                "T1→T2→T4→T3→T5→T6",
                "T1→T2→T3→T5→T4→T6",
                "D",
                "T1 und T2 müssen zuerst (Abhängigkeitskette). T5 hat Priorität 1 und hängt von T3 ab, daher muss T3 vor T5 laufen - dies zuerst, noch vor dem gleich priorisierten T4. Danach T4, abschließend T6 (abhängig von T4).",
            ),
            q(
                "Welches Element wird im Testquadrantenmodell dem Quadranten Q1 ('technologieorientiert' und 'Unterstützung des Teams') zugeordnet?",
                "Gebrauchstauglichkeitstests",
                "Smoke-Tests",
                "Benutzerabnahmetests",
                "Komponentenintegrationstests",
                "D",
                "Komponentenintegrationstests sind technologieorientiert und unterstützen das Entwicklungsteam - genau Q1. Gebrauchstauglichkeits- und Benutzerabnahmetests gehören zu Q3 (geschäftlich, Produktkritik), Smoke-Tests zu Q4 (technisch, Produktkritik).",
            ),
            q(
                "Welche Aussage beschreibt die Beziehung zwischen Produktrisiko und Testplanung NICHT genau?",
                "Hohe IT-Sicherheitsrisiken führten dazu, dass das Endekriterium für den Sicherheitstest auf 99 bestandene Testfälle erhöht wurde.",
                "Die geforderte Qualität des Netzwerkmoduls ist unklar, was zu weiteren Risikoanalysen führen wird.",
                "Nutzerprobleme mit der bestehenden Benutzungsschnittstelle führten zu zusätzlich geplanten Gebrauchstauglichkeitstests für das Nachfolgesystem.",
                "Kritische Ladezeiten der neuen Website führten zum Einsatz eines Performanztest-Experten im Projekt.",
                "B",
                "Unklare Qualitätsanforderungen erfordern zwar weitere Risikoanalyse, das beschreibt aber keine konkrete, aus dem Risiko abgeleitete Testplanungs-Maßnahme im Sinne der Risikosteuerung - anders als die anderen drei Beispiele, die jeweils klare Reaktionen (höheres Endekriterium, mehr Tests, Experteneinsatz) auf identifizierte Risiken zeigen.",
            ),
            q(
                "Welche der folgenden Kennzahlen ist eine Produktqualitätsmetrik?",
                "Mittlere Betriebsdauer bis zum Ausfall (Mean Time to Failure)",
                "Anzahl der aufgedeckten Fehlerzustände",
                "Anforderungsüberdeckung",
                "Fehlerdichte",
                "A",
                "Die mittlere Zeit bis zum Ausfall misst die Reife des Produkts und ist damit eine echte Produktqualitätsmetrik. Anzahl aufgedeckter Fehler und Fehlerdichte sind Fehlerzustandsmetriken, Anforderungsüberdeckung eine Überdeckungsmetrik.",
            ),
            q(
                "Ein europäisches Testteam entwickelt für einen nordamerikanischen Kunden mit DevOps/CI-CD-Ansatz. Welche Kommunikationsmethode wäre angesichts der geografischen Entfernung am WENIGSTEN effektiv für den Testfortschritt?",
                "Persönliche Treffen (von Angesicht zu Angesicht)",
                "Interaktive Dashboards",
                "E-Mail-Aktualisierungen",
                "Videokonferenzen",
                "A",
                "Persönliche Treffen über große Entfernungen und Zeitzonen hinweg sind am schwierigsten zu organisieren. Dashboards sind jederzeit verfügbar, E-Mails und Videokonferenzen überbrücken Zeitzonenunterschiede deutlich praktikabler als physische Treffen.",
            ),
            q(
                "Welche Aussage beschreibt ein Beispiel dafür, wie Konfigurationsmanagement (KM) das Testen unterstützt?",
                "Über die Versionsnummer der Testumgebung kann das KM-Werkzeug die Versionsnummern der verwendeten Bibliotheken, Platzhalter und Treiber abrufen.",
                "Die Änderung von Baselines wird durch KM-Werkzeuge flexibel unterstützt, wenn Tester dies für notwendig erachten.",
                "Das Konfigurationsmanagement verfolgt Testskripte und Testfälle; Testergebnisse werden dagegen durch das Fehlermanagement verwaltet.",
                "Komplexe Konfigurationselemente werden in einer Baseline zusammengefasst; ein Zurückgreifen auf frühere Baselines ist danach nicht mehr möglich.",
                "A",
                "KM erfasst für komplexe Konfigurationselemente wie Testumgebungen die Komponenten, ihre Beziehungen und Versionen. Baseline-Änderungen erfordern einen formalen Änderungsprozess (nicht 'flexibel nach Bedarf'), KM verfolgt auch Testergebnisse, und ein Rückgriff auf frühere Baselines ist grundsätzlich möglich.",
            ),
            q(
                "Ein Sortierfunktions-Test zeigt: TC3, TC4, TC5 schlagen fehl, wobei jeweils Duplikate in der Eingabe (z.B. mehrfache -2 oder 4) im Ergebnis nur einmal erscheinen. Welche Fehlerbeschreibung eignet sich am BESTEN für den Fehlerbericht?",
                "Das System kann mehrere Zahlensätze nicht sortieren. Referenz: TC3, TC4, TC5.",
                "Das System scheint Duplikate beim Sortieren zu ignorieren. Referenz: TC3, TC4, TC5.",
                "Das System kann keine negativen Zahlen sortieren. Referenz: TC4, TC5.",
                "TC3, TC4 und TC5 sind fehlerhaft (doppelte Eingabedaten) und sollten korrigiert werden.",
                "B",
                "Die Beobachtung zeigt konkret, dass Duplikate ignoriert und nur einmal zurückgegeben werden - das ist die präzise, für Entwickler nützliche Ursachenbeschreibung. Negative Zahlen werden korrekt einsortiert (nicht das Problem), und die Testfälle selbst sind nicht fehlerhaft, da Duplikate in der Spezifikation nicht ausgeschlossen sind.",
            ),
        ]

        # ---------- LO6: Fragen 39-40 ----------
        lo6_questions = [
            q(
                "Beschreibungen: 1) Unterstützung der Workflow-Verfolgung, 2) Kommunikation erleichtern, 3) virtuelle Maschinen, 4) Unterstützung von Review-Auswertungen. Kategorien: A) Statische Testwerkzeuge, B) Werkzeuge für Skalierbarkeit/Standardisierung, C) DevOps-Werkzeuge, D) Werkzeuge für Zusammenarbeit. Welche Zuordnung passt am BESTEN?",
                "1A, 2B, 3C, 4D",
                "1B, 2D, 3C, 4A",
                "1C, 2D, 3B, 4A",
                "1D, 2C, 3A, 4B",
                "C",
                "DevOps-Werkzeuge unterstützen u.a. die Workflow-Verfolgung (1C), Werkzeuge für Zusammenarbeit erleichtern Kommunikation (2D), virtuelle Maschinen fallen unter Skalierbarkeit/Standardisierung (3B), und statische Testwerkzeuge unterstützen Review-Auswertungen (4A).",
            ),
            q(
                "Welcher der folgenden Vorteile trifft AM EHESTEN auf die Testautomatisierung zu?",
                "Die Testautomatisierung ermöglicht auch die Messung komplexerer Überdeckungskriterien.",
                "Durch die Testautomatisierung wird ein Teil der Verantwortung für das Testen dem Werkzeuganbieter übertragen.",
                "Die Testautomatisierung macht kritisches Denken bei der Analyse von Testergebnissen überflüssig.",
                "Testautomatisierung generiert Testfälle auf Systemebene aus einer Analyse des Programmcodes.",
                "A",
                "Automatisierung kann Überdeckungsmaße liefern, die für Menschen zu komplex zu berechnen wären (z.B. White-Box-Überdeckung bei nicht-trivialem Code). Die Testverantwortung bleibt beim Tester, kritisches Denken bei der Ergebnisanalyse bleibt unverzichtbar, und Systemtestfälle lassen sich nicht allein aus Code-Analyse generieren, da erwartete Ergebnisse aus der Spezifikation stammen müssen.",
            ),
        ]

        chapter_map = [
            (lo1, "OFF-B-LO1", "Offizielle Prüfung SET B - LO1", lo1_questions),
            (lo2, "OFF-B-LO2", "Offizielle Prüfung SET B - LO2", lo2_questions),
            (lo3, "OFF-B-LO3", "Offizielle Prüfung SET B - LO3", lo3_questions),
            (lo4, "OFF-B-LO4", "Offizielle Prüfung SET B - LO4", lo4_questions),
            (lo5, "OFF-B-LO5", "Offizielle Prüfung SET B - LO5", lo5_questions),
            (lo6, "OFF-B-LO6", "Offizielle Prüfung SET B - LO6", lo6_questions),
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


if __name__ == "__main__":
    from app import app
    seed_official_set_a(app)
    seed_official_set_b(app)
    print("Offizielle Prüfungsfragen (SET A + SET B) erfolgreich eingespielt.")