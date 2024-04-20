import tkinter as tk
from controlador import *

def ventana():
    ventana = tk.Tk()
    texto = tk.Label(ventana,text=dameNombre(),fg="red")
    texto.pack(padx=50,pady=50)

    ventana.mainloop()
