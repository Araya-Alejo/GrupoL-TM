from tkinter import messagebox as MessageBox

direccion_base_datos = "base_datos/databaseGeneral.sqlite3"
tipografia = "Bahnschrift Light"

def MENSAJE_INFO(texto):
    MessageBox.showinfo("", texto)

def MENSAJE_ERROR(texto):
    MessageBox.showwarning("Alerta", texto)
