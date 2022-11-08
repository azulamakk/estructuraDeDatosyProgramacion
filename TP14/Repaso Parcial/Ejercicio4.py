# Implemente la función fusionar. Esta función recibe una pila de enteros como parámetro
# y agrega al final los datos contenidos en la pila en orden inverso. 
# Por ejemplo, dada lapila [42,3,17] el resultado será la pila [42,3,17,17,3,42].

pila=[42,3,17]
# pilaAux=pila.reversed()
# print(pilaAux)

pila.extend[pila[::-1]]

print(pila)