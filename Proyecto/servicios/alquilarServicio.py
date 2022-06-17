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
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def ordenarPorClasificacion(tree, busqueda):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    if(busqueda):
        consulta = consultaBusqueda(busqueda) + " ORDER BY clasificacion DESC"
    else:
        consulta = "SELECT * FROM vehiculos ORDER BY clasificacion DESC"
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def ordenarPorMarca(tree, busqueda):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    if(busqueda):
        consulta = consultaBusqueda(busqueda) + " ORDER BY marca DESC"
    else:
        consulta = "SELECT * FROM vehiculos ORDER BY marca DESC"
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def ordenarPorModelo(tree, busqueda):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    if(busqueda):
        consulta = consultaBusqueda(busqueda) + " ORDER BY modelo DESC"
    else:
        consulta = "SELECT * FROM vehiculos ORDER BY modelo DESC"
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def ordenarPorGeneracion(tree, busqueda):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    if(busqueda):
        consulta = consultaBusqueda(busqueda) + " ORDER BY generacion DESC"
    else:
        consulta = "SELECT * FROM vehiculos ORDER BY generacion DESC"
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def ordenarPorKilometros(tree, busqueda):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    if(busqueda):
        consulta = consultaBusqueda(busqueda) + " ORDER BY km DESC"
    else:
        consulta = "SELECT * FROM vehiculos ORDER BY km DESC"
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def ordenarPorPrecio(tree, busqueda):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    if(busqueda):
        consulta = consultaBusqueda(busqueda) + " ORDER BY precio DESC"
    else:
        consulta = "SELECT * FROM vehiculos ORDER BY precio DESC"
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def buscarVehiculo(tree, busqueda):
    elementos = tree.get_children()
    for elemento in elementos:
        tree.delete(elemento)

    consulta = consultaBusqueda(busqueda)
    vehiculos = ejecutarConsulta(consulta, ())

    if (vehiculos != None):
        for vehiculo in vehiculos:
            if (vehiculo[7] == 0):
                values = (vehiculo[1], vehiculo[2], vehiculo[3],
                          vehiculo[5], vehiculo[6])
                tree.insert("", 0, text=vehiculo[0], values=values)


def consultaBusqueda(busqueda):
    busqueda = busqueda.lower()
    consulta = "SELECT * FROM vehiculos WHERE LOWER(clasificacion) LIKE '%"+busqueda+"%' OR LOWER(marca) LIKE '%"+busqueda+"%' OR LOWER(modelo) LIKE '%" + \
        busqueda+"%' OR LOWER(generacion) LIKE '%"+busqueda+"%' OR LOWER(km) LIKE '%" + \
        busqueda+"%' OR LOWER(precio) LIKE '%"+busqueda+"%'"
    return consulta


def mensajeError(titulo, mensaje):
    messagebox.showerror(title=titulo, message=mensaje)
