from p1ClaseTeorica0509 import *

class lista():
    def __init__(self):
        self.head=None
        self.len=0
    
    def agregarInicio(self, nodo:nodo):
        if (self.len)==0:
            self.head=nodo
        else:
            nodo.prox=self.head
            self.head=nodo
        self.len+=1
    
    def __str__(self):
        nodo=self.head
        cadena=''
        if (self.len==0):
            return 'Lista es vacia'
        else:
            while(nodo!=None):
                cadena+=str(nodo.dato)+ "\t"
                nodo=nodo.prox
            return cadena
    
    def append(self, nodo1:nodo):
        if (self.len==0):
            self.head=nodo1
        else:
            nodomov=nodo()
            nodomov=self.head
            while(nodomov!=None):
                nodomov=nodomov.prox
                nodomov.prox=nodo
        self.len+=1
    
    def pop(self, pos=None):
        nodo1=nodo()
        nodo1=self.head
        if pos==None:
            final=self.len-2
            for i in range(final):
                nodo1=nodo1.prox
            nodo1.prox=None
        else:
            for i in range(pos-1):
                nodo1=nodo1.prox
            nodo1.prox=nodo1.prox.prox
        self.len-=1
        


if __name__=='__main__':
    lista1=lista()
    #print(lista1)
    nodo1=nodo(12)
    #print(nodo1)

    #Agregando el primer nodo a la lista
    #print(nodo1.prox)
    lista1.agregarInicio(nodo1)
    print(lista1)

    #Agregando el segundo nodo a la lista
    nodo1=nodo(21)
    lista1.agregarInicio(nodo1)
    print(lista1)

    nodo1=nodo(1)
    lista1.agregarInicio(nodo1)
    print(lista1)

    #Agregar un elemento al final de la lista
    nodo1=nodo(22)
    lista1.append(nodo1)
    print(lista1)

    #Agregar un elemento al final de la lista
    nodo1=nodo(222)
    lista1.append(nodo1)
    print(lista1)

    #Quitar un elemento del final de la lista
    lista1.pop()
    print(lista1)

    #Quitar un elemento del final de la lista
    lista1.pop(1)
    print(lista1)
    print(lista1.len)
