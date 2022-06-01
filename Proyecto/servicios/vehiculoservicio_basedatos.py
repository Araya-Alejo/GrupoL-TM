'''
    Métodos de Servicio para Vehiculo (Base de Datos)
    @author Bulos
'''
# ------------------------------------------------------------------------------
import sqlite3

from tkinter import messagebox
from entidades.vehiculo import Vehiculo
# ------------------------------------------------------------------------------
'''
    Función para consulta a base de datos.
'''
def run_query(query, parameters=()):
    db_name = "base_datos/databaseGeneral.sqlite3"

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
    except sqlite3.OperationalError:
        messagebox.showinfo(message="No se pudo acceder a la base de datos!", title="")
    else:
        return result

'''
    Procedimiento que obtiene los datos de la base de datos.
    Ingresa los datos obtenidos a Treeview.
'''
def get_vehiculo(tree):
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    query = "SELECT * FROM vehiculo"
    db_rows = run_query(query)

    for row in db_rows:
        tree.insert("", 0, values=row)

'''
    Procedimiento para ingresar un Vehiculo a la base de datos.
'''
def add_vehiculo(vehiculo, root):
    query = "INSERT INTO vehiculo VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
    parameters = (vehiculo.getClasificacion(),
        vehiculo.getMarca(),
        vehiculo.getModelo().upper(),
        vehiculo.getGeneracion(),
        vehiculo.getMatricula().replace(" ", "").upper(),
        vehiculo.getKm(),
        vehiculo.getPrecio(),
        vehiculo.isEstaAlquilado())
    result = run_query(query, parameters)
    if (resul != None):
        messagebox.showinfo(message="Vehiculo agregado!", title="", parent=root)

'''
    Procedimiento para eliminar un Vehiculo de la base de datos.
'''
def delete_vehiculo(tree, root):
    try:
        matricula = tree.item(tree.selection())["values"][4]
    except IndexError:
        messagebox.showinfo(message="Seleccione un Vehiculo!", title="", parent=root)
    else:
        query = "DELETE FROM vehiculo WHERE matricula = ?"
        result = run_query(query, (matricula, ))
        if (result != None):
            messagebox.showinfo(message="Vehiculo Eliminado!", title="", parent=root)

'''
    Función que valida si un Vehiculo ya se ha ingresado.
    La verificación se realiza por matricula.
    Retorna un bool.
'''
def validate_vehiculo(matricula):
    query = "SELECT * FROM vehiculo"
    db_rows = run_query(query)

    for row in db_rows:
        if (row[4] == matricula.upper()):
            return True

    return False
