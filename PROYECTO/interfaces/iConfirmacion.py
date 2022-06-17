import tkinter as tk  # biblioteca para diseniar interfaz
from tkinter import *  # botones tablas .. etc
#from servicios.conexionPago import Conexion
import sqlite3  # modulo para conexion
from tkinter import messagebox
from interfaces.ESTANDARES import *
from servicios.mail import *
from servicios.SO import *

# clase pago va a tener todos los metodos de mi ventana (titulo botones, entradas dde texto) funcionalidad de nuestras ventanas


class ConfirPago:

    def __init__(self, window, mensaje, email):
        self.wind = window
        self.wind.title("Alquila Ya")
        # Obtiene ancho del área de visualización.
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 800
        # Establece altura de la ventana.
        height = 600
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.wind.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.wind.resizable(0, 0)

        #Creacion del Frame
        frame = LabelFrame(self.wind)
        frame.place(relwidth=1, relheight=1)

        #Creacion de los Label de etiqueta
        tk.Label(frame, text="CONFIRMACION Auto Alquilado").place(                                                                        relx=0.40, rely=0.40)                               # --->

        self.labelValidacion = tk.Label(frame, text="A continuacion se le enviará un email informando la confirmacion del alquiler").place(relx=0.2, rely=0.50)
        #print(mensaje)
        ENVIAR_CORREO(email)

        #Creacion de los Botones
        tk.Button(frame, text="Salir",command=window.destroy).place(relx=0.60, rely=0.70)
        tk.Button(frame, text="Volver a Pagina de inicio", command=self.atras).place(relx=0.30, rely=0.7)



        window.mainloop()
        """
                                                                                                                                                                ---fin
        """
    def atras(self):
        self.wind.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj= Ventana1(Tk())
