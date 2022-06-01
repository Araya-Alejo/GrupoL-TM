import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from interfaces.iDevolucion import VentanaDevolucion


class ReconDev:
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

        #Label
        tk.Label(frame, text="EN ESTA INTERFAZ RECONOCERIA EL ROSTRO").place(
            relx=0.40, rely=0.4)

        #Creacion de los Botones
        tk.Button(frame, text="Reconocimiento",
                  command=self.validarUsuario).place(relx=0.40, rely=0.60)

        #Crecion de Entry
        self.idCuil = tk.Entry(frame)
        self.idCuil.focus()
        self.idCuil.place(relx=0.50, rely=0.3)

        window.mainloop()

    def validarUsuario(self):
        if (self.idCuil.get()):
            dato =self.idCuil.get()
            if (dato):
                self.wind.withdraw()
                ventana = VentanaDevolucion(Tk(), dato)
            else:
                messagebox.showwarning(
                    "Usuario sin operacion", "No hay alquileres pendientes para este usuario")
                self.idCuil.focus()
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
            "SELECT IdCuil FROM Alquileres WHERE IdCuil=?", (idCuil,))
        datos = cur.fetchall()
        con.close()
        return datos
