# Implemente un método RECURSIVO que calcule la altura de un árbol binario de búsqueda

class NodoArbol:
    def __init__(self, dato=None):
        self.izquierdo=self.izquierdo
        self.derecho=self.derecho
        self.dato=dato


    def calculoAltura(self, altura):
        if self.izquierdo == None and self.derecho == None:
            return altura
        else:
            alturaIzq = altura
            if self.izquierdo != None:
                alturaIzq = self.izquierdo.calculoAltura(altura + 1)
            
            alturaDer = altura
            if self.derecho != None:
                alturaDer = self.derecho.calculoAltura(altura + 1)
            
            return max(altura)


raiz=NodoArbol(5)
raiz.calculoAltura(0)

