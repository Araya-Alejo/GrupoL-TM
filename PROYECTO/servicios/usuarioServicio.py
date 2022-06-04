from entidades.usuario import Usuario
from servicios.vehiculoservicio import *


class UsuarioServicio():


    def validarString(self, cadena):
        return (cadena.isspace()) or (cadena == "")

    def validarAlfa(self,candena):
        return (cadena.isdigit()) or (cadena.isalpha())

    def validarStringAlfa (self, cadena):
        return (cadena.isspace()) or (cadena == "") or (cadena.isdigit()) or (cadena.isalpha())

    def validarDNI(self, numero):
        try:
            numero = int(numero)
            if(numero > 6 and numero < 9 ):
                return True
        except ValueError:
            return False

    def validarCUIL(self, numero):
        try:
            numero = int(numero)
            if(numero > 9 and numero < 12 ):
                return True
        except ValueError:
            return False

    def validarLomgitudFecha(self, numero):
        try:
            if(len(numero) == 10 ):
                return True
        except ValueError:
            return False


    def validarInt(self, numero):
        try:
            numero = int(numero)
        except ValueError:
            return False
        else:
            return numero > 0

    def validarFloat(self, numero):
        try:
            numero = float(numero)
        except ValueError:
            return False
        else:
            return numero > 0.0
