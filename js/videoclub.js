const URL = "4ndr35M00N.pythonanywhere.com/"
const botonlistar = document.querySelector("#botonlistar")
const botonbuscar = document.querySelector("#botonbuscar")
const buscar = document.querySelector("#textoBuscar")

const listar = () => {
    fetch(URL + "listar")
        .then(response => response.json())
        .then(pelis => {
            const list = pelis;
            list.map((item) => { //divide los datos que llegan desde la api en nuevos arrays, para poder manipularlos por separado
                const id = item.IdPeliculas
                const nombre = item.Nombre
                const genero = item.Genero
                const año = item.anio
                const stock = item.Stock
                const pelicula = `<tr><td>${id}</td><td>${nombre}</td><td>${genero}</td><td>${año}</td><td>${stock}</td></tr>`//genera una lista con los datos encontrados
                contpelis.innerHTML += pelicula //inserta la lista en la trabla con el id busqueda
            })
        })
}



const consultar = () => {
    nombrePeli = buscar.value
    fetch(URL + "consultar")
        .then(response => response.json())
        .then(pelis => {
            const list = pelis;
            list.forEach(element => {
                console.log(element)
                if (element.Nombre.trim() == nombrePeli) {
                    const pelicula = `<tr><td>${element.IdPeliculas}</td><td>${element.Nombre}</td><td>${element.Genero}</td><td>${element.anio}</td><td>${element.Stock}</td></tr>`//genera una lista con los datos encontrados
                    contpelis.innerHTML += pelicula //inserta la lista en la trabla con el id busqueda
                }
            }); 
        })
}


//------------------------------------------------------------------------
const peliculasumar = {
    nombre: document.querySelector("#agregarnombre").value,
    genero: document.querySelector("#agregargenero").value,
    año: parseInt(document.querySelector("#agregaraño").value),
    stock: parseInt(document.querySelector("#agregarstock").value),
}
const agregar = () => {
    nombrePeli = input.value

    fetch(URL + "agregar", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Ajusta el tipo de contenido según tus necesidades
        },
        body: JSON.stringify(peliculasumar) // Ajusta 'data' con los datos que deseas enviar en la solicitud
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Manejar la respuesta de la solicitud POST aquí
        })
        .catch(error => {
            // Manejar cualquier error que ocurra durante la solicitud
        });
}


botonlistar.addEventListener("click", listar)
botonbuscar.addEventListener("click", consultar)
document.querySelector("#formulario").addEventListener('submit', agregar)