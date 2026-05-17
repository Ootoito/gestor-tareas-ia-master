document.addEventListener("DOMContentLoaded", function () {
    const canvasEstados = document.getElementById("graficoEstadosChart");

    console.log("Canvas encontrado:", canvasEstados);
    console.log("data-pendientes atributo:", canvasEstados.getAttribute("data-pendientes"));

    const datos = [
        Number(canvasEstados.getAttribute("data-pendientes") || 0),
        Number(canvasEstados.getAttribute("data-pendientes-firma") || 0),
        Number(canvasEstados.getAttribute("data-pendientes-devolucion") || 0),
        Number(canvasEstados.getAttribute("data-programadas") || 0),
        Number(canvasEstados.getAttribute("data-urgentes") || 0),
        Number(canvasEstados.getAttribute("data-completadas") || 0)
    ];

    console.log("Datos definitivos gráfico estados:", datos);

    new Chart(canvasEstados.getContext("2d"), {
        type: "bar",
        data: {
            labels: ["Pendientes", "Pend. firma", "Pend. devolución", "Programadas", "Urgentes", "Completadas"],
            datasets: [{
                label: "Tareas",
                data: datos,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });

    const canvasTecnicos = document.getElementById("graficoTecnicosChart");

if (canvasTecnicos) {
    const tecnicos = JSON.parse(canvasTecnicos.getAttribute("data-tecnicos") || "[]");
    const totales = JSON.parse(canvasTecnicos.getAttribute("data-totales") || "[]");

    new Chart(canvasTecnicos.getContext("2d"), {
        type: "bar",
        data: {
            labels: tecnicos,
            datasets: [{
                label: "Tareas",
                data: totales,
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: "y",
            responsive: true,
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}
});