from ventas import *

def porcentajeXGenero():
    cantTotCompras=len(listaVentas)
    cantTotMujeres=0
    cantTotHombres=0
    try:
        for venta in listaVentas:
            if venta.gender=='Female':
                cantTotMujeres+=1
            else:
                cantTotHombres+=1
    except:
        'Error'
    porcentajeMujeres = str(cantTotMujeres/cantTotCompras*100)
    porcentajeHombres = str(cantTotHombres/cantTotCompras*100)
    return 'el porcentaje de ventas realizadas por mujeres es {}% y el porcentaje de ventas realizadas por hombres es {}%'.format(str(porcentajeMujeres), str(porcentajeHombres))

print(porcentajeXGenero())