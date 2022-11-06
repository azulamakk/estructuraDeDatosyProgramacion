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
     
#     for i in range(len(listaVentasDict)):
#         if listaVentasDict == 'Ewallet':
#             cantEwallet+=1
#             ratingEwallet += listaVentasDict[i]
#         else:
#             cantOtros+=1
#             ratingEwallet += listaVentasDict[i]
#     ratingAvgEwallet=ratingEwallet/cantEwallet
#     ratingAvgOtros=ratingOtros/cantOtros
#     if ratingAvgEwallet < ratingAvgOtros:
#         return 'la Ewallet presenta mejores calificaciones que los otros medios de pago'
#     else:
#         return 'la Ewallet presenta menores calificaciones que los otros medios de pago'
# # # def efectividadEwallet():
#     with open('/Users/azulmakk/Desktop/Estructura de Datos/TP14/Parcial 2 viejo/supermarket_sales - Sheet1.csv', newline='') as csvFile:
#         reader=csv.DictReader(csvFile)
#         for heading in reader.fieldnames:
#             if heading == 'Payment':
#                 cantEwallet=0
#                 ratingEwallet=0
#                 cantOtros=0
#                 ratingOtros=0
#                 for i in range(len(reader)): # Aca hay error
#                     if reader.fieldnames[heading] == 'Ewallet':
#                         cantEwallet+=1
#                     # if reader.fieldnames[heading] == 'Ewallet':
#                     #     ratingEwallet+= 
#                     else:
#                         cantOtros+=1
#                         ratingOtros+=reader[i]
#     promedioRatingEwallet=ratingEwallet/cantEwallet
#     promedioRatingOtros=ratingOtros/cantOtros
#     if promedioRatingEwallet > promedioRatingOtros:
#         return 'La ewallet presenta una mejor calificacion con respecto a otros medios de pago'
#     else:
#         return 'La ewallet presenta menor calificacion con respecto a otros medios de pago'

# from ventas import *
# def efectividadEwallet():
    