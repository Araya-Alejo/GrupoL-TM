
try:
    from tkinter import Tk
    from interfaces.iPrimerPantalla import Ventana1
except ModuleNotFoundError:
    print("Error")
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    ventana = Ventana1(Tk())
