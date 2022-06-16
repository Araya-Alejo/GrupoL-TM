import tkinter as tk  # biblioteca para diseniar interfaz
from tkinter import *  # botones tablas .. etc
#from servicios.conexionPago import Conexion
import sqlite3  # modulo para conexion
from tkinter import messagebox

# clase pago va a tener todos los metodos de mi ventana (titulo botones, entradas dde texto) funcionalidad de nuestras ventanas


class Pago:

    def boton(self):
        ventana2 = Conexion(Tk())

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

        #Creacion de los Label de etiqueta
        tk.Label(frame, text="DATOS DEL ALQUILER").place(relx=0.40, rely=0.0)
        tk.Label(frame, text="Cuil:").place(relx=0.01, rely=0.05)
        tk.Label(frame, text="Nombre y Apellido:").place(
            relx=0.01, rely=0.10)
        tk.Label(frame, text="Correo").place(
            relx=0.01, rely=0.15)
        tk.Label(frame, text="Marca:").place(relx=0.01, rely=0.20)
        tk.Label(frame, text="Modelo:").place(relx=0.01, rely=0.25)
        tk.Label(frame, text="Matricula del auto alquilado:").place(
            relx=0.01, rely=0.30)
        tk.Label(frame, text="Fecha del Alquiler:").place(
            relx=0.01, rely=0.35)
        tk.Label(frame, text="Precio del alquiler por dia:").place(relx=0.01, rely=0.40)
        tk.Label(frame, text="Cantidad de dias del alquiler:").place(
            relx=0.01, rely=0.45)
        tk.Label(frame, text="Precio Total").place(
            relx=0.01, rely=0.50)
        #Creacion de los Botones

        tk.Button(frame, text="CONFIRMAR",
                  command=self.siguienteInterfaz).place(relx=0.80, rely=0.80)

        window.mainloop()

        """
        self.idMatricula = ""
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cursorAlq = con.cursor()
        cursorAlq.execute("SELECT * FROM Alquileres WHERE idCuil=?", (idCuil,))
        recordsAlq= cursorAlq.fetchall()
        for row in recordsAlq:
            self.idMatricula = ""+row[1]
            self.L1 = tk.Label(frame, text= row[0]).place(relx=0.4, rely=0.05)
            self.L5 = tk.Label(frame, text=row[1]).place(
                relx=0.4, rely=0.20)
            self.L6 = tk.Label(frame, text=row[2]).place(
                relx=0.4, rely=0.30)
            self.L7 = tk.Label(frame, text=row[3]).place(
                relx=0.4, rely=0.35)
            self.L8 = tk.Label(frame, text=row[4]).place(
                relx=0.4, rely=0.40)
            self.L9 = tk.Label(frame, text=(row[3]*row[4])).place(
                relx=0.4, rely=0.45)

        cursorUser = con.cursor()
        cursorUser.execute("SELECT * FROM Usuarios WHERE Cuil=?", (idCuil,))
        recordsUser= cursorUser.fetchall()
        for row in recordsUser:
            self.L2 = tk.Label(frame, text= row[0]+" "+row[1]).place(relx=0.4, rely=0.10)


        cursorVehiculo = con.cursor()
        cursorVehiculo.execute("SELECT * FROM vehiculos WHERE matricula=?", (self.idMatricula,))
        recordsVehiculo= cursorVehiculo.fetchall()
        for row in recordsVehiculo:
            self.L3 = tk.Label(frame, text=row[1]).place(relx=0.4, rely=0.25)
            self.L4 = tk.Label(frame, text=row[2]).place(relx=0.4, rely=0.15)

        con.close()
        """

        #tk.Button(frame, text="Atras",
        #           command=self.atras).place(relx=0.01, rely=0.9)





    def siguienteInterfaz(self):
        self.wind.withdraw()
        #Conexion con siguiente interfaz



app = Pago(Tk())
