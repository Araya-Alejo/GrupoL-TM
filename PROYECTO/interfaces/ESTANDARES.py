from tkinter import messagebox as MessageBox, Label

visible = True
direccion_base_datos = "base_datos/databaseGeneral.sqlite3"
tipografia = "Bahnschrift Light"


def MENSAJE_INFO(texto):
    MessageBox.showinfo("", texto)

def MENSAJE_ERROR(texto):
    MessageBox.showwarning("Alerta", texto)

def MENSAJE_CONSOLA(texto, visible):
    if(visible):
        print(texto)

def SALTO_DE_LINEA(cantidad):
    for x in range(cantidad):
        print(" ")
