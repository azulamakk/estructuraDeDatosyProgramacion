# Primera forma de importar
from array import array

# Segunda forma de importar
#import array as arr

vector = array('d', [1.2,3.5,6.9,7])
print(vector)
print(type(vector))

lista=[1,4,9,12,-5]
vectorInt=array('i', lista)
print(vectorInt)

for dato in vectorInt:
    print(dato, end='\t')

# Acceder a una determinada posicion del vector

print('\n', len(vectorInt))
x=len(vectorInt)-1
print(x)
print(vectorInt[x])

print(vectorInt[-1])

# Slicing
# Mostrar los elementos del vector de decimales desde la posicion 1 a 3
print(vector[1:3])

# Modificar un valor en el vector dada su posicion
vectorInt[0] = -25
print(vectorInt)

vector[0:3]=array('d', [2.5,6.4,3.1])
print(vector)

vectorInt.append(33)
print(vectorInt)

vectorInt.extend([34,21,90])
print(vectorInt)

# Concatenar vector
lista = [1,3,4,2]
vectorNuevo=array('i', lista)
print(vectorNuevo)

numeros = array('i')
numeros=vectorInt+vectorNuevo
print(numeros)

# index, envia la posicion de la primera aparicion del dato
print(numeros.index(4))

# Borrar elementos del vector
# Remove
vector.remove(7.0)
print(vector)

# Pop
# Usa el comportamiento de las pilas, ultimo en entrar primero en salir
vector.pop()
print(vector)

vector.pop(0) # Elimina en esa posicion
print(vector)

# Reverse
vectorInt.reverse()
print(vectorInt)

# Ordenamiento sorted
print(sorted(vectorInt))

# Convertir un vector en una lista
lista=vectorInt.tolist()
print(lista)
print(type(lista))
print(type(vectorInt))

listaDecimal = vector.tolist()
print(listaDecimal)
print(type(listaDecimal))
print(type(vector))