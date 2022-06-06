from tkinter import *
from tkcalendar import *

def obtenerFecha():
    label.config(text=calendar.get_date())
    # return calendar.get_date()

class  VentanaCalendario:

    def __init__(self, ventana):
        global calendar
        global label

        self.ventana = ventana
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()
        ancho2 = 800
        alto2 = 600
        izquierda = (ancho - ancho2) / 2
        arriba = (alto - alto2) / 2
        ventana.geometry("%dx%d+%d+%d" % (ancho2, alto2, izquierda, arriba))
        ventana.title("Calendario")
        ventana.resizable(False, False)


        calendar = Calendar(ventana, selectmode ="day", year=2022,month=5,day=21)
        calendar.pack(pady=20)

        boton = Button(ventana, text = 'Seleccionar fecha', font= ("Bahnschrift Light",10), command = obtenerFecha )
        boton.pack(pady = 5)


        label = Label(ventana, text = "")
        label.pack(pady = 20)

        ventana.mainloop()
