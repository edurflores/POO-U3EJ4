from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldoBasico = 0.0
    __antiguedad = 0
    __sueldototal = 0.0 # A calcular
    def __init__(self,docu,nom,direc,tel,sueldoba,anti):
        super().__init__(docu, nom, direc, tel)
        self.__sueldoBasico = sueldoba
        self.__antiguedad = anti
        self.__sueldototal = self.__sueldoBasico + ((self.__sueldoBasico * 1)/100) * self.__antiguedad
    def GetSueldoBasico(self):
        return self.__sueldoBasico
    def GetAntiguedad(self):
        return self.__antiguedad
    def GetSueldoTotal(self):
        return self.__sueldototal