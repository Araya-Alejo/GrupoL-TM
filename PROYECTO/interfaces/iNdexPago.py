from tkinter import ttk  # biblioteca para diseniar interfaz
from tkinter import *  # botones tablas .. etc
from conexionPago import Conexion  # de modulo conexion importa la clase Conexion

import sqlite3  # modulo para conexion

# clase pago va a tener todos los metodos de mi ventana (titulo botones, entradas dde texto) funcionalidad de nuestras ventanas


class Pago:

    def boton(self):
        ventana2 = Conexion(Tk())

    def __init__(self, myVentana):  # funcion (constructor de nuestra clase)
        self.ventana = myVentana  # wind (almacenar ventana como parametro)
        self.ventana.title('Pago')  # titulo de la ventana

        # Obtiene ancho del área de visualización.
        screenWidth = myVentana.winfo_screenwidth()
        # Obtiene altura del área de visualización.
        screenHeight = myVentana.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 800
        # Establece altura de la ventana.
        height = 600
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        # Ancho x Alto + Desplazamiento x + Desplazamiento y
        myVentana.geometry("%dx%d+%d+%d" % (width, height, left, top))

        # -----------------CONTENEDOR-----------------
        # interfaz creo un contenedor (Frame)
        # elemento de bibioteca ttk lo asignamos a la variable frame
        # elemento que provee la libreria ttk
        contenedor = LabelFrame(self.ventana, text='agregar un Pago')
        contenedor.grid(row=20, column=20, columnspan=3, pady=20)  # metodo grid(posicionamiento)
        #               fila  , columna   desplazar columnas , espaciado/relleno
        # ----------------------------------

        # entrada para nombre(caja de texto etiqueta)

        # Label(frame, text='Name').grid(row=1, column=0)  # metodo Label      fila 1, texto
        # self.name = Entry(frame)  # entrada
        # self.name.focus()
        # self.name.grid(row=1, column=1)  # metodo grid(posicionamiento)

        # boton de Pago
        ttk.Button(contenedor, text='Pagando', command=self.boton).grid(
            row=3, columnspan=2, sticky=W+E)

        myVentana.mainloop()  # final **ejecutar ventana


if __name__ == '__main__':  # arrancar app
    # myVentana = Tk()  # ejecutar tk me devuelve ventana(de app)
    app = Pago(Tk())
