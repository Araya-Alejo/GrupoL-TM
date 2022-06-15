import sqlite3

from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox


def ejecutarConsulta(consulta, parametros=()):
    dbNombre = "base_datos/databaseGeneral.sqlite3"

    try:
        with sqlite3.connect(dbNombre) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
    except sqlite3.OperationalError:
        mensajeError("¡Error!", "No se pudo ingresar a la base de datos")
    else:
        return result


def mostrarVehiculoDisponible(tree):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    consulta = "SELECT * FROM vehiculos"
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[4], vehiculo[5], vehiculo[6], "No")
                tree.insert("", 0, text=vehiculo[0], values=values)


def mensajeError(titulo, mensaje):
    messagebox.showerror(title=titulo, message=mensaje)
