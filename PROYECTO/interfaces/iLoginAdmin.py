from tkinter import ttk
from tkinter import *


from interfaces.iControlStock import VentanaControlStock
import sqlite3
from tkinter import messagebox

class LoginAdministrador:

    def __init__(self, window):
        self.ventanaAdmin = window
        self.ventanaAdmin.title("Ingreso de Administradores")
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
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
        self.contrasena = ttk.Entry(frameLoginAdmin, show="*")
        self.contrasena.place(relx=0.50, rely=0.4)

        #Creacion del Boton Validar
        ttk.Button(frameLoginAdmin, text="Validar",
                command=self.validar).place(relx=0.50, rely=0.5)
        ttk.Button(frameLoginAdmin, text="Atras",
               command=self.volver).place(relx=0.01, rely=0.01)

        window.mainloop()

    def volver(self):
        self.ventanaAdmin.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj= Ventana1(Tk())

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
