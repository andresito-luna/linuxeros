const URL = "http://127.0.0.1:5000/"

fetch(URL)
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