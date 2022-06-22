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

def write_file(data, path):
    # Convert binary data to proper format and write it on your computer
    with open(path, 'wb') as file:
        file.write(data)




# RETURN PHOTO
# SHOW THE VIDEO
'''
def obtener_usuario(cuil,path):
    try:
        consulta = "INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?)"
        parametros = (cuil,)
        with sqlite3.connect(direccion_base_datos) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(consulta, parametros)

            for row in records:
                id = row[0]
                write_file(row[2], path)
            rows = len(records)

            #records = cursor.fetchall()
            conn.commit()











    try:
    con = db.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
    cursor = con.cursor()
    sql = "SELECT * FROM `user` WHERE name = %s"

    cursor.execute(sql, (name,))
    records = cursor.fetchall()


    except db.Error as e:
        print(f"Failed to read image: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"id": id, "affected": rows}
'''
