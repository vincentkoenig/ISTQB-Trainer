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


if __name__ == "__main__":
    from app import app
    seed_official_set_a(app)
    print("Offizielle Prüfungsfragen (SET A) erfolgreich eingespielt.")