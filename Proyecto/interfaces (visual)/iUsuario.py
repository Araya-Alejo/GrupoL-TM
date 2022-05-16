from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__ (self, _nombre, _pasaporte, _cuil, _licencia, _edad, _foto):
        self._nombre = _nombre
        self._pasaporte = _pasaporte
        self._cuil = _cuil
        self._licencia = _licencia
        self._edad = _edad
        self._foto = _foto


    def get_nombre(self):
        return self._nombre

    def get_pasaporte(self):
        return self._pasaporte

    def get_cuil(self):
        return self._cuil

    def get_licencia(self):
        return self._licencia

    def get_edad(self):
        return self._edad

    def get_foto(self):
        return self._foto


    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

    def set_pasaporte(self, new_pasaporte):
        self._pasaporte = new_pasaporte

    def set_cuil(self, new_cuil):
        self._cuil = new_cuil

    def set_licencia(self, new_licencia):
        self._licencia = new_licencia

    def set_edad(self, new_edad):
        self._edad = new_edad

    def set_foto(self, new_foto):
        self._foto = new_foto


class Ventana:
    def __init__(self, inter):
        self.interfaz = inter
        self.interfaz.geometry("800x600")
        self.interfaz.title("Alquila YA")
        self.dibujarVentana()

# LAYOUT
    def dibujarVentana(self):
        Button(self.interfaz, command=self.loginAdmin,
               text="Login Admin").place(x=700, y=10)
        Button(self.interfaz, command=self.alquilar,
               text="Alquilar").place(x=325, y=250)
        Button(self.interfaz, command=self.devolucion,
               text="Devolucion").place(x=425, y=250)

# VALIDACION
    def validar(a1, a2):
        #print("hola")
        if a1 == "Rxvargas" and a2 == "rodrigo":
            abrirVentanaAdmin()
        else:
            messagebox.showwarning("Error", "Error de credenciales")

    def loginAdmin(self):
        self.interfaz.withdraw()
        ventana2 = tk.Toplevel()
        ventana2.geometry("800x600")
        ventana2.title("Alquila YA")
        etiqueta1 = Label(ventana2, text="Nombre: ").place(x=325, y=150)
        text1 = Entry(ventana2).place(x=400, y=150)
        etiqueta2 = Label(ventana2, text="Pasaporte: ").place(x=325, y=175)
        text2 = Entry(ventana2).place(x=400, y=175)
        etiqueta3 = Label(ventana2, text="Cuil: ").place(x=325, y=200)
        text2 = Entry(ventana2).place(x=400, y=200)
        etiqueta4 = Label(ventana2, text="Liciencia: ").place(x=325, y=225)
        text2 = Entry(ventana2).place(x=400, y=225)
        etiqueta5 = Label(ventana2, text="Edad: ").place(x=325, y=250)
        text2 = Entry(ventana2).place(x=400, y=250)
        Button(self.interfaz, command=self.loginAdmin,
               text="Reconocimiento facial").place(x=700, y=350)

        botonValidar = Button(ventana2, text="Validar",
                              command=partial(validar, text1, text2)).place(x=450, y=350)

    def abrirVentanaAdmin(self):
        ventana2.withdraw()
        ventana3 = tk.Toplevel()
        ventana3.geometry("800x600")
        ventana3.title("Alquila YA")
        Label(ventana3, text="Exito!!!").place(x=325, y=250)

    def alquilar(self):
        print("Hola")

    def devolucion(self):
        print("Hola")


obj = Ventana(Tk())
obj.interfaz.mainloop()
