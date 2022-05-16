from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import messagebox


class Ventana:

    def __init__(self, inter):
        self.interfaz = inter
        self.interfaz.geometry("800x600")
        self.interfaz.title("Alquila YA")
        self.dibujarVentana()

    def dibujarVentana(self):
        Button(self.interfaz, command=self.loginAdmin,
               text="Login Admin").place(x=700, y=10)
        Button(self.interfaz, command=self.alquilar,
               text="Alquilar").place(x=325, y=250)
        Button(self.interfaz, command=self.devolucion,
               text="Devolucion").place(x=425, y=250)

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
        etiqueta1 = Label(ventana2, text="Usuario: ").place(x=325, y=250)
        text1 = Entry(ventana2).place(x=400, y=250)
        etiqueta2 = Label(ventana2, text="Contraseña: ").place(x=325, y=275)
        text2 = Entry(ventana2).place(x=400, y=300)
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
