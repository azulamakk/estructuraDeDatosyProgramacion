# Implemente la clase Pila, como una secuencia de nodos anidados. 
# En esta implementación el constructor dela clase lista almacena la dirección al nodo cima.Los métodos de la clase Pila a realizar son: 
# apilar, desapilar, esVacia, visualizar Pila
from nodo import *

class Pila:
    def __init__(self):
        self.headvalue=None
        self.len=0

    def esVacia(self):
        if self.len==0:
            return True
        else:
            return False

    def apilar(self, nodo:Nodo):
        nodo=Nodo(nodo)
        if (self.esVacia()):
            self.headvalue=nodo
        else:
            nodo.next=self.headvalue
            self.headvalue=nodo
        self.len+=1
    
    def desapilar(self):
        if (self.esVacia()):
            print('No hay elementos por desapilar')
        else:
            nodo=self.headvalue
            self.headvalue=nodo.next
            self.len-=1
        
    def __str__(self):
        nodo=self.headvalue
        cadena=''
        if self.len==0:
            return 'Lista vacia'
        else:
            while (nodo!=None):
                cadena+=str(nodo.dato)+'\t'
                nodo=nodo.next
            return cadena
    
    def esVacia(self):
        if self.len==0:
            return True
        else: 
            return False

if __name__=='__main__':
    pila=Pila()

    pila.apilar(8)
    print(pila)

    pila.apilar(88)
    print(pila)

    pila.apilar(888)
    print(pila)

    pila.desapilar()
    print(pila)
    print(pila.esVacia())