from tkinter import *
from tkinter import messagebox as MessageBox
import tkinter as tk
from tkinter import ttk
import entidades.usuario as usuario
import subprocess
from TyC import *
import re
from servicios.vehiculoservicio import *
from servicios.usuarioServicio import UsuarioServicio
import base_datos
import sqlite3

us = UsuarioServicio()

class  VentanaUsuario:
    db_nombre = 'base_datos/databaseGeneral.sqlite3'

#---------------------------------------------------------------------------------#

    def cuandoEscribaFecha(self,event):
        if(len(self.fechaNacimiento.get()) > 9):
            return "break"

        if event.char.isdigit():
            texto = self.fechaNacimiento.get()
            letras = 0
            for i in texto:
                letras +=1

            if letras == 2:
                self.fechaNacimiento.insert(2,"/")
            elif letras == 5:
                self.fechaNacimiento.insert(5,"/")
        else:
            return "break"

    def cuandoEscribaCUIL(self,event):
        if event.char.isdigit():
            if(len(self.cuil.get()) > 10):
                return "break"
        else:
            return "break"

#---------------------------------------------------------------------------------#

    def cuandoEscriba_correo(self,texto):
        try:
            patron = re.compile(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{1,3}$')
            return re.search(patron, texto)
        except  ValueError:
            return False

#---------------------------------------------------------------------------------#

    def validarPASAPORTE(self, texto):
        try:
            patron = re.compile(r'^([A-Z]{3})+([0-9]){6}')
            return re.search(patron, texto)
        except ValueError:
            return False

#---------------------------------------------------------------------------------#

    def llamarVentanaCalendario(self):
        ventana = VentanaCalendario(Tk())

#---------------------------------------------------------------------------------#

    def abrirPDF(self):
        path = 'TyC\AlquilaYa_TerminosyCondiciones.pdf'
        subprocess.Popen([path], shell=True)

#---------------------------------------------------------------------------------#

    def cambiar(self):
        print("ingrese")
        if(self.extranjero.get() == "SI"):
            print("si")
            self.cuil.config(state=tk.DISABLED)             #proceso
        if(self.extranjero.get()  == "NO"):
            print("no")
            self.cuil.config(state=tk.NORMAL)
#---------------------------------------------------------------------------------#

    def aceptar(self):
        contador = 0
        try:
            if(not us.isStringVacio(self.nombre.get())):
                if(us.validarString(self.nombre.get())):
                    contador = contador + 1
                    print("nombre bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            if(not us.isStringVacio(self.apellido.get())):
                if(us.validarString(self.apellido.get())):
                    contador = contador + 1
                    print("apellido bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            if(not us.isStringVacio(self.carnetConducir.get())):
                if(us.isEnteroPositivo(self.carnetConducir.get())):
                    if(us.validarDNI(self.carnetConducir.get())):
                        contador = contador + 1
                        print("carnet bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            if(not us.isStringVacio(self.fechaNacimiento.get())):
                if(us.validarLongitudFecha(self.fechaNacimiento.get())):
                    if(us.validarFecha(self.fechaNacimiento.get())):
                        contador = contador + 1
                        print("fecha bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            if(not us.isStringVacio(self.correo.get())):
                if(self.cuandoEscriba_correo(self.correo.get())):
                    contador = contador + 1
                    print("correo bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            if(not us.isStringVacio(self.cuil.get())):
                if(us.isEnteroPositivo(self.cuil.get())):
                    if(us.validarCUIL(self.cuil.get())):
                        contador = contador + 1
                        print("cuil bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            if(not us.isStringVacio(self.pasaporte.get())):
                if( self.validarPASAPORTE(self.pasaporte.get())):
                    print("pasaporte bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            print(self.variable.get())
            if(self.variable.get() == 0):
                contador = contador + 1                 #terminar
                print("check bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")


        if(contador == 7):
            return True
#---------------------------------------------------------------------------------#

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

        self.nombre = Label(area, text = 'Nombre *', font= ("Bahnschrift Light",10))
        self.nombre.pack(fill=tk.BOTH)
        self.nombre = Entry(area)
        self.nombre.pack(pady = 5)

        self.apellido =Label(area, text = 'Apellido *', font= ("Bahnschrift Light",10))
        self.apellido.pack(fill=tk.BOTH)
        self.apellido = Entry(area)
        self.apellido.pack(pady = 5)

        self.carnetConducir =Label(area, text = 'Carnet de Conducir *', font= ("Bahnschrift Light",10))
        self.carnetConducir.pack(fill=tk.BOTH)
        self.carnetConducir = Entry(area)
        self.carnetConducir.pack(pady = 5)

        self.fechaNacimiento =Label(area, text = 'Fecha de nacimiento *', font= ("Bahnschrift Light",10))
        self.fechaNacimiento.pack(fill=tk.BOTH)
        self.fechaNacimiento = Entry(area)
        self.fechaNacimiento.pack()
        self.fechaNacimiento.bind("<Key>", self.cuandoEscribaFecha)
        self.fechaNacimiento.bind("<BackSpace>", lambda _:self.fechaNacimiento.delete(tk.END))

        self.correo =Label(area, text = 'Correo *', font= ("Bahnschrift Light",10))
        self.correo.pack(fill=tk.BOTH)
        self.correo = Entry(area)
        self.correo.pack(pady = 5)

        self.extranjero =Label(area, text = 'Es extranjero? *', font= ("Bahnschrift Light",10))
        self.extranjero.pack(fill=tk.BOTH)
        self.extranjero = ttk.Combobox(area, state="readonly")
        self.extranjero.pack(pady = 5)
        self.extranjero['values'] = ('SI', 'NO')
        self.extranjero.current(1)


        self.cuil =Label(area, text = 'CUIL', font= ("Bahnschrift Light",10))
        self.cuil.pack(fill=tk.BOTH)
        self.cuil = Entry(area)
        self.cuil.pack(pady = 5)
        self.cuil.bind("<Key>", self.cuandoEscribaCUIL)
        self.cuil.bind("<BackSpace>", lambda _:self.cuil.delete(tk.END))

        self.pasaporte =Label(area, text = 'Pasaporte', font= ("Bahnschrift Light",10))
        self.pasaporte.pack(fill=tk.BOTH)
        self.pasaporte = Entry(area)
        self.pasaporte.pack(pady = 5)


        self.boton = tk.Button(area, text = 'T&C', font= ("Bahnschrift Light",10), command = self.abrirPDF )
        self.boton.pack()

        self.variable = IntVar()
        self.check = Checkbutton(area, text="Termino y condiciones *", variable=self.variable, onvalue=1, offvalue=0)
        self.check.pack()

        self.boton = tk.Button(area, text = 'Reconocimiento facial *', font= ("Bahnschrift Light",10),command = self.desarrollando )
        self.boton.pack()


        self.boton = tk.Button(area, text = 'Enviar', font= ("Bahnschrift Light",10),command = self.agregar_usuario )
        self.boton.pack(pady = 20)

        ventana.mainloop()

#---------------------------------------------------------------------------------#

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

#---------------------------------------------------------------------------------#

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
                if self.validar():
                    MessageBox.showinfo(" ", "Se a guardado el usuario en la base de datos")
                    consulta = 'INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
                    parametros = (self.nombre.get(),self.apellido.get(),self.carnetConducir.get(),self.fechaNacimiento.get(),self.correo.get(),self.extranjero.get(),self.cuil.get(),self.pasaporte.get())
                    self.ejecutar_consulta(consulta,parametros)
            except Exception:
                MessageBox.showwarning("Alerta", "Hay valores fue erroneo")

#---------------------------------------------------------------------------------#

    def validar(self):
        if(self.aceptar()):
            print("fue validado")
            return True
        else:
            print("no fue validado")
            return False
