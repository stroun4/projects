// Ejemplo básico de actualización de la interfaz
function mostrarEstadisticas(estadisticas) {
    const mainElement = document.querySelector('main');
    mainElement.innerHTML = `<h2>Estadísticas de partidas para ${nombreInvocador}</h2>`;
    
    estadisticas.forEach(partida => {
        mainElement.innerHTML += `<div>${partida.gameId}: Campeón ${partida.champion}</div>`;
    });
}

// ----------------------------------------------------------------------------------------------------//

fetch('http://localhost:5000/api/obtener_estadisticas_partidas?nombre=nombre_de_tu_invocador')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error al obtener datos:', error));
