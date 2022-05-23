from tkinter import ttk
from tkinter import *
from interfaces.iReconDevolucion import ReconDev
from interfaces.iDevolucion import VentanaDevolucion
from interfaces.iControlStock import VentanaControlStock
import sqlite3
from interfaces.iUsuario import VentanaUsuario
from interfaces.iIniciarSesion import VentanaInicioSesion
from tkinter import messagebox


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
        self.ventanaAdmin.resizable(0, 0)

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
        ttk.Button(frameLoginAdmin, text="Atras",
                   command=self.ventanaAdmin.withdraw).place(relx=0.01, rely=0.01)

    def searchUsuarioCont(self):
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        usuario = self.usuario.get()
        contrasena = self.contrasena.get()
        cur.execute(
            "SELECT IDUsuario FROM Administradores WHERE IDUsuario=? AND Contrasena=?", (usuario, contrasena))
        datos = cur.fetchall()
        con.close()
        return datos

    def validar(self):
        if (self.usuario.get()):
            if (self.searchUsuarioCont()):
                self.wind.withdraw()
                self.ventanaAdmin.withdraw()
                ventana = VentanaControlStock(Tk())
            else:
                messagebox.showwarning(
                    "Error de credenciales", "Datos incorrectos")
                self.usuario.focus()
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.usuario.focus()
        #conexion a iControlStock

    def llamadaInicioDeSesion(self):
        self.wind.withdraw()
        ventana = VentanaInicioSesion(Tk())
        #conexion con inicio de sesion de usuario

    def devolucion(self):
        self.wind.withdraw()
        ventana = ReconDev(Tk())
        #Se hace la conexion a la interfaz de devolucion para continuar trabajando
        #Primero va la conexion a la interfaz de la verificacion por reconocimiento facial
        #y luego a la interfaz de devolucion si el reconocimiento facial da True


window = Tk()
application = Ventana1(window)
window.mainloop()
