// Konfigurasi Standar Dark Mode untuk Chart.js
Chart.defaults.color = '#ffffff';
Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';

function renderFisheryChart(tangkapan, biaya) {
    const ctx = document.getElementById('fisheryChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Pendapatan', 'Biaya Solar'],
            datasets: [{
                label: 'Analisis Ekonomi (Rp)',
                data: [tangkapan, biaya],
                backgroundColor: ['#3b82f6', '#ef4444'], // Biru & Merah
                borderRadius: 10
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            }
        }
    });
}