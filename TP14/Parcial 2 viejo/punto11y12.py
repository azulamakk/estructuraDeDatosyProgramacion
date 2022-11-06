from ventas import *
from datetime import *

def IngresoFechayHora():
    try:
        diaFecha=int(input('Ingrese un dia: '))
        if diaFecha < 0 or diaFecha > 31:
            diaFecha =int(input('Por favor ingrese un numero de fecha valido: '))

        mesFecha=int(input('Ingrese un mes: '))
        if mesFecha < 0 or mesFecha > 12:
            mesFecha =int(input('Por favor ingrese un numero de mes valido: '))

        anioFecha=int(input('Ingrese año: '))
        if anioFecha < 2019 or anioFecha >2022:
            anioFecha =int(input('Por favor ingrese un numero de anio valido: '))

        horaFecha=int(input('Ingrese hora: '))
        if horaFecha < 00 or horaFecha >23:
            horaFecha = int(input('Por favor ingrese un numero de hora valido: '))
            
        minutosFecha=int(input('Ingreso minutos: '))
        
        if minutosFecha < 00 or minutosFecha > 59: 
            minutosFecha = int(input('Por favor ingrese un numero de minutos valido: '))
        fecha=str(diaFecha)+'/'+str(mesFecha)+'/'+str(anioFecha)+'  '+str(horaFecha)+':'+str(minutosFecha)+':'+str(00)
   
    except:
        'Hubo un error en la informacion'
    
    return fecha

fechaIngresada=IngresoFechayHora()

class NodoArbol:
    #constructor
    def __init__(self,dato=None):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None

    def agregarnodos(raiz,nodo):
        if raiz.dato<nodo.dato:
            if raiz.derecho==None:
                raiz.derecho=nodo
            else:
                NodoArbol.agregarnodos(raiz.derecho,nodo)
        elif raiz.dato>nodo.dato:
            if raiz.izquierdo==None:
                raiz.izquierdo=nodo
            else:
                NodoArbol.agregarnodos(raiz.izquierdo,nodo)


raiz=NodoArbol(fechaIngresada)

for venta in listaVentas:
    # fechaYHora = ''
    # for i in range(len(venta.date)):
    #     if venta.date[i] != "/":
    #         fechaYHora += venta.date[i]
    # fechaYHora += '  '
    # for i in range(len(venta.time)):
    #     if venta.time[i] != ':':
    #         fechaYHora += venta.time
    
    # fecha = datetime.strptime(fechaYHora, '%d/%m/%y %H:%M')
    fecha = date(venta.date) + '  ' + time(venta.time)
    fecha=NodoArbol()
    fecha.agregarnodos(fecha)
