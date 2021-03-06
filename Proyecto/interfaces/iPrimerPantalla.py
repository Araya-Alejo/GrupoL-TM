'''
    Interfaz grafica para ingresar los atributos del usuario
    @author Vargas
'''

from tkinter import ttk
from tkinter import *

from interfaces.iReconDevolucion import ReconDev
import sqlite3
from interfaces.iIniciarSesion import VentanaInicioSesion
from tkinter import messagebox
from interfaces.iLoginAdmin import LoginAdministrador
from interfaces.iAlquilar import VentanaAlquilar

class Ventana1:

    def __init__(self, window):
        self.wind = window
        self.wind.title("Alquila Ya")
        # Obtiene ancho del área de visualización.
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 800
        # Establece altura de la ventana.
        height = 600
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.wind.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.wind.resizable(0, 0)

        #Creacion del Frame
        frame = LabelFrame(self.wind)
        frame.place(relwidth=1, relheight=1)

        #Creacion de Botones
        ttk.Button(frame, text="Alquilar", command=self.llamadaInicioDeSesion).place(
            relx=0.35, rely=0.4)
        ttk.Button(frame, text="Devolución", command=self.devolucion).place(
            relx=0.55, rely=0.4)
        ttk.Button(frame, text="Ingreso de Administradores",
                   command=self.loginAdmin).place(relx=0.05, rely=0.01)


        window.mainloop()

    def loginAdmin(self):
        self.wind.withdraw()
        obj = LoginAdministrador(Tk())

    def llamadaInicioDeSesion(self):
        self.wind.withdraw()
        ventana = VentanaAlquilar(Tk())
        #conexion con inicio de sesion de usuario

    def devolucion(self):
        self.wind.withdraw()
        ventana = ReconDev(Tk())




#prueba de modificacion
