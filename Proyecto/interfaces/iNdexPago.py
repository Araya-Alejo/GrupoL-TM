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
        tk.Label(frame, text="DATOS DEL ALQUILER").place(            relx=0.40, rely=0.0)
        tk.Label(frame, text="Cuil:").place(                         relx=0.01, rely=0.05)
        tk.Label(frame, text="Nombre y Apellido:").place(            relx=0.01, rely=0.10)
        tk.Label(frame, text="Correo").place(                        relx=0.01, rely=0.15)
        tk.Label(frame, text="Marca:").place(                        relx=0.01, rely=0.20)
        tk.Label(frame, text="Modelo:").place(                       relx=0.01, rely=0.25)
        tk.Label(frame, text="Matricula del auto alquilado:").place( relx=0.01, rely=0.30)
        tk.Label(frame, text="Fecha del Alquiler:").place(           relx=0.01, rely=0.35)
        tk.Label(frame, text="Precio del alquiler por dia:").place(  relx=0.01, rely=0.40)
        tk.Label(frame, text="Cantidad de dias del alquiler:").place(relx=0.01, rely=0.45)
        tk.Label(frame, text="Precio Total").place(                  relx=0.01, rely=0.50)
        #Creacion de los Botones
        tk.Button(frame, text="PAGO",command=self.verPago).place(               relx=0.05, rely=0.60)
        tk.Button(frame, text="SIGUIENTE",command=self.siguienteInterfaz).place(relx=0.80, rely=0.80)
        #tk.Button(frame, text="A",command=self.atras).place(                    relx=0.01, rely=0.9)


        window.mainloop()

        """
        self.idMatricula = ""

        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)                                          # mi conexion   con
        cursorAlq = con.cursor()                                                # mi cursor     cursorAlq
        cursorAlq.execute("SELECT * FROM Alquileres WHERE idCuil=?", (idCuil,)) # ejecutar alquiereles--idcuil
        recordsAlq= cursorAlq.fetchall()

        for row in recordsAlq:
            self.idMatricula = ""+row[1]
            self.L1 = tk.Label(frame, text= row[0]).place(           relx=0.4, rely=0.05)
            self.L5 = tk.Label(frame, text= row[1]).place(           relx=0.4, rely=0.20)
            self.L6 = tk.Label(frame, text= row[2]).place(           relx=0.4, rely=0.30)
            self.L7 = tk.Label(frame, text= row[3]).place(           relx=0.4, rely=0.35)
            self.L8 = tk.Label(frame, text= row[4]).place(           relx=0.4, rely=0.40)
            self.L9 = tk.Label(frame, text=(row[3]*row[4])).place(   relx=0.4, rely=0.45)

        cursorUser = con.cursor()                                               # mi cursor     cursorUser
        cursorUser.execute("SELECT * FROM Usuarios WHERE Cuil=?", (idCuil,))    # ejecutar Usuarios--Cuil
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


    def verPago(self):
        self.verPago = Toplevel()
        self.verPago.title("PAGO")
        screenWidth = self.verPago.winfo_screenwidth()
        screenHeight = self.verPago.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 400
        # Establece altura de la ventana.
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.verPago.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.verPago.resizable(0, 0)

        #Creacion del Frame
        frameVerPago = LabelFrame(self.verPago)
        frameVerPago.place(relwidth=1, relheight=1)

        #Creacion de los Label
        tk.Label(frameVerPago, text="Ingrese Codigo de Verificación:").place(
            relx=0.30, rely=0.3)

        #Crecion de los Textbox
        self.codigoVer = tk.Entry(frameVerPago)
        self.codigoVer.focus()
        self.codigoVer.place(relx=0.50, rely=0.3)

        #Creacion del Botones
        tk.Button(frameVerPago, text="Validar",
                  command=self.validarPago).place(relx=0.50, rely=0.5)
        tk.Button(frameVerPago, text="Atras",
                  command=self.verPago.withdraw).place(relx=0.01, rely=0.01)

    def validarPago(self):
        if (self.codigoVer.get()):
            if (self.codigoVer.get() == "123"):  # Valida el codigo ingresado con el codigo tecnico
                messagebox._show("Pago", "Codigo Aceptado")
                self.verPago.withdraw()
            else:
                messagebox.showwarning("Pago", "Codigo Erroneo")
                self.codigoVer.focus()
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.codigoVer.focus()

    def siguienteInterfaz(self):
        self.wind.withdraw()
        #Conexion con siguiente interfaz


app = Pago(Tk())
