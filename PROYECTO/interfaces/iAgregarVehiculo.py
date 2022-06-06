'''
    Interfaz Administrador para agregar Vehiculo
    @author Bulos
'''
# ------------------------------------------------------------------------------
from tkinter import Tk, Frame, Label, Button, Entry, ttk, messagebox

from entidades.vehiculo import Vehiculo
from servicios.vehiculoservicio_basedatos import add_vehiculo, validate_vehiculo
from servicios.vehiculoservicio import VehiculoServicio
# ------------------------------------------------------------------------------
class VentanaAgregarVehiculo():

    '''
        Procedimiento que limpia la pantalla (Combobox y Entry).
    '''
    def limpiar(self):
        self.comboClasificacion.delete(0, "end")
        self.comboMarca.delete(0, "end")
        self.entryModelo.delete(0, "end")
        self.entryGeneracion.delete(0, "end")
        self.entryMatricula.delete(0, "end")
        self.entryKm.delete(0, "end")
        self.entryPrecio.delete(0, "end")

    '''
        Procedimiento para el Button Cancelar.
        Destuye la ventana actual.
    '''
    def cancelar(self):
        self.root.destroy()

    '''
        Función que valida los campos ingresados.
        Coloca un Label a todos aquellos campos incorrectos.
        Retorna un bool.
    '''
    def validar(self):
        vs = VehiculoServicio()
        band = True

        # Validación Clasifiación
        if (vs.isStringVacio(self.comboClasificacion.get())):
            self.labelClasificacion["text"] = "Incorrecto"
            band = False
        else:
            self.labelClasificacion["text"] = ""

        # Validación Marca
        if (vs.isStringVacio(self.comboMarca.get())):
            self.labelMarca["text"] = "Incorrecto"
            band = False
        else:
            self.labelMarca["text"] = ""

        # Validación Modelo
        if (vs.isStringVacio(self.entryModelo.get()) or
            (not vs.isStringAlfaNumerico(self.entryModelo.get()))):
            self.labelModelo["text"] = "Incorrecto"
            band = False
        else:
            self.labelModelo["text"] = ""

        # Validación Generación
        if (not vs.isEnteroPositivo(self.entryGeneracion.get())):
            self.labelGeneracion["text"] = "Incorrecto"
            band = False
        else:
            self.labelGeneracion["text"] = ""

        # Validación Matricula
        if (not vs.isMatricula(self.entryMatricula.get(), self.entryGeneracion.get())):
            self.labelMatricula["text"] = "Incorrecto"
            band = False
        else:
            self.labelMatricula["text"] = ""

        # Validación Kilómetros
        if (not vs.isDecimalPositivo(self.entryKm.get())):
            self.labelKm["text"] = "Incorrecto"
            band = False
        else:
            self.labelKm["text"] = ""

        # Validación Precio
        if (not vs.isDecimalPositivo(self.entryPrecio.get())):
            self.labelPrecio["text"] = "Incorrecto"
            band = False
        else:
            self.labelPrecio["text"] = ""

        return band

    '''
        Procedimiento para el Button Aceptar.
        Si la validacion es correcta, crea un Vehiculo y lo ingresa a la db, en
            caso contrario avisa mediante un mensaje.
    '''
    def aceptar(self):
        if (self.validar()):
            if (not validate_vehiculo(self.entryMatricula.get())):
                add_vehiculo(Vehiculo(self.comboClasificacion.get(),
                    self.comboMarca.get(), self.entryModelo.get(),
                    self.entryGeneracion.get(), self.entryMatricula.get(),
                    self.entryKm.get(), self.entryPrecio.get(), False), self.root)
                self.limpiar()
            else:
                messagebox.showinfo(message="El vehiculo ya ha sido ingresado!", title="", parent=self.root)
        else:
            messagebox.showinfo(message="No se pudo agregar el vehiculo!", title="", parent=self.root)

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

        self.initComponents(root)

    '''
        Procedimiento que inicializa los componentes gráficos.
    '''
    def initComponents(self, root):
        # Frame
        frame1 = Frame(root, width="100", height="50")
        frame1.pack(expand=False, fill="both")

        frame2 = Frame(root, width="100", height="400")
        frame2.pack(expand=False, fill="both")

        # Label
        Label(frame1, text="Introducir los siguientes datos:", font=("Bahnschrift SemiLight", 20)).place(x=400, y=25, anchor="center")
        Label(frame2, text="CLASIFICACIÓN: ", font=("Bahnschrift Light", 10)).place(x=50, y=30)
        Label(frame2, text="MARCA: ", font=("Bahnschrift Light", 10)).place(x=50, y=70)
        Label(frame2, text="MODELO: ", font=("Bahnschrift Light", 10)).place(x=50, y=110)
        Label(frame2, text="GENERACIÓN: ", font=("Bahnschrift Light", 10)).place(x=50, y=150)
        Label(frame2, text="MATRICULA: ", font=("Bahnschrift Light", 10)).place(x=50, y=190)
        Label(frame2, text="KILÓMETROS: ", font=("Bahnschrift Light", 10)).place(x=50, y=230)
        Label(frame2, text="PRECIO DE ALQUILER: ", font=("Bahnschrift Light", 10)).place(x=50, y=270)

        # Label (Salida)
        self.labelClasificacion = Label(frame2, text="", fg="red")
        self.labelClasificacion.place(x=350, y=30)

        self.labelMarca = Label(frame2, text="", fg="red")
        self.labelMarca.place(x=350, y=70)

        self.labelModelo = Label(frame2, text="", fg="red")
        self.labelModelo.place(x=350, y=110)

        self.labelGeneracion = Label(frame2, text="", fg="red")
        self.labelGeneracion.place(x=350, y=150)

        self.labelMatricula = Label(frame2, text="", fg="red")
        self.labelMatricula.place(x=350, y=190)

        self.labelKm = Label(frame2, text="", fg="red")
        self.labelKm.place(x=350, y=230)

        self.labelPrecio = Label(frame2, text="", fg="red")
        self.labelPrecio.place(x=350, y=270)

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
