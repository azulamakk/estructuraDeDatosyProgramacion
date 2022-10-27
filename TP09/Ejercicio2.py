# Implemente la clase Cola. En esta implementación el constructor de la clase es una lista.Los métodos de la clase Cola a implementar son: encolar, desencolar, esVacia, visualizar Cola, longitud.

from nodo import *

class Cola:
    def __init__(self):
        self.tailvalue=None
        self.len=0

    def esVacia(self):
        if self.len==0:
            return True
        else:
            return False

    def encolar(self, nodo:Nodo):
        nodo=Nodo(nodo)
        if (self.esVacia()):
            self.tailvalue=nodo
        else:
            nodo.next=nodo
        self.len+=1
    
    def desencolar(self):
        if (self.esVacia()):
            print('No hay elementos por desapilar')
        else:
            self.tailvalue=None
            self.len-=1
        
    def __str__(self):
        nodo=self.tailvalue
        cadena=''
        if self.len==0:
            return 'Lista vacia'
        else:
            while (nodo!=None):
                cadena+=str(nodo.dato)+'\t'
                nodo=nodo.next
            return cadena

if __name__=='__main__':
    cola=Cola()

    cola.encolar(8)
    print(cola)

    cola.encolar(88)
    print(cola)

    cola.encolar(888)
    print(cola)

    cola.desencolar()
    print(cola)
    print(cola.esVacia())