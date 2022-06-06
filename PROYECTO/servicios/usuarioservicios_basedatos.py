
import sqlite3
from entidades.usuario import Usuario
import interfaces.iUsuario

def ejecutar_consulta(self, consulta, parametros = ()):
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

def agregar_usuario(self):
        try:
            print("agregar usuario")
            if self.validar():
                MessageBox.showinfo(" ", "Se a guardado el usuario en la base de datos")
                consulta = 'INSERT INTO Usuarios VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
                parametros = (self.nombre.get(),self.apellido.get(),self.carnetConducir.get(),self.fechaNacimiento.get(),self.correo.get(),self.extranjero.get(),self.cuil.get(),self.pasaporte.get())
                self.ejecutar_consulta(consulta,parametros)
        except Exception:
            MessageBox.showwarning("Alerta", "Hay valores fue erroneo")
