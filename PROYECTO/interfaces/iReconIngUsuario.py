import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from interfaces.iNdexPago import Pago
from servicios.reconocimientoFacial import capturarImagenIngreso


class ReconIniciar:

    def __init__(self, root, matricula):
        # Ventana
        self.root = root
        self.matricula = matricula
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        width = 500
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        root.geometry("%dx%d+%d+%d" % (width, height, left, top))
        root.title("Iniciar Sesión")
        root.resizable(False, False)

        self.initComponents(root)

    '''
        Procedimiento que inicializa los componentes gráficos.
    '''
    def initComponents(self, root):
        # Frame
        frame1 = Frame(root, width="300", height="50")
        frame1.pack(expand=False, fill="both")

        frame2 = Frame(root, width="300", height="250")
        frame2.pack(expand=False, fill="both")

        # Label
        Label(frame1, text="Iniciar Sesión", font=("Bahnschrift SemiLight", 20)).place(x=250 ,y=25, anchor="center")
        Label(frame2, text="CUIL:", font=("Bahnschrift Light", 12)).place(x=25, y=20)

        # Entry
        self.idCuil = Entry(frame2, width=20)
        self.idCuil.place(x=100, y=20, height=25)
        self.idCuil.focus_force()

        # Button
        Button(frame2, text="Volver", command=self.actionVolver).place(x=50, y=150, anchor="center")
        Button(frame2, text="Capturar Rostro", command=self.validarUsuario).place(x=250, y=100, anchor="center", width=200, height=50)

        root.mainloop()

    def actionVolver(self):
        self.root.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj=Ventana1(Tk())

    def validarUsuario(self):
        if (self.idCuil.get()):
            datoCuil =self.idCuil.get()
            if (self.searchEnAlquiler()):
                messagebox.showwarning(
                    "Usuario sin operacion", "Ya tiene un auto en alquiler")
                self.idCuil.focus()
            else:
                if (capturarImagenIngreso(self.idCuil.get())) :
                    self.wind.withdraw()
                    ventana = Pago(Tk(), datoCuil, self.matricula)
                else:
                    messagebox.showwarning("Usuario sin operacion", "Ya tiene un auto en alquiler")
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.idCuil.focus()

    def searchUsuario(self):
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        idCuil = self.idCuil.get()
        cur.execute(
            "SELECT Cuil FROM Usuarios WHERE Cuil=?", (idCuil,))
        datos = cur.fetchall()
        con.close()
        return datos

    def searchEnAlquiler(self):
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        idCuil = self.idCuil.get()
        cur.execute("SELECT IdCuil FROM Alquileres WHERE IdCuil=?", (idCuil,))
        datos = cur.fetchall()
        con.close()
        return datos
