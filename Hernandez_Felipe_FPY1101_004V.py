import csv
import math
import os
import random



trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
trabajadores_lista = []

def menu():
    opcion = 0
    try:
        opcion = int(input('''\n********* Sistema de gestión - Planing Solutions *********
           1. Asignar sueldos aleatorios
           2. Clasificar sueldos
           3. Ver estadísticas
           4. Reporte de sueldos
           5. Salir del programa
           Ingrese una opción: '''))
    except ValueError:
        print("Por favor ingrese una opción válida, entre 1 y 5")
        opcion = 0
    return opcion

def asignar_sueldos():
    global trabajadores_lista
    print("*** Asignación de sueldos automática ***")
    trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
    sueldos = []
    for i in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    trabajadores_lista = [{'empleado': trabajador, 'sueldo': sueldo} for trabajador, sueldo in zip(trabajadores, sueldos)]
    print("Trabajadores asignados a diccionarios individuales con sueldos:")

def clasificar_sueldos():
    menores=0
    entre=0
    superiores=0
    sueldos_totales= 0
    print("\n*** Clasificación de sueldos ***")
    print("\nSueldos menores a $800.000: ")
    print("Nombre empleado                    Sueldo")
    for trabajador in trabajadores_lista:
        if trabajador['sueldo'] < 800000:
            menores +=1
            print(f"{trabajador['empleado']}                    {trabajador['sueldo']}")
    print(f"Hay '{menores}' trabajador(es) en esta cetegoría")
    
    print("\nSueldos entre $800.000 y $2.000.000: ")
    print("Nombre empleado                    Sueldo")
    for trabajador in trabajadores_lista:
        if trabajador['sueldo'] >= 800000 and trabajador['sueldo'] <= 2000000:
            entre +=1
            print(f"{trabajador['empleado']}                    {trabajador['sueldo']}")
    print(f"Hay '{entre}' trabajador(es) en esta cetegoría")
    
    print("\nSueldos superiores a $2.000.000: ")
    print("Nombre empleado                    Sueldo")
    for trabajador in trabajadores_lista:
        if trabajador['sueldo'] > 2000000:
            superiores +=1
            print(f"{trabajador['empleado']}                    {trabajador['sueldo']}")
    print(f"Hay '{superiores}' trabajador(es) en esta cetegoría")
    
    for trabajador in trabajadores_lista:
        sueldos_totales += trabajador['sueldo']
    print(f"\nTOTAL SUELDOS: ${sueldos_totales}")
    
def ver_estadisticas():
    print("\n*** Estadísticas de sueldos ***")
    sueldos = []
    for trabajador in trabajadores_lista:
       sueldos.append(trabajador['sueldo'])
    alto = max(sueldos)
    bajo = min(sueldos)
    promedio = sum(sueldos) /len(sueldos)
    producto = 1
    for sueldo in sueldos:
        producto *= sueldo
    n = len(sueldos)
    mediaGeo = producto ** (1/n)
    print(f"El sueldo más alto es de ${alto}")
    print(f"El sueldo más bajo es de ${bajo}")
    print(f"El promedio de sueldos es ${promedio:.2f}")
    print(f"La media geométrica de los sueldos es ${mediaGeo:.2f}")

def reporte_sueldos():
    with open('Reporte sueldos.csv', 'w', newline='') as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow(["Nombre empleado", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo líquido"])
        print("\n*** Reporte de sueldos ***")
        print("Nombre empleado         Sueldo base         Descuento salud              Descuento AFP              Sueldo líquido")
        for trabajador in trabajadores_lista:
            sueldo_base = trabajador['sueldo']
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - (descuento_afp + descuento_salud)
            escribir.writerow([trabajador['empleado'], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"{trabajador['empleado']}              {sueldo_base}                   {round(descuento_salud)}                      {round(descuento_afp)}                      {round(sueldo_liquido)}")
        print(f"Registro de trabajadores actualizado y guardado en {os.getcwd()}")

def salir_programa():
    while True:
        try:
            salir = int(input("\n¿Desea salir del programa? (1:sí - 2:no): "))
            if salir == 1:
                print("\nFinalizando programa...")
                print("Desarrollado por Felipe Hernández")
                print("RUT 16.304.137-5")
                print("")
                return True
            elif salir == 2:
                print("\nPuede continuar operando")
                return False
            else:
                print("\nOpción no reconocida, por favor ingrese 1 o 2")
        except ValueError:
            print("\nOpción no reconocida, por favor ingrese 1 o 2")

while True:
    opcion = menu()
    if opcion == 1:
        asignar_sueldos()
    elif opcion == 2:
        clasificar_sueldos()
    elif opcion == 3:
        ver_estadisticas()
    elif opcion == 4:
        reporte_sueldos()
    elif opcion == 5:
        if salir_programa():
            break
    
    