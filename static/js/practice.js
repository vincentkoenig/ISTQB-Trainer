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

    const response = await fetch(`/api/answer/${question.id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ selected: selectedLetter }),
    });
    const result = await response.json();

    // Buttons einfärben
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
    feedback.innerHTML = `
        <div class="explanation-box">
            <strong>${result.correct ? "✅ Richtig!" : "❌ Falsch."}</strong>
            ${result.explanation ? `<p>${result.explanation}</p>` : ""}
        </div>
        <button class="next-button" onclick="nextQuestion()">
            ${currentIndex + 1 < questions.length ? "Nächste Frage" : "Fertig"}
        </button>
    `;
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