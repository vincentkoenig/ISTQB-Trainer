const loId = document.body.dataset.loId;
let questions = [];
let currentIndex = 0;
let answeredCurrent = false;

async function loadQuestions() {
    const response = await fetch(`/api/practice/${loId}`);
    const data = await response.json();

    document.getElementById("lo-title").textContent = `Üben: ${data.lo_title}`;
    questions = data.questions;
    currentIndex = 0;

    if (questions.length === 0) {
        renderNoQuestionsDue();
    } else {
        renderQuestion();
    }
}

function renderNoQuestionsDue() {
    const container = document.getElementById("practice-container");
    container.innerHTML = `
        <div class="question-card">
            <p>Aktuell sind keine Fragen fällig. Schau später wieder vorbei!</p>
            <a href="/" class="next-button" style="display:inline-block; text-decoration:none;">Zurück zum Dashboard</a>
        </div>
    `;
}

function renderQuestion() {
    answeredCurrent = false;
    const question = questions[currentIndex];
    const container = document.getElementById("practice-container");

    const optionsHtml = Object.entries(question.options)
        .map(([letter, text]) => `
            <button class="option-button" data-letter="${letter}" onclick="submitAnswer('${letter}')">
                ${letter}) ${text}
            </button>
        `)
        .join("");

    container.innerHTML = `
        <div class="progress-indicator">Frage ${currentIndex + 1} von ${questions.length}</div>
        <div class="question-card">
            <div class="question-prompt">${question.prompt}</div>
            <div id="options">${optionsHtml}</div>
            <div id="feedback"></div>
        </div>
    `;
}

async function submitAnswer(selectedLetter) {
    if (answeredCurrent) return;
    answeredCurrent = true;

    const question = questions[currentIndex];
    window._lastSelectedLetter = selectedLetter;
    window._lastQuestionId = question.id;

    const response = await fetch(`/api/answer/${question.id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ selected: selectedLetter, difficulty: "einfach" }),
    });
    const result = await response.json();
    window._lastResult = result;

    document.querySelectorAll(".option-button").forEach((btn) => {
        const letter = btn.dataset.letter;
        if (letter === result.correct_option) {
            btn.classList.add("correct");
        } else if (letter === selectedLetter && !result.correct) {
            btn.classList.add("incorrect");
        }
        btn.disabled = true;
    });

    const feedback = document.getElementById("feedback");

    if (result.correct) {
        feedback.innerHTML = `
            <div class="explanation-box">
                <strong>✅ Richtig!</strong>
                ${result.explanation ? `<p>${result.explanation}</p>` : ""}
            </div>
            <p style="margin-top:12px; font-size:14px; color:#666;">Wie schwer war diese Frage für dich?</p>
            <div style="display:flex; gap:8px; margin-top:8px;">
                <button class="next-button" style="background:#c0392b;" onclick="rateDifficulty('schwer')">Schwer (5 Min)</button>
                <button class="next-button" style="background:#2c3e50;" onclick="rateDifficulty('einfach')">Einfach (10 Min)</button>
                <button class="next-button" style="background:#27ae60;" onclick="rateDifficulty('sehr_einfach')">Sehr einfach (1 Tag)</button>
            </div>
        `;
    } else {
        // Innerhalb dieser Sitzung sofort wieder einreihen, ein paar Fragen später
        const requeuedCopy = { ...question };
        const insertPos = Math.min(currentIndex + 3, questions.length);
        questions.splice(insertPos, 0, requeuedCopy);

        feedback.innerHTML = `
            <div class="explanation-box">
                <strong>❌ Falsch.</strong>
                ${result.explanation ? `<p>${result.explanation}</p>` : ""}
                <p style="margin-top:8px; font-size:13px; color:#666;">Diese Frage wird dir gleich in dieser Sitzung nochmal gezeigt.</p>
            </div>
            <button class="next-button" onclick="nextQuestion()">
                ${currentIndex + 1 < questions.length ? "Nächste Frage" : "Fertig"}
            </button>
        `;
    }
}

async function rateDifficulty(difficulty) {
    await fetch(`/api/answer/${window._lastQuestionId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ selected: window._lastSelectedLetter, difficulty: difficulty }),
    });
    nextQuestion();
}

function nextQuestion() {
    currentIndex++;
    if (currentIndex < questions.length) {
        renderQuestion();
    } else {
        document.getElementById("practice-container").innerHTML = `
            <div class="question-card">
                <p>🎉 Alle fälligen Fragen für dieses Kapitel beantwortet!</p>
                <a href="/" class="next-button" style="display:inline-block; text-decoration:none;">Zurück zum Dashboard</a>
            </div>
        `;
    }
}

loadQuestions();