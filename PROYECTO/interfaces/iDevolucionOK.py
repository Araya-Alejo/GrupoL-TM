import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from functools import partial
from interfaces.ESTANDARES import *


class VentanaDevOk:

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
        frame = tk.Frame(self.wind)
        frame.place(relwidth=1, relheight=1)

        #Creacion de los Label de etiqueta
        tk.Label(frame, text="DEVOLUCIÓN REALIZADA").place(relx=0.40, rely=0.0)

        self.labelValidacion = tk.Label(frame, text="A continuacion se le enviará un email informando la confirmacion de la Devolución", fg="red").place(relx=0.40, rely=0.60)
        self.Verificacion = False

        self.idMatricula = ""
        #Creacion de los Botones
        tk.Button(frame, text="Salir",
                  command=self.siguienteInterfaz).place(relx=0.80, rely=0.80)
        tk.Button(frame, text="Volver a Pagina de inicio",
                   command=self.atras).place(relx=0.01, rely=0.9)

        #self.cambiosEnBD(idCuil)
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cursorAlq = con.cursor()
        cursorAlq.execute("SELECT * FROM Alquileres WHERE idCuil=?", (idCuil,))
        recordsAlq= cursorAlq.fetchall()
        for row in recordsAlq:
            self.idMatricula = ""+row[1]
            row[5]="DEVUELTO"

        cursorVehiculo = con.cursor()
        cursorVehiculo.execute("SELECT * FROM vehiculos WHERE matricula=?", (self.idMatricula,))
        recordsVehiculo= cursorVehiculo.fetchall()
        for row in recordsVehiculo:
            row[7]=0

        con.close()

        window.mainloop()

    def atras(self):
        self.wind.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj= Ventana1(Tk())

    def siguienteInterfaz(self):
        self.wind.destroyAllWindows()

        #Conexion con siguiente interfaz
