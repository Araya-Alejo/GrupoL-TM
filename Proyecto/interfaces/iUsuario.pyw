from tkinter import *
import tkinter as tk
import entidades.usuario as usuario
import subprocess
from TyC import *
from servicios.usuarioServicio import UsuarioServicio
import base_datos
import sqlite3

us = UsuarioServicio()

class  VentanaUsuario:
    db_nombre = 'base_datos/databaseGeneral.sqlite3'

    def llamarVentanaCalendario(self):
        ventana = VentanaCalendario(Tk())

    def abrirPDF(self):
        path = 'TyC\AlquilaYa_TerminosyCondiciones.pdf'
        subprocess.Popen([path], shell=True)

    def aceptar(self):


        if(not us.validarString(self.nombre.get())):
            print("Nombre: Bien")
        else:
            print("Nombre: Mal")

        if(not us.validarString(self.apellido.get())):
            print("Apellido: Bien")
        else:
            print("Apellido: Mal")

        if(us.validarInt(self.carnetConducir.get())):
            print("carnetConducir: Bien")
        else:
            print("carnetConducir: Mal")

        if(not us.validarStringAlfa(self.fechaNacimiento.get())):
            print("fechaNacimiento: Bien")
        else:
            print("fechaNacimiento: Mal")

        if(not us.validarStringAlfa(self.correo.get())): #Completar
            print("correo: Bien")
        else:
            print("correo: Mal")

        if(not us.validarString(self.extranjero.get())):
            print("extranjero: Bien")
        else:
            print("extranjero: Mal")

        if(us.validarInt(self.cuil.get())):
            print("cuil: Bien")
        else:
            print("cuil: Mal")

        if(not us.validarStringAlfa(self.pasaporte.get())):
            print("pasaporte: Bien")
        else:
            print("pasaporte: Mal")

        if(self.var1.get()=="On"):                      #Arreglar
            print("terminos y condiciones : Bien")
        else:
            print("terminos y condiciones : Mal")


    def __init__(self, ventana):
        self.ventana = ventana
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()
        ancho2 = 800
        alto2 = 600
        izquierda = (ancho - ancho2) / 2
        arriba = (alto - alto2) / 2
        self.ventana.geometry("%dx%d+%d+%d" % (ancho2, alto2, izquierda, arriba))
        self.ventana.title("Agregar Vehiculo")
        self.ventana.resizable(False, False)

        area = Frame(ventana, pady=10)
        area.pack(expand=True, fill=tk.BOTH)

        self.nombre = Label(area, text = 'Nombre', font= ("Bahnschrift Light",10))
        self.nombre.pack(fill=tk.BOTH)
        self.nombre = Entry(area)
        self.nombre.pack(pady = 5)

        self.apellido =Label(area, text = 'Apellido', font= ("Bahnschrift Light",10))
        self.apellido.pack(fill=tk.BOTH)
        self.apellido = Entry(area)
        self.apellido.pack(pady = 5)

        self.carnetConducir =Label(area, text = 'Carnet de Conducir', font= ("Bahnschrift Light",10))
        self.carnetConducir.pack(fill=tk.BOTH)
        self.carnetConducir = Entry(area)
        self.carnetConducir.pack(pady = 5)

        self.fechaNacimiento =Label(area, text = 'Fecha de nacimiento', font= ("Bahnschrift Light",10))
        self.fechaNacimiento.pack(fill=tk.BOTH)
        self.fechaNacimiento = Entry(area)
        self.fechaNacimiento.pack()

        self.correo =Label(area, text = 'Correo', font= ("Bahnschrift Light",10))
        self.correo.pack(fill=tk.BOTH)
        self.correo = Entry(area)
        self.correo.pack(pady = 5)

        self.extranjero =Label(area, text = 'Es extranjero?', font= ("Bahnschrift Light",10))
        self.extranjero.pack(fill=tk.BOTH)
        self.extranjero = Entry(area)
        self.extranjero.pack(pady = 5)

        self.cuil =Label(area, text = 'CUIL', font= ("Bahnschrift Light",10))
        self.cuil.pack(fill=tk.BOTH)
        self.cuil = Entry(area)
        self.cuil.pack(pady = 5)

        self.pasaporte =Label(area, text = 'Pasaporte', font= ("Bahnschrift Light",10))
        self.pasaporte.pack(fill=tk.BOTH)
        self.pasaporte = Entry(area)
        self.pasaporte.pack(pady = 5)


        self.boton = tk.Button(area, text = 'T&C', font= ("Bahnschrift Light",10), command = self.abrirPDF )
        self.boton.pack()

        self.var1 = StringVar()
        self.check = Checkbutton(area, text="Termino y condiciones", variable=self.var1, onvalue="On", offvalue="Off")
        self.check.pack()

        self.boton = tk.Button(area, text = 'Reconocimiento facial', font= ("Bahnschrift Light",10),command = self.desarrollando )
        self.boton.pack()


        self.boton = tk.Button(area, text = 'Enviar', font= ("Bahnschrift Light",10),command = self.agregar_usuario )
        self.boton.pack(pady = 20)



        ventana.mainloop()

    def desarrollando(self):
        self.ventana = Tk()
        ancho = self.ventana.winfo_screenwidth()
        alto = self.ventana.winfo_screenheight()
        ancho2 = 400
        alto2 = 200
        izquierda = (ancho - ancho2) / 2
        arriba = (alto - alto2) / 2
        self.ventana.geometry("%dx%d+%d+%d" % (ancho2, alto2, izquierda, arriba))
        self.ventana.title("Agregar Vehiculo")
        self.ventana.resizable(False, False)

        area = Frame(self.ventana, pady=10)
        area.pack(expand=True, fill=tk.BOTH)

        self.mensaje = Label(area, text = 'Se hara proximamente', font= ("Bahnschrift Light",10))
        self.mensaje.pack(expand = True)

    def ejecutar_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(self.db_nombre) as coneccion:
            cursor = coneccion.cursor()
            resultados = cursor.execute(consulta, parametros)
            coneccion.commit()
        return resultados
    #
    # def obtener_usuario(self):
    #     consulta = 'SELECT * FROM Usuarios ORDER BY nombre DESC'
    #     db_filas = self.ejecutar_consulta(consulta)
    #     print(db_filas)

    def agregar_usuario(self):
            try:
                if self.aceptar():
                    consulta = 'INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
                    parametros = (self.nombre.get(),self.apellido.get(),self.carnetConducir.get(),self.fechaNacimiento.get(),self.correo.get(),self.extranjero.get(),self.cuil.get(),self.pasaporte.get())
                    self.ejecutar_consulta(consulta,parametros)
            except Exception:
                print("hay un error")
