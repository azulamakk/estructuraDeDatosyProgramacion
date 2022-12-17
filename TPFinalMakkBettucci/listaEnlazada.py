
class Nodo:
    def __init__(self, valor = None, prox = None):
        self.valor = valor
        self.prox: 'Nodo' = prox

    def __str__(self):
        return str(self.valor)
        
class ListaEnlazada:
    def __init__(self):
        self.head: Nodo = None

    # Insertar ordenado iterativamente
    def agregar(self, valor):
        if self.head == None:
            self.head = Nodo(valor)
            return
        
        anterior = self.head
        if valor < anterior.valor:
            self.head = Nodo(valor, anterior)
            return

        actual = anterior.prox

        while actual != None and actual.valor < valor:
            anterior = actual
            actual = anterior.prox
        
        anterior.prox = Nodo(valor, actual)

    def __str__(self):
        actual = self.head
        res = ""
        while actual != None:
            res += str(actual.valor) + ", "
            actual = actual.prox

        return res[:-2]

    def __repr__(self):
        return self.__str__()
