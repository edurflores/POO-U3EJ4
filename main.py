from claseManejadorEmpleados import ManejadorEmpleados


if __name__ == '__main__':
    me = ManejadorEmpleados()
    me.Carga()
    print('Menu')
    print('1- Registrar horas.\n2- Total de tarea.\n3- Ayuda.\n4- Calcular sueldo.\n0- Salir.')
    op = int(input('Seleccione opcion:'))
    while op != 0:
        if op == 1:
            me.RegistrarHoras()
        elif op == 2:
            me.TotalDeTarea()
        elif op == 3:
            me.Ayuda()
        elif op == 4:
            me.CalcularSueldo()
        elif op == 0:
            print('Saliendo del programa.')
        elif op == 6:
            me.MostrarTodos() # Opcional
        print('Menu')
        print('1- Registrar horas.\n2- Total de tarea.\n3- Ayuda.\n4- Calcular sueldo.\n0- Salir.')
        op = int(input('Seleccione opcion:'))
        
    # Nota: Por requerimiento de consigna,
    # deben introducirse la cantidad de empleados por teclado. Se incluyen 3 archivos de empleados.
    # Cada uno tiene 5 empleados para usar como lote de pruebas. Siendo un total 15 empleados.
    # Se recomienda ingresar 15 para que funcione el programa. Ingresar menos que eso podría producir error.