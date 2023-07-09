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
        cursor.execute("""SELECT * FROM peliculas""")
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
            print(peli)
        return jsonify(response)
                
        
    except:
        return jsonify("erroooooor")
    

#----------------------------------------------------------------------------------

@app.route("/agregar", methods=['POST'])
def agregar_pelicula():
    data = request.get_json()
    if 'Nombre' not in data or 'Genero' not in data or 'anio' not in data:
        return jsonify({'error': 'Falta uno o más campos requeridos'}), 400
    #print(data)
    print(type(data))
    # print(data['IdPeliculas'])
    # print(data['Nombre'])
    # print(data['Genero'])
    # print(data['anio'])
    # print(data['Stock'])
    try:
        cursor = conexion.cursor()
        cursor.execute("""
                    INSERT INTO peliculas(IdPeliculas, Nombre, Genero, Año, Stock)
                    VALUES(%s,%s,%s,%s,%s) """,
                    (data['IdPeliculas'],data['Nombre'], data['Genero'], data['anio'], data['Stock']))
        conexion.commit()
        cursor.close()
        
        return jsonify({'mensaje': 'Alta efectuada correctamente'}), 201
    except:
        return jsonify({'error': 'Error al dar de alta el producto'}), 500



#------------------------------MODIFICAR----------------------------------------------------



@app.route("/modificar", methods=['PUT'])

def modificar_pelicula():
    data = request.get_json()
    print(data)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
                    UPDATE peliculas (Nombre, Genero, Año, Stock)
                    SET Nombre = "%s", Genero= "%s", anio = "%s", Stock = "%s" 
                    WHERE IdPeliculas = %s """,
                    (data['Nombre'], data['Genero'], data['anio'], data['Stock'], data['IdPeliculas']))
        conexion.commit()
        cursor.close()

        return jsonify({'mensaje': 'Alta efectuada correctamente'}), 201
    except:
        return jsonify({'error': 'Error al dar de alta el producto'}), 500



#-------------------------------------------------------------------


@app.route('/editar/<codigo>')
def consultar2_pelicula(codigo):
    try:
        cursor = conexion.cursor()
        cursor.execute("""SELECT * FROM peliculas WHERE IdPeliculas = %s""",(codigo,))
        pelis = cursor.fetchone()
        cursor.close()
                
        return jsonify(pelis)
    except:
        return jsonify("erroooooor")



#----------------------------------------------------------------------------------


if __name__ == '__main__':

    app.run(debug=True)
