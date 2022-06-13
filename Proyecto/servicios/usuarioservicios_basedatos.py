import sqlite3
from entidades.usuario import Usuario
import interfaces.iUsuario
import servicios.reconocimientoFacial
from interfaces.ESTANDARES import *

def agregar_usuario(usuario, imagen):
        try:
            consulta = "INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?)"
            print("consulta")
            print(usuario.getNombre(),usuario.getApellido(),usuario.getCarnetConducir(),usuario.getFechaNacimiento(),usuario.getCorreo(),usuario.getCuil())
            parametros = (usuario.getNombre(),usuario.getApellido(),usuario.getCarnetConducir(),usuario.getFechaNacimiento(),usuario.getCorreo(),usuario.getCuil(), imagen)
            print("parametros")
            resultado = ejecutar_consulta(consulta,parametros)
            print("resultados")
            if (resultado != None):
                MENSAJE_INFO("Se a guardado el usuario en la base de datos")
        except Exception:
            MENSAJE_ERROR("Hay un error al agregar un usuario")

def ejecutar_consulta(consulta, parametros = ()):
    print("ejecutar")

    try:
        with sqlite3.connect(direccion_base_datos) as conn:
            cursor = conn.cursor()
            print("cursor")
            resultado = cursor.execute(consulta, parametros)
            print("resultado")
            conn.commit()
    except sqlite3.OperationalError:
        MENSAJE_INFO("No se pudo acceder a la base de datos!")
    return resultado
