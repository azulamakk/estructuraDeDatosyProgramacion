# Dado un árbol binario de búsqueda de números enteros, Implemente un método RECURSIVO que busque si un valor numérico dado está en el árbol binario de búsqueda.

def buscarValorEnArbol(raiz, valor):
    encontrado = False
    if raiz == valor:
        encontrado = True
        return encontrado
    if valor < int(raiz): 
        if valor > raiz.izquierdo:
            return encontrado
        buscarValorEnArbol(raiz.izquierdo, valor)
    if valor > raiz:
        if valor < raiz.derecho:
            return encontrado
        buscarValorEnArbol(raiz.derecho, valor)
        
    

class Nodo:
    def __init__(self,dato=None):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None

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

raiz= NodoArbol(5)
raiz.agregarnodos(Nodo(3))
raiz.agregarnodos(Nodo(7))

valorBuscado = 1
print(buscarValorEnArbol(raiz, valorBuscado))