from entidades.usuario import Usuario
from servicios.vehiculoservicio import *
import re


class UsuarioServicio():

    def cuandoEscriba_correo(self,texto):
        try:
            patron = re.compile(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{1,3}$')
            return re.search(patron, texto)
        except  ValueError:
            return False

    def isStringVacio(self, cadena):
        return (cadena.isspace() or cadena == "")

    def validarString(self, cadena):
        return (cadena.isalpha())

    def validarAlfa(self,candena):
        return (cadena.isdigit()) or (cadena.isalpha())

    def validarStringAlfa (self, cadena):
        return (cadena.isspace()) or (cadena == "") or (cadena.isdigit()) or (cadena.isalpha())

    def validarDNI(self, numero):
        try:
            if(len(numero) > 6 and len(numero) < 9 ):
                return True
        except ValueError:
            return False

    def validarCUIL(self, numero):
        try:
            if(len(numero) > 9 and len(numero) < 12 ):
                return True
        except ValueError:
            return False

    def compararDNI_CUIL(self, cuil, carnetConducir):
        if(carnetConducir == cuil[2:10]):
            return True
        else:
            return False
    def validarLongitudFecha(self, numero):
        try:
            return len(numero) == 10
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

    def isEnteroPositivo(self, numero):
        try:
            numero = int(numero)
        except ValueError:
            return False
        else:
            return numero > 1

    def validarFecha(self,texto):
        try:
            if (texto[2]  == "/" and texto[5] == "/"):
                if(int(texto[0:2]) > 0 and  int(texto[0:2]) < 32):
                    if(int(texto[3:5]) > 0 and  int(texto[3:5]) < 13):
                        if(int(texto[6:10]) > 1931 and  int(texto[6:10]) < 2002):
                            return True
        except ValueError:
            return False
            
