async function loadDashboard() {
    const response = await fetch("/api/dashboard");
    const learningObjectives = await response.json();

    const container = document.getElementById("lo-list");
    container.innerHTML = "";

    learningObjectives.forEach((lo) => {
        const card = document.createElement("div");
        card.className = "lo-card";
        card.innerHTML = `
            <strong>${lo.code} – ${lo.title}</strong>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${lo.percent}%;">${lo.percent}%</div>
            </div>
            <small>${lo.due_count} Frage(n) heute fällig</small><br>
            <a class="button" href="/practice/${lo.id}">Üben</a>
        `;
        container.appendChild(card);
    });
}

loadDashboard();