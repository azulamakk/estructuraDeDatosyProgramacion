# 2) Implemente la clase Cola. En esta implementación el constructor de la clase es una lista.Los métodos de la clase Cola a implementar son: encolar, desencolar, esVacia, visualizar Cola, longitud.
# 4) Escriba un método en la clase cola que invierte el orden de los elementos de la cola

class Cola:
    def __init__(self):
        self.cole=[]
    def encolar(self, valor):
        self.cola.append(valor)
    def esVacia(self):
        return self.cola == []
    def longitud(self):
        return len(self.cola)
    def desencolar(self):
        return self.cola.pop()
    def visualizar(self):
        listaaux=[]
        for i in range(len(self.cola)):
            listaaux.append(self.cola[i])
        return listaaux
    def invertir(self):
        colaaux=[]
        for i in range(len(self.cola)):
            colaaux.append(self.cola.pop())
        return colaaux

if __name__ == "__main__":
    cola=Cola()
    invertida=[]
    cola.encolar(9)
    cola.encolar(27)
    print(cola.visualizar())
    print(cola.esVacia())
    print(cola.longitud())
    print(cola.longitud())