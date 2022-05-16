from tkinter import Tk, Frame, Label, Button, Entry, ttk

from alquilaya_servicios.vehiculoservicio import VehiculoServicio
# ------------------------------------------------------------------------------
vs = VehiculoServicio()
# ------------------------------------------------------------------------------
class VentanaAgregarVehiculo():

    '''
        Procedimiento para el Button Cancelar.
        Destruye la ventana actual.
    '''
    def cancelar(self):
        self.root.destroy()

    '''
        Procedimiento para el Button Aceptar.
        Obtiene todos los campos.
    '''
    def aceptar(self):
        if(not vs.validarString(self.comboClasificacion.get())):
            self.labelClasificacion.tk.configure(text="Bien")
        else:
            print("Clasificacion: Mal")

        if(not vs.validarString(self.comboMarca.get())):
            print("Marca: Bien")
        else:
            print("Marca: Mal")

        if(not vs.validarString(self.entryModelo.get())):
            print("Modelo: Bien")
        else:
            print("Modelo: Mal")

        if(vs.validarInt(self.entryGeneracion.get())):
            print("Generacion: Bien")
        else:
            print("Generacion: Mal")

        if(vs.validarMatricula(self.entryMatricula.get(), self.entryGeneracion.get())):
            print("Matricula: Bien")
        else:
            print("Matricula: Mal")

        if(vs.validarInt(self.entryKm.get())):
            print("Km: Bien")
        else:
            print("Km: Mal")

        if(vs.validarFloat(self.entryPrecio.get())):
            print("Precio: Bien")
        else:
            print("Precio: Mal")

    '''
        Método Constructor.
    '''
    def __init__(self, root):
        # Ventana
        self.root = root
        screenWidth = root.winfo_screenwidth()                                  # Obtiene ancho del área de visualización.
        screenHeight = root.winfo_screenheight()                                # Obtiene altura del área de visualización.
        width = 800                                                             # Establece ancho de la ventana.
        height = 600                                                            # Establece altura de la ventana.
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, left, top))          # Ancho x Alto + Desplazamiento x + Desplazamiento y
        self.root.title("Agregar Vehiculo")
        self.root.resizable(False, False)

        # Frame
        frame1 = Frame(root, width="100", height="50")
        frame1.pack(expand=False, fill="both")

        frame2 = Frame(root, width="100", height="400")
        frame2.pack(expand=False, fill="both")

        # Label
        Label(frame1, text="Introducir los siguientes datos:", font=("Bahnschrift SemiLight", 20)).place(x=400, y=25, anchor="center")

        Label(frame2, text="CLASIFICACIÓN: ", font=("Bahnschrift Light", 10)).place(x=50, y=30)
        self.labelClasificacion = Label(frame2, text="", fg="red").place(x=350, y=30)

        Label(frame2, text="MARCA: ", font=("Bahnschrift Light", 10)).place(x=50, y=70)
        self.labelMarca = Label(frame2, text="", fg="red").place(x=350, y=70)

        Label(frame2, text="MODELO: ", font=("Bahnschrift Light", 10)).place(x=50, y=110)
        self.labelModelo = Label(frame2, text="", fg="red").place(x=350, y=110)

        Label(frame2, text="GENERACIÓN: ", font=("Bahnschrift Light", 10)).place(x=50, y=150)
        self.labelGeneracion = Label(frame2, text="", fg="red").place(x=350, y=150)

        Label(frame2, text="MATRICULA: ", font=("Bahnschrift Light", 10)).place(x=50, y=190)
        self.labelMatricula = Label(frame2, text="", fg="red").place(x=350, y=190)

        Label(frame2, text="KILÓMETROS: ", font=("Bahnschrift Light", 10)).place(x=50, y=230)
        self.labelKm= Label(frame2, text="", fg="red").place(x=350, y=230)

        Label(frame2, text="PRECIO DE ALQUILER: ", font=("Bahnschrift Light", 10)).place(x=50, y=270)
        self.labelPrecio = Label(frame2, text="", fg="red").place(x=350, y=270)

        # Conmbobox
        opcTipo = ["SUV", "COUPE", "SEDAN", "PICKUP", "URBANO", "DEPORTIVO",
                "FURGONETA", "TODOTERRENO", "DESCAPOTABLE", "MONOVOLUMEN"]
        self.comboClasificacion = ttk.Combobox(frame2, values=opcTipo, state="readonly")
        self.comboClasificacion.place(x=200, y=30, height=24)

        opcMarca = ["FIAT","AUDI","BMW","FORD","NISSAN","TOYOTA","RENAULT",
                "PEUGEOT", "PORSCHE","CHEVROLET","VOLKSWAGEN","MERCEDES-BENZ"]
        self.comboMarca = ttk.Combobox(frame2, values=opcMarca, state="readonly")
        self.comboMarca.place(x=200, y=70, height=24)

        # Entry
        self.entryModelo = Entry(frame2, width=23)
        self.entryModelo.place(x=200, y=110, height=22)

        self.entryGeneracion = Entry(frame2, width=23)
        self.entryGeneracion.place(x=200, y=150, height=22)

        self.entryMatricula = Entry(frame2, width=23)
        self.entryMatricula.place(x=200, y=190, height=22)

        self.entryKm = Entry(frame2, width=23)
        self.entryKm.place(x=200, y=230, height=22)

        self.entryPrecio = Entry(frame2, width=23)
        self.entryPrecio.place(x=200, y=270, height=22)

        # Button
        Button(frame2, text="Cancelar", width=10, height=1, command=self.cancelar).place(x=50, y=325)
        Button(frame2, text="Aceptar", width=10, height=1, command=self.aceptar).place(x=200, y=325)

        root.mainloop()
