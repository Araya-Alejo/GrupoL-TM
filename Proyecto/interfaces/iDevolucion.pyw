import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox


class VentanaDevolucion:

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

        #Creacion de los Label
        tk.Label(frame, text="DATOS DEL ALQUILER").place(relx=0.40, rely=0.0)
        tk.Label(frame, text="Usuario:").place(relx=0.01, rely=0.05)
        tk.Label(frame, text="Fecha del Alquiler:").place(
            relx=0.01, rely=0.10)
        tk.Label(frame, text="Marca:").place(relx=0.01, rely=0.25)
        tk.Label(frame, text="Modelo:").place(relx=0.01, rely=0.15)
        tk.Label(frame, text="Matricula del auto alquilado:").place(
            relx=0.01, rely=0.20)
        tk.Label(frame, text="Precio de alquiler:").place(
            relx=0.01, rely=0.30)
        tk.Label(frame, text="Cantidad de dias del alquiler:").place(
            relx=0.01, rely=0.35)

        #Creacion de los Botones
        tk.Button(frame, text="VERIFICACIÓN TÉCNICA",
                  command=self.verTecnica).place(relx=0.05, rely=0.45)
        tk.Button(frame, text="SIGUIENTE",
                  command=self.siguienteInterfaz).place(relx=0.80, rely=0.80)
        tk.Button(frame, text="Mostrar Datos",
                  command=self.mostrarDatos).place(relx=0.90, rely=0.9)

        window.mainloop()

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
        frameVerTec = LabelFrame(self.verTec)
        frameVerTec.place(relwidth=1, relheight=1)

        #Creacion de los Label
        tk.Label(frameVerTec, text="Ingrese Codigo de Verificación:").place(
            relx=0.30, rely=0.3)

        #Crecion de los Textbox
        self.codigoVer = tk.Entry(frameVerTec)
        self.codigoVer.focus()
        self.codigoVer.place(relx=0.50, rely=0.3)

        #Creacion del Botones
        tk.Button(frameVerTec, text="Validar",
                  command=self.validarTec).place(relx=0.50, rely=0.5)
        tk.Button(frameVerTec, text="Atras",
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

    def mostrarDatos(self):
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute('SELECT * FROM Usuarios')
        data = cur.fetchall()
        print(data[0])
        for row in data:
            print(row)
        #for row in cur.execute("SELECT Nombre FROM Usuarios;"):
        #    print(row)

        con.close()
