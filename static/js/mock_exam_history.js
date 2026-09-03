async function loadHistory() {
    const response = await fetch("/api/mock-exam/history");
    const attempts = await response.json();

    const container = document.getElementById("history-container");

    if (attempts.length === 0) {
        container.innerHTML = `<div class="empty-state">Noch keine Prüfungssimulationen absolviert. <br><a href="/mock-exam">Jetzt starten</a></div>`;
        return;
    }

    container.innerHTML = attempts.map((a) => renderAttemptCard(a)).join("");
}

function renderAttemptCard(a) {
    const statusClass = a.passed ? "passed" : "failed";

    const loRows = a.lo_results.map((lo) => {
        const cellClass = lo.percent >= 65 ? "ok" : "low";
        return `<div class="mini-lo-row"><span>${lo.code} – ${lo.title}</span><span class="${cellClass}">${lo.correct}/${lo.total} (${lo.percent}%)</span></div>`;
    }).join("");

    return `
        <div class="attempt-card" onclick="this.classList.toggle('expanded')">
            <div class="attempt-left">
                <div class="attempt-date">${a.taken_at}</div>
                <div class="attempt-score ${statusClass}">${a.overall_percent}%</div>
                <div>${a.total_correct} von ${a.total_questions} richtig</div>
            </div>
            <div class="attempt-badge ${statusClass}">${a.passed ? "Bestanden" : "Nicht bestanden"}</div>
            <div class="attempt-details">${loRows}</div>
        </div>
    `;
}

loadHistory();