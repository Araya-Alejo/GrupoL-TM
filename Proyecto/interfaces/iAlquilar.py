from tkinter import Tk, Frame, Label, Button, ttk

from interfaces.iAgregarVehiculo import VentanaAgregarVehiculo
from servicios.alquilarServicio import mostrarVehiculoDisponible


class VentanaAlquilar():

    '''
        Procedimiento para el Button Agregar.
        Muestra la ventana para cargar datos del Vehiculo.
    '''

    def pago(self):
        ventanaPago = EJEMPLOVentanaPago(Tk())

    def actionVolver(self):
        from interfaces.iPrimerPantalla import Ventana1

        self.root.withdraw()
        ventanaPrincipal = Ventana1(Tk())

    '''
        Método Constructor
    '''

    def __init__(self, root):
        # Ventana
        self.root = root
        # Obtiene ancho del área de visualización.
        screenWidth = root.winfo_screenwidth()
        # Obtiene altura del área de visualización.
        screenHeight = root.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 800
        # Establece altura de la ventana.
        height = 600
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        # Ancho x Alto + Desplazamiento x + Desplazamiento y
        root.geometry("%dx%d+%d+%d" % (width, height, left, top))
        root.title("Alquilar Vehículo")
        root.resizable(False, False)

        self.initComponents(root)

    '''
        Procedimiento que inicializa los componentes gráficos.
    '''

    def initComponents(self, root):
        # Frame
        frame1 = Frame(root, width="100", height="50")
        frame1.pack(expand=False, fill="both")

        frame2 = Frame(root, width="100", height="100")
        frame2.pack(expand=False, fill="both")

        frame3 = Frame(root, width="100", height="450")
        frame3.pack(expand=True, fill="both")

        # Label
        Label(frame1, text="Alquilar", font=("Bahnschrift SemiLight", 20)).place(
            x=400, y=25, anchor="center")

        # Treeview
        self.tree = ttk.Treeview(frame3, height=20, columns=[
                                 f"#{n}" for n in range(1, 7)])
        self.tree.heading("#0", text="Clasifiación")
        self.tree.heading("#1", text="Marca")
        self.tree.heading("#2", text="Modelo")
        self.tree.heading("#3", text="Generación")
        self.tree.heading("#4", text="Matricula")
        self.tree.heading("#5", text="Kilómetros")
        self.tree.heading("#6", text="Precio")

        self.tree.column("#0", minwidth=0, width=105)
        self.tree.column("#1", minwidth=0, width=95)
        self.tree.column("#2", minwidth=0, width=95)
        self.tree.column("#3", minwidth=0, width=95)
        self.tree.column("#4", minwidth=0, width=95)
        self.tree.column("#5", minwidth=0, width=95)
        self.tree.column("#6", minwidth=0, width=95)

        self.tree.place(x=400, y=225, anchor="center")

        # Button

        Button(frame2, text="Alquilar", width=10, height=1,
               command=self.pago).place(x=400, y=40, anchor="center")

        Button(frame1, text="Volver", width=10, height=1,
               command=self.actionVolver).place(x=40, y=25, anchor="center")

        # Database
        mostrarVehiculoDisponible(self.tree)

        root.mainloop()
