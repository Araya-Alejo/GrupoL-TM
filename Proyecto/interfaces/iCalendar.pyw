from tkinter import *
from tkcalendar import *

class  VentanaCalendario:

    def obtenerFecha():
        return calendar.get_date()

    def __init__(self, ventana):
        self.ventana = ventana
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()
        ancho2 = 800
        alto2 = 600
        izquierda = (ancho - ancho2) / 2
        arriba = (alto - alto2) / 2
        self.ventana.geometry("%dx%d+%d+%d" % (ancho2, alto2, izquierda, arriba))
        self.ventana.title("Calendario")
        self.ventana.resizable(False, False)

        calendar = Calendar(ventana, selectmode ="day", year=2020,month=5,day=22)
        calendar.pack(pady=20)

        self.boton = tk.Button(area, text = 'Seleccionar fecha', font= ("Bahnschrift Light",10), command = self.obtenerFecha )
        self.boton.pack(pady = 5)

        ventana.mainloop()
