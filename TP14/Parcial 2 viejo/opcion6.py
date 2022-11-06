from ventas import *
diccionario = dict.fromkeys(tuplaSucursales, [])

def sucursalGastosXPlan():
    print('Las sucursales con clientes Member que gastaron menos que el no member:')
    for key in diccionario.keys():
        diccionario[key]=[0,0]    

    for venta in listaVentas:
        if venta.branch in diccionario and venta.customerType == 'Member':
            diccionario[venta.branch][0] += float(venta.total)
        else:
            diccionario[venta.branch][1] += float(venta.total)
    
    listaMayorGastosNormales = []
    for key in diccionario.keys():
        if diccionario[key][0] < diccionario[key][1]:
            listaMayorGastosNormales.append(key)

    return listaMayorGastosNormales

print(sucursalGastosXPlan())