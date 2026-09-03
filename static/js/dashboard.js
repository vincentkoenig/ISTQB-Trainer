async function loadDashboard() {
    const response = await fetch("/api/dashboard");
    const learningObjectives = await response.json();

    const container = document.getElementById("lo-list");
    container.innerHTML = "";

    learningObjectives.forEach((lo) => {
        const card = document.createElement("div");
        card.className = "lo-card";

        const box = lo.box_distribution;
        const neverAnswered = lo.not_started;
        const inProgress = box[1] - neverAnswered; // Box 1, aber schon mal beantwortet = zuletzt falsch

        card.innerHTML = `
            <strong>${lo.code} – ${lo.title}</strong>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${lo.percent}%;">${lo.percent}%</div>
            </div>
            <small>${lo.mastered} von ${lo.total_questions} Fragen gemeistert (Box 3+)</small>
    
            <div class="box-breakdown">
                <div class="box-row"><span class="box-dot" style="background:#ccc;"></span> Noch nie beantwortet: ${neverAnswered}</div>
                <div class="box-row"><span class="box-dot" style="background:#e74c3c;"></span> Zuletzt falsch (Box 1): ${inProgress}</div>
                <div class="box-row"><span class="box-dot" style="background:#f39c12;"></span> Box 2: ${box[2]}</div>
                <div class="box-row"><span class="box-dot" style="background:#f1c40f;"></span> Box 3: ${box[3]}</div>
                <div class="box-row"><span class="box-dot" style="background:#2ecc71;"></span> Box 4: ${box[4]}</div>
                <div class="box-row"><span class="box-dot" style="background:#27ae60;"></span> Box 5 (sicher): ${box[5]}</div>
            </div>
    
            <small>${lo.due_count} Frage(n) heute fällig</small><br>
            <a class="button" href="/practice/${lo.id}">Üben</a>
            <a class="button" href="/review/${lo.id}" style="background:#6c757d;">Alle Fragen ansehen</a>
        `;
        container.appendChild(card);
    });
}

loadDashboard();