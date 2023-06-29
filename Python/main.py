import pymysql
from flask import Flask, jsonify, request
from flask_cors import CORS

# Nombre del objeto flask.
app = Flask(__name__)
CORS(app)

# Conexión a la base de datos
conexion = pymysql.connect(
    host="localhost",  # Cambiar por la dirección del servidor de la base de datos
    port = 3306,        #este es el puerto que te asigna el xxamp
    user="root",              # Cambiar por el nombre de usuario de la base de datos
    password="",              # Cambiar por la contraseña de la base de datos
    database="noventas videoclub"  # Cambiar por el nombre de la base de datos
    
)
#-------------------------------------------------------------------
def consultar_pelicula():
    try:
        cursor = conexion.cursor()
        nombre = input("Ingrese nombre de la pelicula: ")
        cursor.execute("SELECT * FROM peliculas where Nombre =%s", (nombre,))
        pelis = cursor.fetchone()
        cursor.close()
        
        if pelis:
            print(f"Encontramos {nombre}")
            print(f"Nonmbre: {pelis[1]}")
            print(f"Genero: {pelis[2]}")
            print(f"Año: {pelis[3]}")
            print(f"Stock: {pelis[4]}")
        else:
            print(f'No se que es "{nombre}"')
    except pymysql.Error as e:
            print("Error al consultar la peli")

#----------------------------------------------------------------------------
@app.route('/')
def listar_pelis():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas")
        pelis = cursor.fetchall()
        cursor.close()
        response = []
        
        for peli in pelis:
            response.append({
                'IdPeliculas': peli[0],
                'Nombre': peli[1],
                'Genero': peli[2],
                'anio': peli[3],
                'Stock': peli[4],
            })
        return jsonify(response)
                
        
    except:
        return jsonify("erroooooor")

#----------------------------------------------------------------------------------
def agregar_pelicula():
    try:
        nombre = input("Nombre de la Pelicula: ")
        genero = input("Genero de la Pelicula: ")
        año = int(input("Año de estreno: "))
        stock = int(input("Cantidad de copias: "))
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO peliculas (Nombre, Genero, Año, Stock) VALUES (%s,%s,%s,%s)", (nombre,genero,año,stock))
        conexion.commit()
        cursor.close()

        print("se agrego la peli")
    except pymysql.Error as e:
        print("Error al agregar")


if __name__ == '__main__':

    app.run(debug=True)



listar_pelis()
