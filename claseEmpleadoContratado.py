from datetime import date
from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fechainicio = date
    __fechafin = date
    __cantHoras = 0
    __valorHora = 50 # Variable de clase (50 por defecto)
    __sueldo = 0.0 # A calcular
    def __init__(self,docu,nom,direc,tel,fechaini,fechafin,cahoras):
        super().__init__(docu, nom, direc, tel)
        self.__fechainicio = fechaini
        self.__fechafin = fechafin
        if type(cahoras) is int:
            self.__cantHoras = cahoras
        self.__sueldo = self.__cantHoras * self.__valorHora
    @classmethod
    def SetValorHora(cls):
        val = float(input('Ingrese nuevo valor por hora:'))
        cls.__valorHora = val
        print('Valor por hora actualizado. Nuevo valor:',cls.__valorHora)
    def SetCantidadHoras(self,cant):
        self.__cantHoras += cant
        print('Se ha actualizado la cantidad de horas trabajadas.')
        print('Nuevo valor:',self.__cantHoras)
        self.ActualizaSueldo()
    def ActualizaSueldo(self):
        self.__sueldo = self.__cantHoras * self.__valorHora
    def GetSueldo(self):
        self.ActualizaSueldo()
        return self.__sueldo
    def GetFechaInicio(self):
        return self.__fechainicio
    def GetFechaFin(self):
        return self.__fechafin
    def GetCantidadHoras(self):
        return self.__cantHoras
    @classmethod
    def GetValorHora(cls):
        return cls.__valorHora
