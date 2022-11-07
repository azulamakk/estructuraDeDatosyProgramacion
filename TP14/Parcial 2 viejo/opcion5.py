from ventas import *

diccionario = dict.fromkeys(tuplaSucursales, [])

def sucursalMejorCalificada():
    for key in diccionario.keys():
        diccionario[key]=[0,0]
        
    for venta in listaVentas:
        if venta.branch in diccionario and venta.rating != None and venta.rating != '20:33':
            diccionario[venta.branch][0] += float(venta.rating)
            diccionario[venta.branch][1] += 1

    maxKey = ""
    maxAvg = 0
    
    for key in diccionario.keys():
        currAvg = diccionario[key][0] / diccionario[key][1]
        if currAvg > maxAvg:
            maxAvg = currAvg
            maxKey = key
    
    return maxKey