from tkinter import ttk
from tkinter import *
#import iControlStock
import sqlite3


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

        #Creacion del Frame
        frame = LabelFrame(self.wind, text="ALQUILA YA!!!")
        frame.place(relwidth=1, relheight=1)

        #Creacion de Botones
        ttk.Button(frame, text="Alquilar", command=self.alquilar).place(
            relx=0.35, rely=0.4)
        ttk.Button(frame, text="Devolución", command=self.devolucion).place(
            relx=0.55, rely=0.4)
        ttk.Button(frame, text="Ingreso de Administradores",
                   command=self.loginAdmin).place(relx=0.80, rely=0.01)

    def loginAdmin(self):
        self.ventanaAdmin = Toplevel()
        self.ventanaAdmin.title("Ingreso de Administradores")
        screenWidth = self.ventanaAdmin.winfo_screenwidth()
        screenHeight = self.ventanaAdmin.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 400
        # Establece altura de la ventana.
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.ventanaAdmin.geometry("%dx%d+%d+%d" % (width, height, left, top))

        #Creacion del Frame
        frameLoginAdmin = LabelFrame(self.ventanaAdmin)
        frameLoginAdmin.place(relwidth=1, relheight=1)

        #Creacion de los Label
        ttk.Label(frameLoginAdmin, text="Usuario:").place(relx=0.30, rely=0.3)
        ttk.Label(frameLoginAdmin, text="Contraseña:").place(
            relx=0.30, rely=0.4)

        #Crecion de los Textbox
        self.usuario = ttk.Entry(frameLoginAdmin)
        self.usuario.focus()
        self.usuario.place(relx=0.50, rely=0.3)
        self.contrasena = ttk.Entry(frameLoginAdmin)
        self.contrasena.place(relx=0.50, rely=0.4)

        #Creacion del Boton Validar
        ttk.Button(frameLoginAdmin, text="Validar",
                   command=self.validar).place(relx=0.50, rely=0.5)

    def validar(self):
        self.wind.withdraw()
        self.ventanaAdmin.withdraw()
        #conexion a iControlStock

    def alquilar(self):
        self.wind.withdraw()
        #conexion a interface de Alquilar

    def devolucion(self):
        self.wind.withdraw()
        #conexion a interface de Devolucion


window = Tk()
application = Ventana1(window)
window.mainloop()
