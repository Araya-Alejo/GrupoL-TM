import sqlite3
from entidades.usuario import Usuario
import interfaces.iUsuario
import servicios.reconocimientoFacial as RF
from interfaces.ESTANDARES import *

def agregar_usuario(usuario, imagen):
        try:
            consulta = "INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?)"
            MENSAJE_CONSOLA("CONSULTA", visible)
            imagenBinario = RF.convertToBinaryData(imagen)
            MENSAJE_CONSOLA("BINARIO", visible)
            if(imagenBinario != 0):
                print(usuario.getNombre(),usuario.getApellido(),usuario.getCarnetConducir(),usuario.getFechaNacimiento(),usuario.getCorreo(),usuario.getCuil())
                parametros = (usuario.getNombre(),usuario.getApellido(),usuario.getCarnetConducir(),usuario.getFechaNacimiento(),usuario.getCorreo(),usuario.getCuil(), imagenBinario)
                MENSAJE_CONSOLA("PARAMETROS",visible)

                resultado = ejecutar_consulta(consulta,parametros)
                MENSAJE_CONSOLA("RESULTADOS",visible)

                if (resultado != None):
                    MENSAJE_CONSOLA("EL USUARIO FUE GUARDADO EN LA BASE DE DATOS ", visible)
            else:
                MENSAJE_CONSOLA("Return 0, it won't save the user.", visible)
        except Exception:
            MENSAJE_ERROR("HAY UN ERROR AL AGREGAR UN USUARIO")

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
