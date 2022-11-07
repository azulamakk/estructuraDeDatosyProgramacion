from ventas import *

def efectividadEwallet():
    cantEwallet=0
    cantOtros=0
    ratingEwallet=0
    ratingOtros=0
    try:
        for venta in listaVentas:
            if venta.payment=='Ewallet':
                cantEwallet+=1
                ratingEwallet+=float(venta.rating)
            else:
                cantOtros+=1
                ratingOtros+=float(venta.rating)
    except:
        'Error'
    ratingAvgEwallet=ratingEwallet/cantEwallet
    ratingAvgOtros=ratingOtros/cantOtros
    if ratingAvgEwallet < ratingAvgOtros:
        return 'la Ewallet presenta mejores calificaciones que los otros medios de pago'
    else:
        return 'la Ewallet presenta menores calificaciones que los otros medios de pago'