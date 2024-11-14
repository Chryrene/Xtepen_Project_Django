function editarLugar(id) {
    const nombre = document.querySelector(`#nombre-${id}`).textContent;
    const descripcion = document.querySelector(`#descripcion-${id}`).textContent;
    const capacidad = document.querySelector(`#capacidad-${id}`).textContent;
    const disponible = document.querySelector(`#disponible-${id}`).checked;

    fetch(`/api/editar_lugar/${id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            nombre: nombre,
            descripcion: descripcion,
            capacidad: capacidad,
            disponible: disponible
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Lugar actualizado exitosamente');
        } else {
            alert('Error al actualizar el lugar');
        }
    })
    .catch(error => console.error('Error:', error));
}

function eliminarLugar(id) {
    if (confirm('¿Estás seguro de que deseas eliminar este lugar?')) {
        fetch(`/api/eliminar_lugar/${id}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                document.querySelector(`#lugar-row-${id}`).remove();
                alert('Lugar eliminado exitosamente');
            } else {
                alert('Error al eliminar el lugar');
            }
        })
        .catch(error => console.error('Error:', error));
    }
}


console.log("lugares.js cargado correctamente");