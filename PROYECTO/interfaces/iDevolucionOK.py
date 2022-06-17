import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from functools import partial
from interfaces.ESTANDARES import *
from servicios.mail import *
from servicios.SO import *


class VentanaDevOk:

    def __init__(self, window, idCuil, idMatricula, mensaje, email):
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
        tk.Label(frame, text="DEVOLUCIÓN REALIZADA").place(relx=0.40, rely=0.40)

        self.labelValidacion = tk.Label(frame, text="A continuacion se le enviará un email informando la confirmacion de la Devolución").place(relx=0.2, rely=0.50)

        self.cambiosEnBD(idCuil, idMatricula)
        ENVIAR_CORREO(mensaje, email)

        self.idMatricula = ""
        #Creacion de los Botones
        tk.Button(frame, text="Salir",
                  command=window.destroy).place(relx=0.60, rely=0.70)
        tk.Button(frame, text="Volver a Pagina de inicio",
                   command=self.atras).place(relx=0.30, rely=0.7)



        window.mainloop()

    def atras(self):
        self.wind.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj= Ventana1(Tk())

    def cambiosEnBD(self,idCuil, idMatricula):
        try:
            db_name = "base_datos/databaseGeneral.sqlite3"
            con = sqlite3.connect(db_name)
            cursorAlq = con.cursor()
            cursorAlq.execute("DELETE FROM Alquileres WHERE IdCuil=?", (idCuil,))
            con.commit()

            cursorVehiculo = con.cursor()
            estadoV =0
            cursorVehiculo.execute("UPDATE vehiculos SET estaAlquilado=? WHERE matricula=?", (estadoV , idMatricula,))
            con.commit()

            con.close()
        except Exception:
            MENSAJE_ERROR("HAY UN ERROR AL MODIFICAR LOS DATOS")
