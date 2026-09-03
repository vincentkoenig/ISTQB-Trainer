const loId = document.body.dataset.loId;
let currentFilter = "all";

async function loadReview() {
    const response = await fetch(`/api/review/${loId}?filter=${currentFilter}`);
    const data = await response.json();

    document.getElementById("lo-title").textContent = `Fragen ansehen: ${data.lo_title}`;
    renderChapters(data.chapters);
}

function renderChapters(chapters) {
    const container = document.getElementById("review-container");

    if (chapters.length === 0) {
        container.innerHTML = "<p>Keine Fragen in dieser Ansicht.</p>";
        return;
    }

    container.innerHTML = chapters.map((chapter) => `
        <h2 class="chapter-heading">${chapter.chapter_number} – ${chapter.chapter_title}</h2>
        ${chapter.questions.map((q) => renderQuestionCard(q)).join("")}
    `).join("");
}

function renderQuestionCard(q) {
    const statusBadge = q.times_seen === 0
        ? ""
        : q.is_struggling
            ? `<span class="badge badge-struggling">Noch nicht gemeistert</span>`
            : `<span class="badge badge-mastered">Box ${q.box}</span>`;

    const optionsHtml = Object.entries(q.options)
        .map(([letter, text]) => `
            <div class="review-option ${letter === q.correct_option ? 'correct' : ''}">
                ${letter}) ${text}
            </div>
        `)
        .join("");

    return `
        <div class="review-card" onclick="this.classList.toggle('expanded')">
            <div class="review-card-header">
                <div class="review-prompt">${q.prompt}</div>
                <div class="review-badges">${statusBadge}</div>
            </div>
            <div class="review-details">
                ${optionsHtml}
                ${q.explanation ? `<div class="review-explanation">${q.explanation}</div>` : ""}
                <div class="review-stats">Gesehen: ${q.times_seen}× · Richtig: ${q.times_correct}×</div>
            </div>
        </div>
    `;
}

document.querySelectorAll(".filter-button").forEach((btn) => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".filter-button").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        currentFilter = btn.dataset.filter;
        loadReview();
    });
});

loadReview();