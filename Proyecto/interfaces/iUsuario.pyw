from tkinter import *
from tkinter import messagebox as MessageBox
import tkinter as tk
from tkinter import ttk
import entidades.usuario as usuario
import subprocess
from TyC import *
import re
from servicios.usuarioServicio import UsuarioServicio
import base_datos
import sqlite3

us = UsuarioServicio()

class  VentanaUsuario:
    db_nombre = 'base_datos/databaseGeneral.sqlite3'

#---------------------------------------------------------------------------------#

    def cuandoEscriba(self,event):
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
            return False

#---------------------------------------------------------------------------------#

    def cuandoEscriba_correo(self):
        texto = self.correo.get()
        if(re.search(r"@gmail.com$, @hotmail.com$,@hotmail.com.ar$,@gmail.com.ar$,@alumnos.frm.utn.edu.ar$,@docentes.frm.utn.edu.ar$",texto)):
            return True
        else:
            return False

#---------------------------------------------------------------------------------#

    def validarPASAPORTE(self, texto):
        try:
            buscador = re.search(r"[A-Z].{3}er,[0-9].{5}er,",texto)
            print(buscador)
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
                if(us.isEnteroPositivo(self.fechaNacimiento.get())):
                    if(us.validarStringAlfa(self.fechaNacimiento.get())):
                        if(us.validarLomgitudFecha(self.fechaNacimiento.get())):
                            contador = contador + 1
                            print("fecha bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        try:
            if(not us.isStringVacio(self.correo.get())):
                if(cuandoEscriba_correo(self.correo.get())):
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
                    if( us.validarStringAlfa(self.pasaporte.get())):
                        if( us.validarLomgitudFecha(self.pasaporte.get())):
                            contador = contador + 1
                            print("pasaporte bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        if(contador == 6):
            return True

        # if(self.var1.get()=="On"):                      #Arreglar
        #     print("terminos y condiciones : Bien")
        # else:
        #     print("terminos y condiciones : Mal")

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
        self.fechaNacimiento.bind("<Key>", self.cuandoEscriba)
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

        # if(self.extranjero.get() == "SI"):
        #     self.cuil.config(state=tk.DISABLED)             #TERMINAR
        # if(self.extranjero.get() == "NO"):
        #     self.cuil.config(state=tk.NORMAL)


        self.pasaporte =Label(area, text = 'Pasaporte', font= ("Bahnschrift Light",10))
        self.pasaporte.pack(fill=tk.BOTH)
        self.pasaporte = Entry(area)
        self.pasaporte.pack(pady = 5)


        self.boton = tk.Button(area, text = 'T&C', font= ("Bahnschrift Light",10), command = self.abrirPDF )
        self.boton.pack()

        self.var1 = StringVar()
        self.check = Checkbutton(area, text="Termino y condiciones *", variable=self.var1, onvalue="On", offvalue="Off")
        self.check.pack()

        self.boton = tk.Button(area, text = 'Reconocimiento facial *', font= ("Bahnschrift Light",10),command = self.desarrollando )
        self.boton.pack()


        self.boton = tk.Button(area, text = 'Enviar', font= ("Bahnschrift Light",10),command = self.validar )
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
                if self.aceptar():
                    consulta = 'INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
                    parametros = (self.nombre.get(),self.apellido.get(),self.carnetConducir.get(),self.fechaNacimiento.get(),self.correo.get(),self.extranjero.get(),self.cuil.get(),self.pasaporte.get())
                    self.ejecutar_consulta(consulta,parametros)
            except Exception:
                MessageBox.showwarning("Alerta", "Hay valores fue erroneo")

#---------------------------------------------------------------------------------#

    def validar(self):
        if(self.aceptar):
            print("fue validado")
            return True
        else:
            print("no fue validado")
            return False
