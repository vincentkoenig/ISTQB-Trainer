const state = {
    questions: [],
    answers: {},
    currentIndex: 0,
    timerInterval: null,
    remainingSeconds: 0,
};

async function startExam() {
    const response = await fetch("/api/mock-exam/start");
    const data = await response.json();
    state.questions = data.questions;
    state.remainingSeconds = data.duration_seconds;
    renderExam();
    startTimer();
}

function startTimer() {
    updateTimerDisplay();
    state.timerInterval = setInterval(() => {
        state.remainingSeconds--;
        updateTimerDisplay();
        if (state.remainingSeconds <= 0) {
            clearInterval(state.timerInterval);
            submitExam();
        }
    }, 1000);
}

function updateTimerDisplay() {
    const el = document.getElementById("timer");
    if (!el) return;
    const m = Math.floor(state.remainingSeconds / 60);
    const s = state.remainingSeconds % 60;
    el.textContent = `${m}:${s.toString().padStart(2, "0")}`;
    el.classList.toggle("warning", state.remainingSeconds < 300);
}

function renderExam() {
    const container = document.getElementById("exam-container");
    container.innerHTML = `
        <div class="exam-header">
            <div class="progress-indicator">Frage ${state.currentIndex + 1} von ${state.questions.length}</div>
            <div class="timer" id="timer">--:--</div>
        </div>
        <div class="question-nav" id="question-nav"></div>
        <div id="question-slot"></div>
        <div class="exam-actions">
            <button class="nav-button" id="prev-btn" onclick="goPrev()">Zurück</button>
            <button class="submit-button" onclick="confirmSubmit()">Prüfung abgeben</button>
            <button class="nav-button" id="next-btn" onclick="goNext()">Weiter</button>
        </div>
    `;
    updateTimerDisplay();
    renderNav();
    renderQuestion();
}

function renderNav() {
    const nav = document.getElementById("question-nav");
    nav.innerHTML = state.questions.map((q, i) => `
        <button class="nav-dot ${state.answers[q.id] ? 'answered' : ''} ${i === state.currentIndex ? 'current' : ''}" onclick="goToQuestion(${i})">${i + 1}</button>
    `).join("");
}

function renderQuestion() {
    const q = state.questions[state.currentIndex];
    const slot = document.getElementById("question-slot");
    const selected = state.answers[q.id];

    const optionsHtml = Object.entries(q.options).map(([letter, text]) => `
        <button class="option-button ${selected === letter ? 'selected' : ''}" onclick="selectAnswer('${q.id}', '${letter}')">
            ${letter}) ${text}
        </button>
    `).join("");

    slot.innerHTML = `
        <div class="question-card">
            <div class="question-prompt">${q.prompt}</div>
            <div>${optionsHtml}</div>
        </div>
    `;

    document.getElementById("prev-btn").disabled = state.currentIndex === 0;
    document.getElementById("next-btn").disabled = state.currentIndex === state.questions.length - 1;
}

function selectAnswer(questionId, letter) {
    state.answers[questionId] = letter;
    renderNav();
    renderQuestion();
}

function goNext() {
    if (state.currentIndex < state.questions.length - 1) {
        state.currentIndex++;
        renderNav();
        renderQuestion();
        updateProgressIndicator();
    }
}

function goPrev() {
    if (state.currentIndex > 0) {
        state.currentIndex--;
        renderNav();
        renderQuestion();
        updateProgressIndicator();
    }
}

function goToQuestion(index) {
    state.currentIndex = index;
    renderNav();
    renderQuestion();
    updateProgressIndicator();
}

function confirmSubmit() {
    const unanswered = state.questions.length - Object.keys(state.answers).length;
    if (unanswered > 0) {
        const proceed = confirm(`Du hast noch ${unanswered} Frage(n) nicht beantwortet. Trotzdem abgeben?`);
        if (!proceed) return;
    }
    submitExam();
}

async function submitExam() {
    if (state.timerInterval) clearInterval(state.timerInterval);

    const response = await fetch("/api/mock-exam/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answers: state.answers }),
    });
    const result = await response.json();
    renderResults(result);
}

function renderResults(result) {
    const container = document.getElementById("exam-container");
    const passedClass = result.passed ? "passed" : "failed";

    const rows = result.lo_results.map((lo) => {
        const cellClass = lo.percent >= 65 ? "ok" : "low";
        return `
            <tr>
                <td>${lo.code} – ${lo.title}</td>
                <td>${lo.correct} / ${lo.total}</td>
                <td class="percent-cell ${cellClass}">${lo.percent}%</td>
            </tr>
        `;
    }).join("");

    container.innerHTML = `
        <div class="result-summary">
            <div class="result-percent ${passedClass}">${result.overall_percent}%</div>
            <p>${result.total_correct} von ${result.total_questions} Fragen richtig</p>
            <p><strong>${result.passed ? "✅ Bestanden!" : "❌ Nicht bestanden"}</strong> (Bestehensgrenze: 65%)</p>
        </div>
        <table class="result-table">
            <thead>
                <tr><th>Learning Objective</th><th>Punkte</th><th>Prozent</th></tr>
            </thead>
            <tbody>${rows}</tbody>
        </table>
        <br>
        <a href="/" class="nav-button" style="display:inline-block; text-decoration:none;">Zurück zum Dashboard</a>
        <a href="/mock-exam/history" class="nav-button" style="display:inline-block; text-decoration:none; background:#6c757d;">Prüfungsverlauf ansehen</a>
    `;
}

function updateProgressIndicator() {
    const el = document.querySelector(".progress-indicator");
    if (el) {
        el.textContent = `Frage ${state.currentIndex + 1} von ${state.questions.length}`;
    }
}

startExam();