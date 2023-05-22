

const input = document.querySelector("#textoBuscar")
const btn = document.querySelector("#boton")
const refrescar = document.querySelector("#refrescar")
let nombrePeli = ""

const llamada = () => {nombrePeli = input.value
    
   
    fetch(`https://online-movie-database.p.rapidapi.com/auto-complete?q=${nombrePeli}`, {

        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '3c2b00260cmshc4004f9d92f6104p1be85bjsn014051503cef',
            'X-RapidAPI-Host': 'online-movie-database.p.rapidapi.com'//esto lo pide la api 
        }
    })


        .then(response => response.json())
       
        .then(data => {
            const list = data.d;
            list.map((item) => { //divide los datos que llegan desde la api en nuevos arrays, para poder manipularlos por separado
                
               const nombre = item.l //extrae nombre de peli
               const imagen = item.i.imageUrl //extrae la imagen de la peli
               const año = item.y //idem año
               const actores = item.s //idem actores y actrices
                

               const pelicula = `<div class="buschijo"><img src="${imagen}"class="foto"><h2>${nombre}</h2><h2>${año}</h2><h2>${actores}</h2></div>`//genera una lista con los datos encontrados
               busqueda.innerHTML += pelicula //inserta la lista en el div con el id busqueda
            
            
         
            
            })
        })
        input.value=""
    }
   
      
        btn.addEventListener("click", llamada)
        refrescar.addEventListener("click", function(){location.reload()})

      

        