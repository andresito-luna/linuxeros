import pymysql
from flask import Flask, jsonify, request
from flask_cors import CORS

# Nombre del objeto flask.
app = Flask(__name__)
CORS(app)

# Conexión a la base de datos
conexion = pymysql.connect(
    host="codo-a-codo-linuxeros.clfcnl4qjyxz.sa-east-1.rds.amazonaws.com",  # Cambiar por la dirección del servidor de la base de datos
    port = 3306,        #este es el puerto que te asigna el xxamp
    user="andres",              # Cambiar por el nombre de usuario de la base de datos
    password="LinUx&2023#",              # Cambiar por la contraseña de la base de datos
    database="CineCode"  # Cambiar por el nombre de la base de datos
    
)
#-------------------------------------------------------------------
@app.route('/consultar')
def consultar_pelicula():
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

#----------------------------------------------------------------------------
@app.route('/listar')
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
@app.route("/agregar", methods=['POST'])
def agregar_pelicula():
    data = request.get_json()
    if 'nombre' not in data or 'genero' not in data or 'año' not in data:
        return jsonify({'error': 'Falta uno o más campos requeridos'}), 400
    try:
        cursor = conexion.cursor()
        cursor.execute("""
                    INSERT INTO productos(nombre, genero, año, stock)
                    VALUES(?,?,?,?) """,
                    (data['nombre'], data['genero'], data['año'], data['stock']))
        
        cursor.close()
        
        return jsonify({'mensaje': 'Alta efectuada correctamente'}), 201
    except:
        return jsonify({'error': 'Error al dar de alta el producto'}), 500
    
     


if __name__ == '__main__':

    app.run(debug=True)



listar_pelis()
