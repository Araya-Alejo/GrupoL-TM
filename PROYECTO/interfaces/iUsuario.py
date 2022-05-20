from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import messagebox
import entidades.usuario as usuario
import subprocess
from TyC import *
from interfaces.iCalendar import *
import sqlite3

class  VentanaUsuario:
    db_nombre = 'database.db'

    def llamarVentanaCalendario(self):
        ventana = VentanaCalendario(Tk())

    def abrirPDF(self):
        path = 'TyC\AlquilaYa_TerminosyCondiciones.pdf'
        subprocess.Popen([path], shell=True)

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


        area = Frame(ventana, pady=20)
        area.pack(expand=True, fill=tk.BOTH)

        self.nombre = Label(area, text = 'Nombre', font= ("Bahnschrift Light",10))
        self.nombre.pack(fill=tk.BOTH)
        self.nombre = Entry(area)
        self.nombre.pack(pady = 5)

        self.apellido =Label(area, text = 'Apellido', font= ("Bahnschrift Light",10))
        self.apellido.pack(fill=tk.BOTH)
        self.apellido = Entry(area)
        self.apellido.pack(pady = 5)

        self.carnetConducir =Label(area, text = 'Carnet de Conducir', font= ("Bahnschrift Light",10))
        self.carnetConducir.pack(fill=tk.BOTH)
        self.carnetConducir = Entry(area)
        self.carnetConducir.pack(pady = 5)

        self.fechaNacimiento =Label(area, text = 'Fecha de nacimiento', font= ("Bahnschrift Light",10))
        self.fechaNacimiento.pack(fill=tk.BOTH)
        self.fechaNacimiento = Entry(area)
        self.fechaNacimiento.pack()
        self.botonCalendar = tk.Button(area, text = 'Seleccionar fecha', font= ("Bahnschrift Light",10),command = self.llamarVentanaCalendario)
        self.botonCalendar.pack()

        self.correo =Label(area, text = 'Correo', font= ("Bahnschrift Light",10))
        self.correo.pack(fill=tk.BOTH)
        self.correo = Entry(area)
        self.correo.pack(pady = 5)

        self.extrangero =Label(area, text = 'Es extrangero?', font= ("Bahnschrift Light",10))
        self.extrangero.pack(fill=tk.BOTH)
        self.extrangero = Entry(area)
        self.extrangero.pack(pady = 5)

        self.cuil =Label(area, text = 'CUIL', font= ("Bahnschrift Light",10))
        self.cuil.pack(fill=tk.BOTH)
        self.cuil = Entry(area)
        self.cuil.pack(pady = 5)

        self.pasaporte =Label(area, text = 'Pasaporte', font= ("Bahnschrift Light",10))
        self.pasaporte.pack(fill=tk.BOTH)
        self.pasaporte = Entry(area)
        self.pasaporte.pack(pady = 5)



        self.boton = tk.Button(area, text = 'T&C', font= ("Bahnschrift Light",10), command = self.abrirPDF )
        self.boton.pack(pady = 5)

        var1 = IntVar()
        self.check = Checkbutton(area, text="Termino y condiciones", variable=var1)
        self.check.pack()

        self.boton = tk.Button(area, text = 'Enviar', font= ("Bahnschrift Light",10),command = exit )
        self.boton.pack(pady = 20)



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
