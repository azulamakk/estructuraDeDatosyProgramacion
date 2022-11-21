class Nodo:
    def __init__(self, dato, prox = None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.nodoInicial = None
        self.longitud = 0

    def agregar(self, dato):
        nodo = Nodo(dato)

        if self.esta_vacia():
            self.nodoInicial = nodo
            self.longitud = 1
            return True

        nodoActual = self.nodoInicial
        while nodoActual.prox != None:
            if nodoActual.dato == dato:
                return False

            nodoActual = nodoActual.prox
        
        if nodoActual.dato != dato:
            nodoActual.prox = nodo
            self.longitud += 1
            return True
        
        return False

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        if self.nodoInicial.dato == dato:
            self.nodoInicial = self.nodoInicial.prox
            self.longitud -= 1
        
        if self.longitud <= 1:
            return

        nodoPrevio = self.nodoInicial
        nodoActual = nodoPrevio.prox
        while nodoActual != None:
            if nodoActual.dato == dato:
                nodoPrevio.prox = nodoActual.prox
                self.longitud -= 1

            nodoPrevio = nodoActual
            nodoActual = nodoActual.prox

    def tiene_elemento(self, dato):
        nodoActual = self.nodoInicial
        while nodoActual != None:
            if nodoActual.dato == dato:
                return True

            nodoActual = nodoActual.prox

        return False

    def esta_vacia(self):
        return self.longitud == 0

    def __str__(self):
        toReturn = ''
        nodoActual = self.nodoInicial
        while nodoActual != None:
            toReturn += str(nodoActual.dato) + ', '
            nodoActual = nodoActual.prox
        return toReturn

