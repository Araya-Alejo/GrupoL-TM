import tkinter as tk
from tkinter import *

import sqlite3
from tkinter import messagebox
from functools import partial
from interfaces.ESTANDARES import *
from interfaces.iDevolucionOK import VentanaDevOk
import servicios.mail
import servicios.SO


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
        frame = tk.Frame(self.wind)
        frame.place(relwidth=1, relheight=1)

        #Creacion de los Label de etiqueta
        tk.Label(frame, text="DATOS DEL ALQUILER").place(relx=0.40, rely=0.0)
        tk.Label(frame, text="Cuil:").place(relx=0.01, rely=0.05)
        tk.Label(frame, text="Nombre y Apellido:").place(
            relx=0.01, rely=0.10)
        tk.Label(frame, text="Marca:").place(relx=0.01, rely=0.25)
        tk.Label(frame, text="Modelo:").place(relx=0.01, rely=0.15)
        tk.Label(frame, text="Matricula del auto alquilado:").place(
            relx=0.01, rely=0.20)
        tk.Label(frame, text="Fecha del Alquiler:").place(
            relx=0.01, rely=0.30)
        tk.Label(frame, text="Cantidad de dias del alquiler:").place(
            relx=0.01, rely=0.35)
        tk.Label(frame, text="Precio del alquiler por dia:").place(
            relx=0.01, rely=0.40)
        tk.Label(frame, text="Precio Total").place(
            relx=0.01, rely=0.45)
        self.labelValidacion = tk.Label(frame, text="Verificacion", fg="red").place(
            relx=0.40, rely=0.60)
        self.Verificacion = False

        self.idMatricula = ""
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cursorAlq = con.cursor()
        cursorAlq.execute("SELECT * FROM Alquileres WHERE idCuil=?", (idCuil,))
        recordsAlq= cursorAlq.fetchall()
        for row in recordsAlq:
            self.idMatricula = ""+row[1]
            self.bdCuil = tk.Label(frame, text= row[0]).place(relx=0.4, rely=0.05)
            cuil=row[0]
            self.bdMatricula = tk.Label(frame, text=row[1]).place(
                relx=0.4, rely=0.20)
            self.bdFecha = tk.Label(frame, text=row[2]).place(
                relx=0.4, rely=0.30)
            fechaAlquiler=row[2]
            self.bdDiasAlquiler = tk.Label(frame, text=row[3]).place(
                relx=0.4, rely=0.35)
            diasAlquiler=str(row[3])
            self.bdPrecio = tk.Label(frame, text=row[4]).place(
                relx=0.4, rely=0.40)
            precio=str(row[4])
            self.dbPrecioTotal = tk.Label(frame, text=(row[3]*row[4])).place(
                relx=0.4, rely=0.45)
            precioTotal=str(row[3]*row[4])

        cursorUser = con.cursor()
        cursorUser.execute("SELECT * FROM Usuarios WHERE Cuil=?", (idCuil,))
        recordsUser= cursorUser.fetchall()
        for row in recordsUser:
            self.bdNombreApellido = tk.Label(frame, text= row[0]+" "+row[1]).place(relx=0.4, rely=0.10)
            nombreApellido= row[0]+" "+row[1]
            email=row[4]

        cursorVehiculo = con.cursor()
        cursorVehiculo.execute("SELECT * FROM vehiculos WHERE matricula=?", (self.idMatricula,))
        recordsVehiculo= cursorVehiculo.fetchall()
        for row in recordsVehiculo:
            self.bdMarca = tk.Label(frame, text=row[1]).place(relx=0.4, rely=0.25)
            marca=row[1]
            self.bdModelo = tk.Label(frame, text=row[2]).place(relx=0.4, rely=0.15)
            modelo=row[2]

        con.close()
        mensaje= "Subject: AlquilaYa - Devolución de Vehículo.\nSaludos Sr/Sra: " + nombreApellido +"\nLe informamos que se ha devuelto correctamente el vehículo de los siguientes datos: \n Modelo: "+ modelo +"\nMarca: "+ marca +"\nMatricula: "+ self.idMatricula +"\nDesde la fecha"+ fechaAlquiler +"\nDias del alquiler: "+ diasAlquiler +"\nPrecio Total: "+ precioTotal +"\nMuchas gracias por usar nuestro servicio."

        #Creacion de los Botones
        tk.Button(frame, text="VERIFICACIÓN TÉCNICA",
                  command=partial(self.verTecnica,frame)).place(relx=0.01, rely=0.60)
        tk.Button(frame, text="SIGUIENTE",
                  command=partial(self.siguienteInterfaz,idCuil,self.idMatricula, mensaje, email)).place(relx=0.80, rely=0.80)
        tk.Button(frame, text="Atras",
                   command=self.atras).place(relx=0.01, rely=0.9)
        self.codigoVer = tk.Entry(frame)
        self.codigoVer.focus()
        self.codigoVer.place(relx=0.20, rely=0.6)

        #self.muestraDeDatos(idCuil, frame)

        window.mainloop()

    def atras(self):
        self.wind.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj= Ventana1(Tk())

    def verTecnica(self, frame):
        if (self.codigoVer.get()):
            if (self.codigoVer.get() == "123"):  # Valida el codigo ingresado con el codigo tecnico
                messagebox._show("Validación Técnica", "Codigo Aceptado")
                self.Verificacion = True
                self.labelValidacion = tk.Label(frame, text="Verificación OK", fg="green").place(
                    relx=0.40, rely=0.60)
            else:
                messagebox.showwarning("Validación Técnica", "Codigo Erroneo")
                self.codigoVer.focus()
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.codigoVer.focus()


    def siguienteInterfaz(self, idCuil, idMatricula, mensaje, email):
        if(self.Verificacion==True):
            self.wind.withdraw()
            obj=VentanaDevOk(Tk(),idCuil,idMatricula, mensaje, email)
        else:
            messagebox.showerror("Verificacion Tecnica", "Por favor, haga la verificacion tecnica")
        #Conexion con siguiente interfaz
