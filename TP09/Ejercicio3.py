#Implemente la clase Cola, como una secuencia de nodos anidados. 
# En esta implementación el constructorde la clase Cola , almacena la dirección al nodo cima y del nodo final.
# Los métodos de la clase Cola a implementar son: encolar, desencolar, esVacia, visualizar Cola, longitud

class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.next=None
    def __str__(self):
        return self.dato

class Cola():
    def __init__(self):
        self.headvalue=None
        self.len=0
        self.bottonvalue=None
    
    def encolar(self, nodo:Nodo):
        nodo=Nodo(nodo)
        if (self.len==0):
            self.headvalue=nodo
            self.bottonvalue=nodo
        else:
            self.bottonvalue
            nodo.prox=self.headvalue
            self.headvalue=nodo
        
        self.len+=1
    
    def desencolar(self):
        if self.len==0:
            print('No hay elementos')
        else:
            nodo=self.headvalue
            for i in range(self.len-2):
                nodo=nodo.prox
            self.bottonvalue=nodo
            nodo.prox=None
        
    def __str__(self):
        nodo=self.headvalue
        cadena=''
        if self.len==0:
            return 'Lista vacia'
        else:
            while(nodo!=None):
                cadena+=str(nodo.dato)+'\t'
                nodo=nodo.prox
            return cadena

if __name__=='__main__':

    cola=Cola()
    cola.encolar(2)
    cola.encolar(4)
    cola.encolar(6)
    print(cola)
    print('Cabeza: ', cola.headvalue)
    print('Valor de abajo: ', cola.bottonvalue)

    cola.desencolar()
    print(cola)

    print('Valor de abajo: ', cola.bottonvalue)