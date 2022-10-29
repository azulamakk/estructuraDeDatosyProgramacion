# 2 + 5 * (8 + 4)

from turtle import st

expresion='2 + 5 * (8 + 4)'

class Nodo:
    def __init__(self,dato=None):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None

raiz=Nodo('+')
raiz.derecho=Nodo('*') #vertice1
raiz.izquierdo=Nodo(2)

vertice1=raiz.derecho
vertice1.derecho=Nodo(3)
vertice1.izquierdo=Nodo(5)

def es_hoja(nodo):
    if nodo.derecho==None and nodo.izquierdo==None:
        return True
    else:
        return False

def resolverArbol(nodo):
    if es_hoja(nodo)==True:
        return nodo.dato
    else:
        valorDerecho=resolverArbol(nodo.derecho) 
        valorIzquierdo=resolverArbol(nodo.izquierdo)

        operador= nodo.dato 
        if operador == '+':
            return valorDerecho + valorIzquierdo
        elif operador == '-':
            return valorIzquierdo - valorDerecho
        elif operador == '*':
            return valorIzquierdo * valorDerecho
        elif operador == '/':
            return valorIzquierdo / valorDerecho

print(resolverArbol(raiz)) 

class NodoPila:
    def __init__(self, headvalue, prox=None):
        self.headvalue=headvalue
        self.prox=prox
    
class Pila:
    def __init__(self):
        self.tope = None

    def agregarAPila(self, valor):
        aAgregar = NodoPila(valor, self.tope)
        self.tope = aAgregar

    def sacarDePila(self):
        if self.estaVacia():
            return None
        else:
            aSacar=self.tope.headvalue
            self.tope=self.tope.prox
            return aSacar

    def estaVacia(self):
        if self.tope==None:
            return True
        else: 
            return False

    def mostrarTope(self):
        return self.tope.headvalue

def armarArbol(posfija):
    pilaArbol=Pila()
    for i in range(len(posfija)):
        if posfija[i].isnumeric():
            pilaArbol.agregarAPila(Nodo(int(posfija[i])))
        else:
            ladoIzquierdo=pilaArbol.sacarDePila()
            ladoDerecho=pilaArbol.sacarDePila()
            raiz=Nodo(posfija[i])
            raiz.derecho=ladoDerecho
            raiz.izquierdo=ladoIzquierdo
            pilaArbol.agregarAPila(raiz)

    return pilaArbol.sacarDePila()

def infijaAPosfija(infija):
    precedencia = {'+': 0, '-': 0, '*': 1, '/': 1}

    i = 0
    posfija = []
    operadores = "+-/*"
    stack = Pila()
    while i < len(infija):
        char = infija[i]
        if char in operadores:
            if stack.estaVacia() or stack.mostrarTope() == '(':
                stack.agregarAPila(char)
                i += 1
            else:
                tope = stack.mostrarTope()
                if precedencia[char] == precedencia[tope]:
                    popped_element = stack.sacarDePila()
                    posfija.append(popped_element)
                elif precedencia[char] > precedencia[tope]:
                    stack.agregarAPila(char)
                    i += 1
                elif precedencia[char] < precedencia[tope]:
                    popped_element = stack.sacarDePila()
                    posfija.append(popped_element)
        elif char == '(':
            stack.agregarAPila(char)
            i += 1
        elif char == ')':
            tope = stack.mostrarTope()
            while tope != '(':
                popped_element = stack.sacarDePila()
                posfija.append(popped_element)
                tope = stack.mostrarTope()
            stack.sacarDePila()
            i += 1
        else:
            posfija.append(char)
            i += 1

    while not stack.estaVacia():
        posfija.append(stack.sacarDePila())

    return posfija

infija = '1+2*(3+5)'
posfija = infijaAPosfija(infija)
arbol = armarArbol(posfija)
print(resolverArbol(arbol))

infija = '2+5*(8+4)'
posfija = infijaAPosfija(infija)
arbol = armarArbol(posfija)
print(resolverArbol(arbol))