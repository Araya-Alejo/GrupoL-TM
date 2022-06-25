import sqlite3
import interfaces.iUsuario
from interfaces.ESTANDARES import *
from entidades.usuario import Usuario

'''
AGREGAR USUARIO
'''
def agregar_usuario(usuario, imagen):
        try:
            consulta = "INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?)"
            MENSAJE_CONSOLA("CONSULTA", visible)
            from servicios.reconocimientoFacial import convertirABinario
            imagenBinario = convertirABinario(imagen)
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

'''
PETICION A LA BASE DE DATOS
'''
def ejecutar_consulta(consulta, parametros = ()):
    print("ejecutar")

    try:
        with sqlite3.connect(direccion_base_datos) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(consulta, parametros)
            conn.commit()
    except sqlite3.OperationalError:
        MENSAJE_INFO("No se pudo acceder a la base de datos!")
    return resultado

'''
RETORNAR IMAGEN
'''
def obtener_usuario(cuil, path):
    from servicios.reconocimientoFacial import escribirArchivo
    consulta = "SELECT * FROM Usuarios WHERE Cuil = ?"

    try:
        with sqlite3.connect(direccion_base_datos) as conn:
            cursor = conn.cursor()
            cursor.execute(consulta, (cuil,))

            if (results:= cursor.fetchone()) is not None:
                escribirArchivo(results[6], path)
                return 1

    except sqlite3.OperationalError:
        print("¡Error al ingresar a la db!")
        return 0
