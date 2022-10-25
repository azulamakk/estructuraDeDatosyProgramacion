from nodo import *

class Cola:
    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0
    
    def encolar(self, nodo:Nodo): #Para agregar elementos al final
        if self.len==0:
            self.head=nodo
            self.tail=nodo
        else:
            nodoParaMoverse=Nodo()
            nodoParaMoverse=self.head
            while nodoParaMoverse.next!=None:
                nodoParaMoverse=nodoParaMoverse.next
            nodoParaMoverse.next=nodo
        self.len+=1

    def desencolar(self):
        nodo=Nodo()
        nodo=self.head
        self.head=nodo.next # Elimino el primero
        self.len-=1

    def esVacia(self):
        if self.len==0:
            return "Cola vacia"
        else:
            return "Cola no vacia"
        
    def __str__(self):
        nodo=self.head
        cadena=""
        if self.len==0:
            return "Lista vacia"
        else: 
            while nodo!=None:
                cadena+=str(nodo.dato)+'\t'
                nodo=nodo.next
            return cadena
            
    def longitud(self):
        return self.len

cola1=Cola()
print(cola1.esVacia())
nodo1=Nodo(3)
cola1.encolar(nodo1)
print(cola1)
print(cola1.esVacia())
nodo2=Nodo(6)
cola1.encolar(nodo2)
print(cola1)
nodo1=Nodo(9)
cola1.encolar(nodo1)
print(cola1)
cola1.desencolar()
print(cola1)
print(cola1.longitud())


