from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import messagebox
import entidades.usuario as usuario
import sqlite3

class  VentanaUsuario:
    db_nombre = 'database.db'

    def __init__(self, ventana):
        self.ventana = ventana
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()
        ancho2 = 800
        alto2 = 600
        izquierda = (ancho - ancho2) / 2
        arriba = (alto - alto2) / 2
        self.ventana.geometry("%dx%d+%d+%d" % (ancho2, alto2, izquierda, arriba))
        self.ventana.title("Agregar Vehiculo")
        self.ventana.resizable(False, False)


        etiqueta = Frame(ventana, width="100", height="400", pady=120)
        etiqueta.pack(expand=True, fill=tk.BOTH)

        self.nombre = Label(etiqueta, text = 'Nombre', font= ("Bahnschrift Light",10))
        self.nombre.pack(fill=tk.BOTH)
        self.nombre = Entry(etiqueta)
        self.nombre.pack()

        self.apellido =Label(etiqueta, text = 'Apellido', font= ("Bahnschrift Light",10))
        self.apellido.pack(fill=tk.BOTH)
        self.apellido = Entry(etiqueta)
        self.apellido.pack()

        self.carnetConducir =Label(etiqueta, text = 'Carnet de Conducir', font= ("Bahnschrift Light",10))
        self.carnetConducir.pack(fill=tk.BOTH)
        self.carnetConducir = Entry(etiqueta)
        self.carnetConducir.pack()

        self.fechaNacimiento =Label(etiqueta, text = 'Fecha de nacimiento', font= ("Bahnschrift Light",10))
        self.fechaNacimiento.pack(fill=tk.BOTH)
        self.fechaNacimiento = Entry(etiqueta)
        self.fechaNacimiento.pack()

        self.correo =Label(etiqueta, text = 'Correo', font= ("Bahnschrift Light",10))
        self.correo.pack(fill=tk.BOTH)
        self.correo = Entry(etiqueta)
        self.correo.pack()

        self.extrangero =Label(etiqueta, text = 'Es extrangero?', font= ("Bahnschrift Light",10))
        self.extrangero.pack(fill=tk.BOTH)
        self.extrangero = Entry(etiqueta)
        self.extrangero.pack()

        self.cuil =Label(etiqueta, text = 'CUIL', font= ("Bahnschrift Light",10))
        self.cuil.pack(fill=tk.BOTH)
        self.cuil = Entry(etiqueta)
        self.cuil.pack()

        self.pasaporte =Label(etiqueta, text = 'Pasaporte', font= ("Bahnschrift Light",10))
        self.pasaporte.pack(fill=tk.BOTH)
        self.pasaporte = Entry(etiqueta)
        self.pasaporte.pack()

        self.boton = tk.Button(etiqueta, text = 'Enviar', font= ("Bahnschrift Light",10), )
        self.boton.pack()

        var1 = IntVar()
        self.check = Checkbutton(etiqueta, text="male", variable=var1)
        self.check.pack()

        var2 = IntVar()
        self.check = Checkbutton(etiqueta, text="female", variable=var2)
        self.check.pack()


        ventana.mainloop()

    #     self.obtener_usuario()
    #
    # def correo_peticion(self, peticion, parametros = ()):
    #     with sqlite3.connect(self.db_nombre) as conn:
    #         cursor = conn.cursor()
    #         resultados = cursor.execute(peticion, parametros)
    #         conn.commit()
    #     return resultados
    #
    # def obtener_usuario(self):
    #     peticion = 'SELECT * FROM usuarios ORDER BY nombre DESC'
    #     db_filas = self.correo_peticion(peticion)
    #     print(db_filas)
