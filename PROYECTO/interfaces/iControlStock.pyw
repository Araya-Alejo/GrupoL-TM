from tkinter import Tk, Frame, Label, Button, ttk

from alquilaya_interfaces.iAgregarVehiculo import VentanaAgregarVehiculo
# ------------------------------------------------------------------------------
class VentanaControlStock():

    '''
        Procedimiento para el Button Agregar.
        Muestra una ventana para cargar datos.
    '''
    def agregar(self):
        ventanaDatos = VentanaAgregarVehiculo(Tk())

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
        root.geometry("%dx%d+%d+%d" % (width, height, left, top))               # Ancho x Alto + Desplazamiento x + Desplazamiento y
        root.title("Control Stock")
        root.resizable(False, False)

        # Frame
        frame1 = Frame(root, width="100", height="50")
        frame1.pack(expand=False, fill="both")

        frame2 = Frame(root, width="100", height="100")
        frame2.pack(expand=False, fill="both")

        frame3 = Frame(root, width="100", height="450")
        frame3.pack(expand=True, fill="both")

        # Label
        Label(frame1, text="Control Stock", font=("Bahnschrift SemiLight", 20)).place(x=400, y=25, anchor="center")

        # Button
        Button(frame2, text="Agregar", width=10, height=1, command=self.agregar).place(x=200, y=50, anchor="center")
        Button(frame2, text="Eliminar", width=10, height=1,).place(x=400, y=50, anchor="center")
        Button(frame2, text="Modificar", width=10, height=1,).place(x=600, y=50, anchor="center")

        # Treeview
        self.tree = ttk.Treeview(frame3, height=20, columns=[f"#{n}" for n in range(1, 7)])
        self.tree.heading("#0", text="Tipo")
        self.tree.heading("#1", text="Marca")
        self.tree.heading("#2", text="Modelo")
        self.tree.heading("#3", text="Generación")
        self.tree.heading("#4", text="Matricula")
        self.tree.heading("#5", text="Kilómetros")
        self.tree.heading("#6", text="Precio")

        self.tree.column("#0", minwidth=0, width=110)
        self.tree.column("#1", minwidth=0, width=110)
        self.tree.column("#2", minwidth=0, width=110)
        self.tree.column("#3", minwidth=0, width=110)
        self.tree.column("#4", minwidth=0, width=110)
        self.tree.column("#5", minwidth=0, width=110)
        self.tree.column("#6", minwidth=0, width=120)

        self.tree.place(x=400, y=225, anchor="center")

        root.mainloop()
