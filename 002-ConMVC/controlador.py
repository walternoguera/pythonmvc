import mysql.connector

def dameNombre():
    conexion = mysql.connector.connect(
        host = 'localhost',
        user = 'mundev',
        password = 'mundev',
        database = 'nombre'
    )

    cursor = conexion.cursor()
    peticion = "SELECT * FROM nombres"
    cursor.execute(peticion)
    fila = cursor.fetchone()
    return fila[1]
