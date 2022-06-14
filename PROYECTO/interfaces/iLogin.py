'''
    Interfaz de Usuario para inisiar sesión mediante reconocimiento facial.
    @author Bulos
'''
# ------------------------------------------------------------------------------
from tkinter import Frame, Label, Entry, Button
# ------------------------------------------------------------------------------
class VentanaLoginRC():

    '''
        Método Constructor
    '''
    def __init__(self, root):
        # Ventana
        self.root = root
        screenWidth = root.winfo_screenwidth()                                  # Obtiene ancho del área de visualización.
        screenHeight = root.winfo_screenheight()                                # Obtiene altura del área de visualización.
        width = 500                                                             # Establece ancho de la ventana.
        height = 300                                                            # Establece altura de la ventana.
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        root.geometry("%dx%d+%d+%d" % (width, height, left, top))               # Ancho x Alto + Desplazamiento x + Desplazamiento y
        root.title("Iniciar Sesión")
        root.resizable(False, False)

        self.initComponents(root)

    '''
        Procedimiento que inicializa los componentes gráficos.
    '''
    def initComponents(self, root):
        # Frame
        frame1 = Frame(root, width="300", height="50")
        frame1.pack(expand=False, fill="both")

        frame2 = Frame(root, width="300", height="250")
        frame2.pack(expand=False, fill="both")

        # Label
        Label(frame1, text="Iniciar Sesión", font=("Bahnschrift SemiLight", 20)).place(x=250 ,y=25, anchor="center")
        Label(frame2, text="CUIL:", font=("Bahnschrift Light", 12)).place(x=25, y=20)

        # Entry
        self.cuil = Entry(frame2, width=20)
        self.cuil.place(x=100, y=20, height=25)
        self.cuil.focus_force()

        # Button
        Button(frame2, text="Capturar Rostro").place(x=250, y=100, anchor="center", width=200, height=50)

        root.mainloop()
