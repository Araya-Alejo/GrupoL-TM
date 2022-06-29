'''
    Interfaz grafica que contiene dos caminos "Registrarse" o "Iniciar sesion"
    cada una de ellas te deribarar a sus interfaces respetivamente

    @author Araya
'''
# ------------------------------------------------------------------------------
from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import messagebox
# import entidades.usuario as usuario
import sqlite3
from interfaces.iUsuario import VentanaUsuario
from interfaces.iReconIngUsuario import ReconIniciar

class  VentanaInicioSesion:
    # db_nombre = 'database.db'
    def llamadaVentanaUsuario(self):
        ventana = VentanaUsuario(Tk(), self.parametroMatricula)

    def __init__(self, ventana, matricula):
        self.ventana = ventana
        self.parametroMatricula = matricula
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()
        ancho2 = 800
        alto2 = 600
        izquierda = (ancho - ancho2) / 2
        arriba = (alto - alto2) / 2
        self.ventana.geometry("%dx%d+%d+%d" % (ancho2, alto2, izquierda, arriba))
        self.ventana.title("Iniciar Sesion")
        self.ventana.resizable(False, False)

        area = Frame(ventana)
        area.pack(expand = TRUE, fill = 'both')

        self.boton1 = tk.Button(area, text = 'Registrarse', font= ("Bahnschrift Light",10), command= self.llamadaVentanaUsuario )
        self.boton1.place(relx = .3, rely=.5)

        self.boton2 = tk.Button(area, text = 'Iniciar sesion', font= ("Bahnschrift Light",10), command = self.siguientePantalla)
        self.boton2.place(relx = .6, rely=.5)


        ventana.mainloop()

    def siguientePantalla(self):
        self.ventana.withdraw()
        obj = ReconIniciar(Tk(), self.parametroMatricula)
