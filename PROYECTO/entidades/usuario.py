class Usuario():

    # Constructor
    def __init__(self, nombre, apellido, carnetConducir,
                 fechaNacimiento, correo, esExtranjero, cuil, pasaporte):
        self.__nombre = nombre  # String
        self.__apellido = apellido  # String
        self.__carnetConducir = carnetConducir  # Alfanumerico
        self.__fechaNacimiento = fechaNacimiento  # int
        self.__correo = correo  # Alfanumerico
        self.__esExtranjero = esExtranjero  # Boolean
        self.__cuil = cuil  # int
        self.__pasaporte = pasaporte  # Alfanumerico

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

    def getEsExtranjero(self):
        return self.__esExtranjero

    def getCuil(self):
        return self.__cuil

    def getPasaporte(self):
        return self.__pasaporte

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

    def setEsExtranjero(self, esExtranjero):
        self.__esExtranjero = esExtranjero

    def setCuil(self, cuil):
        self.__cuil = cuil

    def setPasaporte(self, pasaporte):
        self.__pasaporte = pasaporte
