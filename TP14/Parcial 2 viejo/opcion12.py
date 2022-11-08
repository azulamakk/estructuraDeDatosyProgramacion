from opcion9y10 import *

def recientesAAntiguos():
    raiz=NodoArbol(listaVentas[0].date, listaVentas[0])
    for venta in listaVentas[1:len(listaVentas)]:
        if venta.date != None:
            nodoVenta = NodoArbol(venta.date, venta)
            raiz.agregarnodos(nodoVenta)     
    print(raiz.reversestr())    