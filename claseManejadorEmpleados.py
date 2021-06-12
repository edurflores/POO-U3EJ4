import csv
import numpy as np
from datetime import date
from claseEmpleado import Empleado
from claseEmpleadoPlanta import EmpleadoPlanta
from claseEmpleadoContratado import EmpleadoContratado
from claseEmpleadoExterno import EmpleadoExterno

class ManejadorEmpleados:
    __arreEmpleados = None
    __dimension = 0
    __indice = 0
    def __init__(self):
        self.__arreEmpleados = np.empty(self.__dimension,dtype=Empleado)
    def AgregaEmpleado(self,unEmpleado):
        if isinstance(unEmpleado, Empleado):
            self.__arreEmpleados[self.__indice] = unEmpleado
            self.__indice += 1
    def CargaEmpPlanta(self):
        archivo = open('planta.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        for fila in reader:
            if ban == False:
                ban = True # Salta primera linea
            else:
                docu = fila[0]
                nom = fila[1]
                direc = fila[2]
                tel = fila[3]
                sueldoba = float(fila[4])
                anti = int(fila[5])
                unEmpleadoPlanta = EmpleadoPlanta(docu, nom, direc, tel, sueldoba, anti)
                self.AgregaEmpleado(unEmpleadoPlanta)
        archivo.close()
        print('Empleados de planta cargados.')
    def CargaEmpContratado(self):
        archivo = open('contratados.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        for fila in reader:
            if ban == False:
                ban = True # Salta primera linea
            else:
                docu = fila[0]
                nom = fila[1]
                direc = fila[2]
                tel = fila[3]
                auxfecha = fila[4].split('/')
                fechaini = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                auxfecha = fila[5].split('/')
                fechafin = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                cahoras = int(fila[6])
                unEmpleadoContratado = EmpleadoContratado(docu, nom, direc, tel, fechaini, fechafin, cahoras)
                self.AgregaEmpleado(unEmpleadoContratado)
        archivo.close()
        print('Empleados contratados cargados.')
    def CargaEmpExterno(self):
        archivo = open('externos.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        for fila in reader:
            if ban == False:
                ban = True # Salta primera linea
            else:
                docu = fila[0]
                nom = fila[1]
                direc = fila[2]
                tel = fila[3]
                tar = fila[4]
                auxfecha = fila[5].split('/')
                fechaini = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                auxfecha = fila[6].split('/')
                fechafi = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                monviati = float(fila[7])
                costo = float(fila[8])
                monseguro = float(fila[9])
                unEmpleadoExterno = EmpleadoExterno(docu, nom, direc, tel, tar, fechaini, fechafi, monviati, costo, monseguro)
                self.AgregaEmpleado(unEmpleadoExterno)
        archivo.close()
        print('Empleados externos cargados.')
    def Carga(self):
        cant = int(input('Ingrese cantidad de empleados en total:'))
        self.__dimension = cant
        self.__arreEmpleados.resize(cant)
        self.CargaEmpPlanta()
        self.CargaEmpContratado()
        self.CargaEmpExterno()
        print('Se han cargado todos los empleados.')
    def RegistrarHoras(self): # Consigna 1
        print('Funcion registrar horas.')
        docu = input('Ingrese DNI:')
        ban = False # Bandera para indicar si encontro al empleado.
        for i in range(self.__dimension):
            if self.__arreEmpleados[i].GetDocu() == docu:
                ban = True # Encontro al empleado.
                if isinstance(self.__arreEmpleados[i], EmpleadoContratado):
                    horas = int(input('Ingrese cantidad de horas trabajadas hoy:'))
                    self.__arreEmpleados[i].SetCantidadHoras(horas)
                    break
                else:
                    print('Error. El DNI proporcionado no corresponde a un empleado contratado.')
                    break
        if ban == False:
            print('Error. No se encontro empleado con el DNI proporcionado.')
    def TotalDeTarea(self): # Consigna 2 (falta considerar las fechas)
        print('Funcion total de tarea.')
        print('Seleccione tarea.\n1- Carpinteria.\n2- Electricidad.\n3- Plomeria.')
        op = int(input('Opcion:'))
        if op == 1:
            tarea = 'Carpinteria'
        elif op == 2:
            tarea = 'Electricidad'
        elif op == 3:
            tarea = 'Plomeria'
        total = 0.0 # Acumulador para calcular el monto total.
        for i in range(len(self.__arreEmpleados)):
            if isinstance(self.__arreEmpleados[i], EmpleadoExterno):
                if self.__arreEmpleados[i].GetTarea() == tarea:
                    total += self.__arreEmpleados[i].GetSueldo()
        print('Monto total a pagar por la tarea {} : {}'.format(str(tarea),float(total)))
        print('--------------------------------------')
    def Ayuda(self): # Consigna 3
        print('Empleados que requieren la ayuda.')
        print('--------------------------------------')
        print('Nombre | Direccion | DNI')
        for i in range(len(self.__arreEmpleados)):
            if self.__arreEmpleados[i].GetSueldo() < 25000:
                print('{} | {} | {}'.format(str(self.__arreEmpleados[i].GetNombre()),str(self.__arreEmpleados[i].GetDireccion()),str(self.__arreEmpleados[i].GetDocu())))
    def CalcularSueldo(self): # Consigna 4
        print('Funcion calcular sueldos.')
        print('--------------------------------------')
        print('Nombre | Telefono | Sueldo a cobrar')
        print('--------------------------------------')
        for i in range(len(self.__arreEmpleados)):
            print('{} | {} | {}',format(str(self.__arreEmpleados[i].GetNombre()),str(self.__arreEmpleados[i].GetTelefono()),float(self.__arreEmpleados[i].GetSueldo())))
        print('--------------------------------------')
    def MostrarTodos(self): # Opcional para ver toda la informacion del arreglo
        print('Todos los empleados.')
        for i in range(len(self.__arreEmpleados)):
            if isinstance(self.__arreEmpleados[i],EmpleadoContratado):
                print('Empleado contratado.')
                print('Nombre:',self.__arreEmpleados[i].GetNombre())
                print('DNI:',self.__arreEmpleados[i].GetDocu())
                print('Direccion:',self.__arreEmpleados[i].GetDireccion())
                print('Telefono:',self.__arreEmpleados[i].GetTelefono())
                print('Fecha de inicio:',self.__arreEmpleados[i].GetFechaInicio())
                print('Fecha de finalizacion:',self.__arreEmpleados[i].GetFechaFin())
                print('Cantidad de horas trabajadas:',self.__arreEmpleados[i].GetCantidadHoras())
                print('Valor por hora:$',self.__arreEmpleados[i].GetValorHora())
                print('--------------------------------------')
            if isinstance(self.__arreEmpleados[i],EmpleadoPlanta):
                print('Empleado de planta.')
                print('Nombre:',self.__arreEmpleados[i].GetNombre())
                print('DNI:',self.__arreEmpleados[i].GetDocu())
                print('Direccion:',self.__arreEmpleados[i].GetDireccion())
                print('Telefono:',self.__arreEmpleados[i].GetTelefono())
                print('Sueldo basico:$',self.__arreEmpleados[i].GetSueldoBasico())
                print('Antiguedad:',self.__arreEmpleados[i].GetAntiguedad())
                print('Sueldo total:$',self.__arreEmpleados[i].GetSueldoTotal())
                print('--------------------------------------')
            if isinstance(self.__arreEmpleados[i],EmpleadoExterno):
                print('Empleado externo.')
                print('Nombre:',self.__arreEmpleados[i].GetNombre())
                print('DNI:',self.__arreEmpleados[i].GetDocu())
                print('Direccion:',self.__arreEmpleados[i].GetDireccion())
                print('Telefono:',self.__arreEmpleados[i].GetTelefono())
                print('Tarea:',self.__arreEmpleados[i].GetTarea())
                print('Fecha de inicio:',self.__arreEmpleados[i].GetFechaInicio())
                print('Fecha de finalizacion:',self.__arreEmpleados[i].GetFechaFin())
                print('Monto de viatico:$',self.__arreEmpleados[i].GetMontoViatico())
                print('Costo de obra: $',self.__arreEmpleados[i].GetCostoObra())
                print('Monto de seguro de vida:$',self.__arreEmpleados[i].GetMontoSeguro())
                print('--------------------------------------')