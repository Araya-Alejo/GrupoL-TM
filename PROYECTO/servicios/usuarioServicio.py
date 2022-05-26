from entidades.usuario import Usuario
# ------------------------------------------------------------------------------
class UsuarioServicio():


    def validarString(self, cadena):
        return (cadena.isspace()) or (cadena == "")

    def validarAlfa(self,candena):
        return (cadena.isdigit()) or (cadena.isalpha())

    def validarStringAlfa (self, cadena):
        return (cadena.isspace()) or (cadena == "") or (cadena.isdigit()) or (cadena.isalpha())


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
