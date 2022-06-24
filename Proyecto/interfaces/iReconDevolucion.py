'''
    Interfaz de Usuario para inisiar sesión mediante reconocimiento facial.
    @author Bulos & Vargas
'''
# ------------------------------------------------------------------------------
from tkinter import Frame, Label, Entry, Button, messagebox, Tk

import sqlite3
from interfaces.iDevolucion import VentanaDevolucion
from servicios.reconocimientoFacial import login_capture
# ------------------------------------------------------------------------------
class ReconDev():

    '''
        Procedimiento para el Button Volver
    '''
    def actionVolver(self):
        from interfaces.iPrimerPantalla import Ventana1
        self.root.withdraw()
        ventana = Ventana1(Tk())

    '''
        Procedimiento para validar un Usuario
    '''
    def validarUsuario(self):
        if (self.idCuil.get()):
            if (self.buscarUsuario()):
                self.root.withdraw()
                #login_capture(self.idCuil.get())
                #ventana = VentanaDevolucion(Tk(), self.idCuil.get())
            else:
                messagebox.showwarning(
                    "Usuario sin operacion", "No hay alquileres pendientes para este usuario")
                self.idCuil.focus()
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.idCuil.focus()

    '''
        Función para buscar un Usuario
    '''
    def buscarUsuario(self):
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute("SELECT IdCuil FROM Alquileres WHERE IdCuil=?", (self.idCuil.get(),))
        datos = cur.fetchall()
        con.close()
        return datos

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
        self.idCuil = Entry(frame2, width=20)
        self.idCuil.place(x=100, y=20, height=25)
        self.idCuil.focus_force()

        # Button
        Button(frame2, text="Volver", command=self.actionVolver).place(x=50, y=150, anchor="center")
        Button(frame2, text="Capturar Rostro", command=self.validarUsuario).place(x=250, y=100, anchor="center", width=200, height=50)

        root.mainloop()
