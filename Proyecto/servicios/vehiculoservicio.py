'''
    Clase Servicio para Vehiculo
    @author Bulos
'''
# ------------------------------------------------------------------------------
class VehiculoServicio():

    '''
        Función que valida si una cadena esta vacía.
        Retorna un bool.
    '''
    def isStringVacio(self, cadena):
        return (cadena.isspace() or cadena == "")

    '''
        Función que valida si una cadena es alfanumerica.
        Retorna un bool.
    '''
    def isStringAlfaNumerico(self, cadena):
        return cadena.isalnum()

    '''
        Función que valida que un número entero sea positivo.
        Retorna un bool.
    '''
    def isEnteroPositivo(self, numero):
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
    def isDecimalPositivo(self, numero):
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
    def isMatricula(self, cadena, generacion):
        cadena = cadena.replace(" ", "")

        if(self.isEnteroPositivo(generacion)):
            if(int(generacion) >= 2016):
                if(len(cadena) == 7):
                    return (cadena[0:2].isalpha() and cadena[2:5].isdigit() and cadena[5:].isalpha())
            else:
                if(len(cadena) == 6):
                    return (cadena[0:3].isalpha() and cadena[3:].isdigit())
        return False
