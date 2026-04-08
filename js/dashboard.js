const dashboardData = {
  "time_series": [
    {"year": 2023, "gdp_growth": 0.6, "inflation": 9.28, "unemployment": 10.2, "exchange_rate": 3900, "public_debt": 52.0, "fiscal_deficit": 4.3},
    {"year": 2024, "gdp_growth": 1.5, "inflation": 5.8, "unemployment": 10.5, "exchange_rate": 4100, "public_debt": 54.5, "fiscal_deficit": 5.6},
    {"year": 2025, "gdp_growth": 2.6, "inflation": 3.5, "unemployment": 9.8, "exchange_rate": 4250, "public_debt": 56.2, "fiscal_deficit": 7.1}
  ],
  "labels": {
    "gdp_growth": "Crecimiento PIB (%)",
    "inflation": "Inflación (%)",
    "unemployment": "Desempleo (%)",
    "exchange_rate": "Tasa de Cambio (COP/USD)",
    "public_debt": "Deuda Pública (% PIB)",
    "fiscal_deficit": "Déficit Fiscal (% PIB)"
  }
};

let mainChart = null;

function initDashboard() {
    renderVariableChart('gdp_growth');
    renderPhillipsChart();
    renderFiscalChart();
}

function renderVariableChart(variableKey) {
    const ctx = document.getElementById('variableChart').getContext('2d');
    const label = dashboardData.labels[variableKey];
    const data = dashboardData.time_series.map(d => d[variableKey]);
    const years = dashboardData.time_series.map(d => d.year);

    if (mainChart) mainChart.destroy();

    mainChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: years,
            datasets: [{
                label: label,
                data: data,
                borderColor: '#6366f1',
                backgroundColor: 'rgba(99, 102, 241, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: {
                y: { beginAtZero: false, grid: { display: false } },
                x: { grid: { display: false } }
            }
        }
    });
}

function updateVariableChart(name) {
    const mapping = {
        'GDP Growth': 'gdp_growth',
        'Inflation': 'inflation',
        'Unemployment': 'unemployment',
        'Exchange Rate': 'exchange_rate'
    };
    renderVariableChart(mapping[name]);
}

function renderPhillipsChart() {
    const ctx = document.getElementById('phillipsChart').getContext('2d');
    new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Inflación vs Desempleo',
                data: dashboardData.time_series.map(d => ({ x: d.inflation, y: d.unemployment })),
                backgroundColor: '#f43f5e',
                pointRadius: 6
            }]
        },
        options: {
            scales: {
                x: { title: { display: true, text: 'Inflación (%)' } },
                y: { title: { display: true, text: 'Desempleo (%)' } }
            }
        }
    });
}

function renderFiscalChart() {
    const ctx = document.getElementById('fiscalChart').getContext('2d');
    const years = dashboardData.time_series.map(d => d.year);
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: years,
            datasets: [
                {
                    label: 'Deuda Pública (% PIB)',
                    data: dashboardData.time_series.map(d => d.public_debt),
                    backgroundColor: '#818cf8'
                },
                {
                    label: 'Déficit Fiscal (% PIB)',
                    data: dashboardData.time_series.map(d => d.fiscal_deficit),
                    backgroundColor: '#fb7185'
                }
            ]
        },
        options: {
            scales: {
                y: { stacked: false, beginAtZero: true }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', initDashboard);
