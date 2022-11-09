
import time
from ventas import *
from opcion1 import *
from opcion2 import * 
from opcion3 import *
from opcion4 import *
from opcion5 import *
from opcion6 import *
from opcion9y10 import *
from opcion11 import *
from opcion12 import *

start = time.process_time()

print('''
    Ingrese que opcion desea realizar:
    1. Mostrar listado de ventas
    2. Cargar venta manualmente
    3. Determinar efectividad de pagos con Ewallet
    4. Calcular porcentajes de compras realidas por hombres y por mujeres
    5. Determinar sucursal mejor calificada
    6. ¿Sucursal con clientes Member gastó menos que el no member?
    7. Graficas de rating de un tipo de producto y cant de ventas
    8. Grafica del porcentaje de ingresos devenidos de compras de hombres y de mujeres
    9. Imprimir ventas anteriores a una determinada fecha y hora
    10. Imprimir ventas posteriores a una determinada fecha y hora
    11. Imprimir todos los registros. De antiguos a recientes
    12. Imprimir todos los registros. De recientes a antiguos
    13. Salir''')

def menuPrincipal(opcionIngresada):

    if opcionIngresada == 1:
        leerListadoVentas()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 2:
        cargarVentaManual()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 3:
        print(efectividadEwallet())
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 4:
        print(porcentajeXGenero())
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()        

    if opcionIngresada == 5:
        print(sucursalMejorCalificada())
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 6:
        print(sucursalGastosXPlan())
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 7:
        print('Opcion elegida: 7')
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 8:
        print('Opcion elegida: 8')
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 9:
        ladoIzquierdo()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 10:
        ladoDerecho()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 11:
        antiguosARecientes()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 12:
        recientesAAntiguos()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()

    if opcionIngresada == 13:
        print('Opcion elegida: 13')
        exit()

def ingresoOpcion():
    opcionIngresada=input('Por favor ingrese una opcion: ')
    try:
        if int(opcionIngresada)>13 or int(opcionIngresada)<0:
            opcionIngresada=ingresoOpcion()
        print(opcionIngresada)
        return opcionIngresada
    except ValueError:
        print('Carga de opcion incorrecta')
        opcionIngresada=ingresoOpcion()
        return opcionIngresada

def ingresoNuevo():
    print('¿Desea ingresar otra opcion?')
    opcionNueva=input('Indique Y/N: ').capitalize()
    if opcionNueva == 'Y':
        return True
    elif opcionNueva == 'N':
        return False
    else:
        print('Ingrese Y/N')
        opcionNueva=ingresoNuevo()

opcionElegida=int(ingresoOpcion())

menuPrincipal(opcionElegida)

def tiempoTranscurrido(start):
    final=time.process_time()-start
    return final