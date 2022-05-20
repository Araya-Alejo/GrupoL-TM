from entidades.vehiculo import Vehiculo
# ------------------------------------------------------------------------------
class VehiculoServicio():

    '''
        Función que valida si una cadena esta vacía o no.
        Retorna un bool.
    '''
    def validarString(self, cadena):
        return (cadena.isspace()) or (cadena == "")

    '''
        Función que valida si una cadena contiene números y caracteres.
        Retorna un bool.
    '''
    def validarStringAlfanumerica(self, cadena):
        return (cadena.isspace()) or (cadena == "") or (cadena.isdigit()) or (cadena.isalpha())

    '''
        Función que valida que un número entero sea positivo.
        Retorna un bool.
    '''
    def validarInt(self, numero):
        try:
            numero = int(numero)
        except ValueError:
            return False
        else:
            return numero > 1

    '''
        Función que valida que un número decimal sea positivo.
        Retorna un bool.
    '''
    def validarFloat(self, numero):
        try:
            numero = float(numero)
        except ValueError:
            return False
        else:
            return numero > 1.0

    '''
        Función que valida que una cadena sea del tipo 'AAA111' o 'AA111AA'
        Retorna un bool.
    '''
    def validarMatricula(self, cadena, generacion):
        cadena = cadena.replace(" ", "")

        if(self.validarInt(generacion)):
            if(int(generacion) >= 2016):
                if(len(cadena) == 7):
                    return (cadena[0:2].isalpha() and cadena[2:5].isdigit() and cadena[5:].isalpha())
            else:
                if(len(cadena) == 6):
                    return (cadena[0:3].isalpha() and cadena[3:].isdigit())
        return False
