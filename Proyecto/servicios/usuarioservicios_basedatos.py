import sqlite3
from entidades.usuario import Usuario
import interfaces.iUsuario
from tkinter import messagebox as MessageBox

def agregar_usuario(usuario):
        try:
            consulta = "INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?)"
            print("consulta")
            print(usuario.getNombre(),usuario.getApellido(),usuario.getCarnetConducir(),usuario.getFechaNacimiento(),usuario.getCorreo(),usuario.getCuil())
            parametros = (usuario.getNombre(),usuario.getApellido(),usuario.getCarnetConducir(),usuario.getFechaNacimiento(),usuario.getCorreo(),usuario.getCuil())
            print("parametros")
            resultado = ejecutar_consulta(consulta,parametros)
            print("resultados")
            if (resultado != None):
                MessageBox.showinfo(" ", "Se a guardado el usuario en la base de datos")
        except Exception:
            MessageBox.showwarning("Alerta", "Hay un error al agregar un usuario")

def ejecutar_consulta(consulta, parametros = ()):
    db_name = "base_datos/databaseGeneral.sqlite3"
    print("ejecutar")

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            print("cursor")
            resultado = cursor.execute(consulta, parametros)
            print("resultado")
            conn.commit()
    except sqlite3.OperationalError:
        messagebox.showinfo(" ","No se pudo acceder a la base de datos!")
    return resultado
