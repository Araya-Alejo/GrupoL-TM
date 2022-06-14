class Usuario():

    # Constructor
    def __init__(self,nombre, apellido, carnetConducir, fechaNacimiento, correo,cuil):
        self.__nombre = nombre  # Texto
        self.__apellido = apellido  # Texto
        self.__carnetConducir = carnetConducir  # Alfanumerico
        self.__fechaNacimiento = fechaNacimiento  # Entero
        self.__correo = correo  # Alfanumerico
        self.__cuil = cuil  # Entero


    # Getters (Métodos get)

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getCarnetConducir(self):
        return self.__carnetConducir

    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def getCorreo(self):
        return self.__correo

    def getCuil(self):
        return self.__cuil

    def getFoto(self):
        return self.__foto

    # Setters (Métodos set)

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setCarnetConducir(self, carnetConducir):
        self.__carnetConducir = carnetConducir

    def setFechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

    def setCorreo(self, correo):
        self.__correo = correo

    def setCuil(self, cuil):
        self.__cuil = cuil

    def setFoto(self, foto):
        self.__foto = foto
