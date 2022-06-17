import tkinter as tk  # biblioteca para diseniar interfaz
from tkinter import *  # botones tablas .. etc
#from servicios.conexionPago import Conexion
import sqlite3  # modulo para conexion
from tkinter import messagebox
from functools import partial
from datetime import datetime # fecha de hoy
from interfaces.iConfirmacion import ConfirPago

from interfaces.ESTANDARES import *

# clase pago va a tener todos los metodos de mi ventana (titulo botones, entradas dde texto) funcionalidad de nuestras ventanas


class Pago:



    def __init__(self, window, idCuil):
        self.wind = window
        self.wind.title("VENTANA PAGO")



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
        frame.config(bg="light green")  # color fondo

        #Creacion de los Label de etiqueta
        tk.Label(frame, text="DATOS DEL ALQUILER").place(            relx=0.40, rely=0.0)
        tk.Label(frame, text="Nombre y Apellido:").place(            relx=0.01, rely=0.05)
        tk.Label(frame, text="Cuil:").place(                         relx=0.01, rely=0.10)
        tk.Label(frame, text="Correo").place(                        relx=0.01, rely=0.15)
        tk.Label(frame, text="Marca:").place(                        relx=0.01, rely=0.20)
        tk.Label(frame, text="Modelo:").place(                       relx=0.01, rely=0.25)
        tk.Label(frame, text="Matricula del auto alquilado:").place( relx=0.01, rely=0.30)
        tk.Label(frame, text="Precio del alquiler por dia:").place(  relx=0.01, rely=0.35)
        tk.Label(frame, text="Fecha del Alquiler:").place(           relx=0.01, rely=0.40)      #pongo yo   (HACER)
        tk.Label(frame, text="Cantidad de dias del alquiler:").place(relx=0.01, rely=0.45)      # (CAJA DE TEXTO)
        tk.Label(frame, text="Precio Total").place(                  relx=0.01, rely=0.50)      # sacarlo (PRECIO ALQUILER X DIA    X     CANTIDAD DE DIAS QUE QUIERAN ALQUILAR )

        # caja de Texto
        self.boxDiasDeAlquiler = tk.Entry(frame)
        self.boxDiasDeAlquiler.focus()
        self.boxDiasDeAlquiler.place(                                relx=0.4, rely=0.45)

        self.fecha = str(datetime.today().strftime('%d-%m-%Y'))
        tk.Label(frame, text=self.fecha).place(                      relx=0.4, rely=0.40)      # posicion fecha

        self.Verificacion = False                                                               # true false

        #Creacion de los Botones
        tk.Button(frame, text="PAGO",command=partial(self.verPago,frame)).place(                                  relx=0.40, rely=0.60)
        tk.Button(frame, text="SIGUIENTE",command=partial(self.siguienteInterfaz, frame)).place(                  relx=0.80, rely=0.80)
        tk.Button(frame, text="CALCULAR TOTAL",command = partial(self.calcularTOTAL,frame)).place(                relx=0.60, rely=0.45)   #tasar
        #tk.Button(frame, text="A",command=self.atras).place(                                                    relx=0.01, rely=0.9)

        """
        ------------****************BASE DE DATOS******************----------------------------------------------------------------------------------------------OPEN---
        """
        self.idMatricula = "AA222BB"

        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)                                                          # mi conexion   con
        cursorUser = con.cursor()                                                               # mi cursor                             #----USUARIO
        cursorUser.execute("SELECT * FROM Usuarios WHERE Cuil=?", (idCuil,))                    # ejecutar Usuarios--Cuil
        recordsUser= cursorUser.fetchall()
        for row in recordsUser:
            self.nombreApellido = tk.Label(frame, text= row[0]+" "+row[1]).place(relx=0.4, rely=0.05)
            self.cuil = tk.Label(          frame, text= row[5]).place(           relx=0.4, rely=0.10)
            self.numeroCUIL = row[5]
            self.correo = tk.Label(        frame, text= row[4]).place(           relx=0.4, rely=0.15)

        cursorVehiculo = con.cursor()                                                                                                   #---VEHICULO
        cursorVehiculo.execute("SELECT * FROM vehiculos WHERE matricula=?", (self.idMatricula,))
        recordsVehiculo= cursorVehiculo.fetchall()
        for row in recordsVehiculo:
            self.marca = tk.Label(          frame, text=row[1]).place(          relx=0.4, rely=0.20)
            self.modelo = tk.Label(         frame, text=row[2]).place(          relx=0.4, rely=0.25)
            self.matricula = tk.Label(      frame, text=row[4]).place(          relx=0.4, rely=0.30)
            self.NroMatricula = row[4]
            self.precio = tk.Label(         frame, text=row[6]).place(          relx=0.4, rely=0.35)
            self.precioXdia = int(row[6])



        con.close()
        """
        ------------****************BASE DE DATOS*****************-----------------------------------------------------------------------------------------------CLOSE---
        """

        window.mainloop()

    def verPago(self,frame):
        self.verPago = Toplevel()
        self.verPago.title(" VER PAGO")
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
                  command=partial(self.validarPago,frame)).place(relx=0.50, rely=0.5)
        tk.Button(frameVerPago, text="Atras",
                  command=self.verPago.withdraw).place(relx=0.01, rely=0.01)


    def validarPago(self, frame):
        if (self.codigoVer.get()):
            if (self.codigoVer.get() == "123"):  # Valida el codigo ingresado con el codigo tecnico
                messagebox._show("Pago", "Pago Aceptado")
                self.Verificacion = True
                self.labelValidacion = tk.Label(frame, text="PAGO OK", fg="green").place(       relx=0.50, rely=0.60)
                self.verPago.withdraw()
            else:
                messagebox.showwarning("Pago", "Pago Erroneo")
                self.codigoVer.focus()
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.codigoVer.focus()


    def calcularTOTAL(self,frame):
        if(self.boxDiasDeAlquiler.get()):
            if(self.boxDiasDeAlquiler.get().isnumeric()):
                if((int(self.boxDiasDeAlquiler.get())<15) and (int(self.boxDiasDeAlquiler.get())>0)):

                    a = int(self.precioXdia)
                    b = int(self.boxDiasDeAlquiler.get())
                    self.cantidadTotal = a*b

                    self.precioTotal = tk.Label(frame, text = self.cantidadTotal ).place(relx=0.4, rely=0.50)
                else:
                    messagebox.showwarning(
                        "Error", "Tiene que ser un numero del 1 al 14")
            else:
                messagebox.showwarning(
                    "Error", "Tiene que ingresar un numero del 1 al 14")
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")


    def siguienteInterfaz(self, frame):
        if(self.Verificacion==True):
            self.cambiosEnBD()
            self.wind.withdraw()
            obj=ConfirPago(Tk())

        else:
            messagebox.showerror("Realizar Pago", "Por favor, haga el pago del alquiler ")
        #Conexion con siguiente interfaz



    def cambiosEnBD(self):
        try:
            db_name = "base_datos/databaseGeneral.sqlite3"
            con = sqlite3.connect(db_name)
            cursorAlq = con.cursor()

            cursorAlq.execute("INSERT INTO Alquileres(IdCuil,IdMatricula,FechaAlquiler,CantDias,PrecioTotal) VALUES ( ?,?,?,?,? )", (self.numeroCUIL,self.NroMatricula,self.fecha,self.boxDiasDeAlquiler.get(),self.cantidadTotal ,))
            con.commit()

            cursorVehiculo = con.cursor()
            estadoV = 1                                                                                                                 # esta alquilado = true
            cursorVehiculo.execute("UPDATE vehiculos SET estaAlquilado=? WHERE matricula=?", (estadoV , self.NroMatricula,))
            con.commit()

            con.close()
        except Exception:
            MENSAJE_ERROR("HAY UN ERROR AL MODIFICAR EL ESTADO")
