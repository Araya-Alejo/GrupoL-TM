import tkinter as tk
from tkinter import Tk, Frame, Label, Button, Entry, ttk, messagebox

import sqlite3
from tkinter import messagebox
from functools import partial


class VentanaDevolucion:

    def __init__(self, window, idCuil):
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
        frame = ttk.LabelFrame(self.wind)
        frame.place(relwidth=1, relheight=1)

        #Creacion de los Label de etiqueta
        ttk.Label(frame, text="DATOS DEL ALQUILER").place(relx=0.40, rely=0.0)
        ttk.Label(frame, text="Cuil:").place(relx=0.01, rely=0.05)
        ttk.Label(frame, text="Nombre y Apellido:").place(
            relx=0.01, rely=0.10)
        ttk.Label(frame, text="Marca:").place(relx=0.01, rely=0.25)
        ttk.Label(frame, text="Modelo:").place(relx=0.01, rely=0.15)
        ttk.Label(frame, text="Matricula del auto alquilado:").place(
            relx=0.01, rely=0.20)
        ttk.Label(frame, text="Fecha del Alquiler:").place(
            relx=0.01, rely=0.30)
        ttk.Label(frame, text="Cantidad de dias del alquiler:").place(
            relx=0.01, rely=0.35)
        ttk.Label(frame, text="Precio del alquiler por dia:").place(
            relx=0.01, rely=0.40)
        ttk.Label(frame, text="Precio Total").place(
            relx=0.01, rely=0.45)
        labelValidacion = ttk.Label(frame, text="hola").place(
            relx=0.30, rely=0.60)

        self.idMatricula = ""
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cursorAlq = con.cursor()
        cursorAlq.execute("SELECT * FROM Alquileres WHERE idCuil=?", (idCuil,))
        recordsAlq= cursorAlq.fetchall()
        for row in recordsAlq:
            self.idMatricula = ""+row[1]
            self.L1 = ttk.Label(frame, text= row[0]).place(relx=0.4, rely=0.05)
            self.L5 = ttk.Label(frame, text=row[1]).place(
                relx=0.4, rely=0.20)
            self.L6 = ttk.Label(frame, text=row[2]).place(
                relx=0.4, rely=0.30)
            self.L7 = ttk.Label(frame, text=row[3]).place(
                relx=0.4, rely=0.35)
            self.L8 = ttk.Label(frame, text=row[4]).place(
                relx=0.4, rely=0.40)
            self.L9 = ttk.Label(frame, text=(row[3]*row[4])).place(
                relx=0.4, rely=0.45)

        cursorUser = con.cursor()
        cursorUser.execute("SELECT * FROM Usuarios WHERE Cuil=?", (idCuil,))
        recordsUser= cursorUser.fetchall()
        for row in recordsUser:
            self.L2 = ttk.Label(frame, text= row[0]+" "+row[1]).place(relx=0.4, rely=0.10)


        cursorVehiculo = con.cursor()
        cursorVehiculo.execute("SELECT * FROM vehiculos WHERE matricula=?", (self.idMatricula,))
        recordsVehiculo= cursorVehiculo.fetchall()
        for row in recordsVehiculo:
            self.L3 = ttk.Label(frame, text=row[1]).place(relx=0.4, rely=0.25)
            self.L4 = ttk.Label(frame, text=row[2]).place(relx=0.4, rely=0.15)

        con.close()

        #Creacion de los Botones
        ttk.Button(frame, text="VERIFICACIÓN TÉCNICA",
                  command=self.verTecnica).place(relx=0.05, rely=0.60)
        ttk.Button(frame, text="SIGUIENTE",
                  command=self.siguienteInterfaz).place(relx=0.80, rely=0.80)
        ttk.Button(frame, text="Atras",
                   command=self.atras).place(relx=0.01, rely=0.9)

        window.mainloop()

    def atras(self):
        self.wind.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj= Ventana1(Tk())

    def verTecnica(self):
        self.verTec = Toplevel()
        self.verTec.title("Ingreso de Administradores")
        screenWidth = self.verTec.winfo_screenwidth()
        screenHeight = self.verTec.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 400
        # Establece altura de la ventana.
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.verTec.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.verTec.resizable(0, 0)

        #Creacion del Frame
        frameVerTec = ttk.LabelFrame(self.verTec)
        frameVerTec.place(relwidth=1, relheight=1)

        #Creacion de los Label
        ttk.Label(frameVerTec, text="Ingrese Codigo de Verificación:").place(
            relx=0.30, rely=0.3)

        #Crecion de los Textbox
        self.codigoVer = ttk.Entry(frameVerTec)
        self.codigoVer.focus()
        self.codigoVer.place(relx=0.50, rely=0.3)

        #Creacion del Botones
        ttk.Button(frameVerTec, text="Validar",
                  command=self.validarTec).place(relx=0.50, rely=0.5)
        ttk.Button(frameVerTec, text="Atras",
                  command=self.verTec.withdraw).place(relx=0.01, rely=0.01)

    def validarTec(self):
        if (self.codigoVer.get()):
            if (self.codigoVer.get() == "123"):  # Valida el codigo ingresado con el codigo tecnico
                messagebox._show("Validación Técnica", "Codigo Aceptado")
                self.verTec.withdraw()
            else:
                messagebox.showwarning("Validación Técnica", "Codigo Erroneo")
                self.codigoVer.focus()
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.codigoVer.focus()

    def siguienteInterfaz(self):
        self.wind.withdraw()
        #Conexion con siguiente interfaz
