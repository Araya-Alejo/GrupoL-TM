class Alquiler:

    def __init__(self, usuarioCuil, vehiculoMatricula, fechaAlquiler, cantDias,
                precioTotal, numAlquiler):
        self.__idCuil = usuarioCuil
        self.__idMatricula = vehiculoMatricula
        self.__fechaAlquiler = fechaAlquiler
        self.__cantDias = cantDias
        self.__precioTotal = precioTotal
        self.__numOperacion = numAlquiler

    #Getters

    def getIdCuil(self):
        return self.__idCuil

    def getIdMatricula(self):
        return self.__idMatricula

    def getFechaAlquiler(self):
        return self.__fechaAlquiler

    def getCantDias(self):
        return self.__cantDias

    def getPrecioTotal(self):
        return self.__precioTotal

    def getNumOperacion(self):
        return self.__numOperacion


    #Setters

    def setIdCuil(self, idCuil):
        self.__idCuil = idCuil

    def setIdMatricula(self, idMatricula):
        self.__idMatricula = idMatricula

    def setFechaAlquiler(self, fechaAlquiler):
        self.__fechaAlquiler = fechaAlquiler

    def setCantDias(self, cantDias):
        self.__cantDias = cantDias

    def setPrecioTotal(self, precioTotal):
        self.__precioTotal = precioTotal

    def setNumOperacion(self, numOperacion):
        self.__numOperacion = numOperacion
