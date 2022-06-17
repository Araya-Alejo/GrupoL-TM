from tkinter import *
import tkinter as tk
from tkinter import ttk
import entidades.usuario as usuario
from TyC import *
from servicios.vehiculoservicio import *
from servicios.usuarioServicio import UsuarioServicio
import base_datos
from entidades.usuario import Usuario
import TyC.ingresoTyC as TC
import servicios.reconocimientoFacial as RECONOCIMIENTO_FACIAL
from interfaces.ESTANDARES import *

us = UsuarioServicio()

class  VentanaUsuario:
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

    def cuandoEscribaCarnet(self,event):
        if event.char.isdigit():
            if(len(self.carnetConducir.get()) > 7):
                return "break"
        else:
            return "break"

    def cuandoEscribaNombre(self,event):
        if event.char.isalpha():
            return event
        else:
            return "break"

#---------------------------------------------------------------------------------#

    def validar(self):
        validado = self.aceptar()
        if(validado == True):
            MENSAJE_CONSOLA("VALORES INGRESADOS VALIDADOS", visible)
            print("---------------------------------------------------------------------------------")
            USUARIO = Usuario(self.nombre.get(),self.apellido.get(),self.carnetConducir.get(),self.fechaNacimiento.get(),self.correo.get(),self.cuil.get())

            MessageBox.showinfo("", "VENTANA DE RECONOCIMIENTO FACIAL")
            RECONOCIMIENTO_FACIAL.register_capture(USUARIO)
        elif (validado == None):
            MENSAJE_CONSOLA("PROBLEMAS CON LA VALIDACION",visible)
            print("---------------------------------------------------------------------------------")
            return False
        else:
            MENSAJE_CONSOLA("PROBLEMAS CON EL RECONOCIMIENTO FACIL",visible)
            print("---------------------------------------------------------------------------------")
            return False

