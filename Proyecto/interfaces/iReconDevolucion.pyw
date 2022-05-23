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
        tk.Button(frame, text="No reconoce",
                  command=self.mensajeError).place(relx=0.40, rely=0.60)
        tk.Button(frame, text="Si reconoce",
                  command=self.siguienteInterfaz).place(relx=0.60, rely=0.60)

        window.mainloop()

    def mensajeError(self):
        messagebox.showinfo("Error", "No se reconoce el rostro")

    def siguienteInterfaz(self):
        self.wind.withdraw()
        ventana = VentanaDevolucion(Tk())
        #Conexion con siguiente interfaz
