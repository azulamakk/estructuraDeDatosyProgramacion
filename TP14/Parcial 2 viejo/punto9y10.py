from ventas import *

def IngresoFechayHora():
    try:
        diaFecha= obtenerInt('Ingrese un dia: ', 0, 31)

        mesFecha= obtenerInt('Ingrese un mes: ', 0, 12)

        anioFecha= obtenerInt('Ingrese un año: ', 2019, 2022)

        horaFecha= obtenerInt('Ingrese una hora: ', 0, 23)

        minutosFecha= obtenerInt('Ingrese un minuto: ', 0, 59)

        fecha = datetime.datetime(anioFecha, mesFecha, diaFecha, horaFecha, minutosFecha)
        print(fecha)
        return fecha
    except:
        'Hubo un error en la informacion'
    
    return fecha

def obtenerInt(mensaje, minimo, maximo):
    try:    
        numero = int(input(mensaje))

        if numero < minimo or numero > maximo:
            print('Numero de fecha incorrecto. Intente de nuevo')
            return obtenerInt(mensaje, minimo, maximo)
        else:
            return numero

    except ValueError or TypeError:
        print('Dato de tipo erroneo')
        return obtenerInt(mensaje, minimo, maximo)

class NodoArbol:
    #constructor
    def __init__(self, dato=None):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None

    def agregarnodos(self, nodo):
        if self.dato < nodo.dato:
            if self.derecho==None:
                self.derecho=nodo
            else:
                self.derecho.agregarnodos(nodo)
        elif self.dato > nodo.dato:
            if self.izquierdo==None:
                self.izquierdo=nodo
            else:
                self.izquierdo.agregarnodos(nodo)
    
    def __str__(self):
        valorIzq = ""
        if self.izquierdo != None:
            valorIzq = str(self.izquierdo)
        
        valorDer = ""
        if self.derecho != None:
            valorDer = str(self.derecho)
        
        return valorIzq + str(self.dato) + valorDer


def armarArbol(raiz):
    for venta in listaVentas:
        if venta.date != None:
            nodoVenta = NodoArbol(venta.date)
            raiz.agregarnodos(nodoVenta)


def ladoIzquierdo():
    raiz=NodoArbol(IngresoFechayHora())
    armarArbol(raiz)
    print(raiz.izquierdo)

def ladoDerecho():
    raiz=NodoArbol(IngresoFechayHora())
    armarArbol(raiz)
    print(raiz.derecho)