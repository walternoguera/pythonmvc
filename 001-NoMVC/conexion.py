import tkinter as tk
import mysql.connector

ventana = tk.Tk()
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

texto = tk.Label(ventana,text=fila[1],fg="red")
texto.pack(padx=50,pady=50)

ventana.mainloop() 
