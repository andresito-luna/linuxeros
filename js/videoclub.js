const URL = "http://127.0.0.1:5000/"
const botonlistar = document.querySelector("#botonlistar")
const botonbuscar = document.querySelector("#botonbuscar")
// const botonagregar = document.querySelector("#formulario")

const buscar = document.querySelector("#textoBuscar")

const listar = () => {
    contpelis.innerHTML = ""
    fetch(URL + "listar")
        .then(response => response.json())
        .then(pelis => {
            const list_l = pelis;
            list_l.map((item) => { //divide los datos que llegan desde la api en nuevos arrays, para poder manipularlos por separado
                const id = item.IdPeliculas
                const nombre = item.Nombre
                const genero = item.Genero
                const año = item.anio
                const stock = item.Stock
                const pelicula = `<tr><td>${id}</td><td>${nombre}</td><td>${genero}</td><td>${año}</td><td>${stock}</td><td><button id="${'editar' + String(id)}" onclick="rellenar(${id}, [${list_l}])">Editar</button></td></tr>`//genera una lista con los datos encontrados
                contpelis.innerHTML += pelicula //inserta la lista en la trabla con el id busqueda
            })
        })
}


const consultar = () => {
    contpelis.innerHTML = ""
    nombrePeli = buscar.value
    fetch(URL + "consultar")
        .then(response => response.json())
        .then(pelis => {
            const list_c = pelis;
            list_c.forEach(element => {
                // console.log(element)
                if (element.Nombre.trim() == nombrePeli) {
                    const pelicula = `<tr><td>${element.IdPeliculas}</td><td>${element.Nombre}</td><td>${element.Genero}</td><td>${element.anio}</td><td>${element.Stock}</td><td><button id="${'editar' + String(element.IdPeliculas)}" onclick="rellenar(${element.IdPeliculas}, [${list_c}])">Editar</button></td></tr>`//genera una lista con los datos encontrados
                    contpelis.innerHTML += pelicula //inserta la lista en la trabla con el id busqueda
                }
            }); 
        })
}


//------------------------------------------------------------------------


document.getElementById('formulario').addEventListener('submit', function(event) {event.preventDefault();

        const peliculasumar = {
        IdPeliculas: document.querySelector("#agregarid").value,
        Nombre: document.querySelector("#agregarnombre").value,
        Genero: document.querySelector("#agregargenero").value,
        anio: parseInt(document.querySelector("#agregaraño").value),
        Stock: parseInt(document.querySelector("#agregarstock").value)
    };


    fetch(URL + "agregar", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Ajusta el tipo de contenido según tus necesidades
        },
        body: JSON.stringify(peliculasumar) // Ajusta 'data' con los datos que deseas enviar en la solicitud
    })
        .then(function (response) {
            return response.json();
        })


        .then(function (data) {
            alert('Pelicula agregada correctamente.');
            // console.log(data)
            // Manejar la respuesta de la solicitud POST aquí
        })
        .catch( function (error) {
            alert('Error al agregar la pelicula.');
            // Manejar cualquier error que ocurra durante la solicitud
        });
console.log(peliculasumar)
document.getElementById('formulario').reset();
});




//-------------------------------------------------------------


function rellenar(id, bd) {
    let base = bd

    return alert("todo mal")
}




// botonagregar.addEventListener("submit", agregar);
botonlistar.addEventListener("click", listar);
botonbuscar.addEventListener("click", consultar);