#---------------------------------------------------------------------------------#

    def aceptar(self):
        contador = 0
        print("---------------------------------------------------------------------------------")

        # Validación Nombre
        if(not us.isStringVacio(self.nombre.get())):
            if(us.validarString(self.nombre.get())):
                contador = contador + 1
                self.Error_labelNombre["text"] = ""
        else:
            self.Error_labelNombre["text"] = "Incorrecto"

        # Validación Apellido
        if(not us.isStringVacio(self.apellido.get())):
            if(us.validarString(self.apellido.get())):
                contador = contador + 1
                self.Error_labelApellido["text"] = ""
        else:
            self.Error_labelApellido["text"] = "Incorrecto"


        # Validación Carnet COnducir
        if(not us.isStringVacio(self.carnetConducir.get())):
            if(us.isEnteroPositivo(self.carnetConducir.get())):
                if(us.validarDNI(self.carnetConducir.get())):
                    contador = contador + 1
                    self.Error_labelCarnetConducir["text"] = ""
        else:
            self.Error_labelCarnetConducir["text"] = "Incorrecto"


        # Validación Fecha Nacimiento
        if(not us.isStringVacio(self.fechaNacimiento.get())):
            if(us.validarLongitudFecha(self.fechaNacimiento.get())):
                if(us.validarFecha(self.fechaNacimiento.get())):
                    contador = contador + 1
                    self.Error_labelFechaNacimiento["text"] = ""
        else:
            self.Error_labelFechaNacimiento["text"] = "Incorrecto"


        # Validación Correo
        if(not us.isStringVacio(self.correo.get())):
            if(us.cuandoEscriba_correo(self.correo.get())):
                contador = contador + 1
                self.Error_labelCorreo["text"] = ""
        else:
            self.Error_labelCorreo["text"] = "Incorrecto"


        # Validación Carnet Conducir
        if(not us.isStringVacio(self.cuil.get())):
            if(us.isEnteroPositivo(self.cuil.get())):
                if(us.validarCUIL(self.cuil.get())):
                    if(us.compararDNI_CUIL(self.cuil.get(), self.carnetConducir.get())):
                        contador = contador + 1
                        self.Error_labelCuil["text"] = ""
        else:
            self.Error_labelCuil["text"] = "Incorrecto"
        """
        try:
            print(self.variable.get())
            if(self.variable.get() == 0):
        """
        contador = contador + 1                 #terminar
        """
                print("check bien")
        except ValueError:
            MessageBox.showwarning("Alerta", "Uno de los valores fue erroneo")

        print("---------------------------------------------------------------------------------")
        """
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

        self.labelNombre = Label(area, text = 'Nombre *', font= (tipografia,10))
        self.labelNombre.place(x=350, y=30)
        self.Error_labelNombre = Label(area, text="", fg="red")
        self.Error_labelNombre.place(x=480, y=50)
        self.nombre = Entry(area)
        self.nombre.place(x=350, y=50)
        self.nombre.bind("<Key>", self.cuandoEscribaNombre)
        self.nombre.bind("<BackSpace>", lambda _:self.nombre.delete(tk.END))



        self.apellido =Label(area, text = 'Apellido *', font= (tipografia,10))
        self.apellido.place(x=350, y=80)
        self.Error_labelApellido = Label(area, text="", fg="red")
        self.Error_labelApellido.place(x=480, y=100)
        self.apellido = Entry(area)
        self.apellido.place(x=350, y=100)
        self.apellido.bind("<Key>", self.cuandoEscribaNombre)
        self.apellido.bind("<BackSpace>", lambda _:self.apellido.delete(tk.END))

        self.carnetConducir =Label(area, text = 'Carnet de Conducir *', font= (tipografia,10))
        self.carnetConducir.place(x=350, y=130)
        self.Error_labelCarnetConducir = Label(area, text="", fg="red")
        self.Error_labelCarnetConducir.place(x=480, y=150)
        self.carnetConducir = Entry(area)
        self.carnetConducir.place(x=350, y=150)
        self.carnetConducir.bind("<Key>", self.cuandoEscribaCarnet)
        self.carnetConducir.bind("<BackSpace>", lambda _:self.carnetConducir.delete(tk.END))


        self.fechaNacimiento =Label(area, text = 'Fecha de nacimiento *', font= (tipografia,10))
        self.fechaNacimiento.place(x=350, y=180)
        self.Error_labelFechaNacimiento = Label(area, text="", fg="red")
        self.Error_labelFechaNacimiento.place(x=480, y=200)
        self.fechaNacimiento = Entry(area)
        self.fechaNacimiento.place(x=350, y=200)
        self.fechaNacimiento.bind("<Key>", self.cuandoEscribaFecha)
        self.fechaNacimiento.bind("<BackSpace>", lambda _:self.fechaNacimiento.delete(tk.END))

        self.correo =Label(area, text = 'Correo *', font= (tipografia,10))
        self.correo.place(x=350, y=230)
        self.Error_labelCorreo = Label(area, text="", fg="red")
        self.Error_labelCorreo.place(x=480, y=250)
        self.correo = Entry(area)
        self.correo.place(x=350, y=250)

        self.cuil =Label(area, text = 'CUIL', font= (tipografia,10))
        self.cuil.place(x=350, y=280)
        self.Error_labelCuil = Label(area, text="", fg="red")
        self.Error_labelCuil.place(x=480, y=300)
        self.cuil = Entry(area)
        self.cuil.place(x=350, y=300)
        self.cuil.bind("<Key>", self.cuandoEscribaCUIL)
        self.cuil.bind("<BackSpace>", lambda _:self.cuil.delete(tk.END))

        self.boton = tk.Button(area, text = 'T&C', font= (tipografia,10), command = TC.abrirPDF )
        self.boton.place(x=400, y=350)

        # self.variable = IntVar()
        # self.check = Checkbutton(area, text="Termino y condiciones *", font=(tipografia,10), variable=self.variable, onvalue=1, offvalue=0)
        # self.check.place(x=340, y=400)

        self.comboTyC = ttk.Combobox(area, state="readonly",
            values=["SI", "NO"])
        self.comboTyC.place(x=342, y=400, height=24)

        self.boton = tk.Button(area, text = 'Reconocimiento facial *', font= (tipografia,10),command = self.validar )
        self.boton.place(x=342, y=450)

        ventana.mainloop()
