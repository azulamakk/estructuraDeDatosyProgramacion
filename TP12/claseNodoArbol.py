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