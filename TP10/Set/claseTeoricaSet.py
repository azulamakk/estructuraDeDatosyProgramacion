# Crear estructura de datos set
import sys

# Utilizando su constructor
conjunto=set()
print(conjunto) # imprime set()

# Utilizar {}
conjunto1={} 
print(conjunto1) # imprime {}

# Crear conjunto con elementos
conjunto1={1,2,3,4,5}
print(conjunto1) # imprime {1,2,3,4,5}

conjunto2={'Ninfa', 'Delgado', 'Estructura de datos', 2022}
print(conjunto2) # imprime {'Ninfa', 'Delgado', 'Estructura de datos', 2022}

conjunto2={'Ninfa', 'Delgado', 'Estructura de datos', 2022, 'Ninfa', 2022}
print(conjunto2) # imprime {'Ninfa', 'Delgado', 'Estructura de datos', 2022} (saca duplicados)

# Crear un conjunto utilizando su constructor
conjunto3=set('amiga')
print(conjunto3) # Imprime letras no repetidas de la cadena
conjunto3=set('amiga', )
print(conjunto3) # imprime letras no repetidas de la cadena

conjunto=set([1,2,3,4,])
print(conjunto) # imprime {1,2,3,4}

# Como recorrer un conjunto
for elemento in conjunto2:
    print(elemento) # imprime cada elemento de conjunto por separado

# Agregar elemento al conjunto
conjunto2.add('azul')
print(conjunto2) # imprime conjunto con 'azul' incluido

# Agregar mas de un elemento al conjunto
conjunto2.update(['Antonieta', 'Maria'])
print(conjunto2) # agrega 'antonieta' y 'maria' al conjunto

conjunto2.update(('Joaquin', 'Tomas'))
print(conjunto2) # agrega 'joaquin' y 'tomas' al conjunto

# Eliminar elementos del conjunto
conjunto2.pop()
print(conjunto2) # saca el primer elemento del set

# Uso de los metodos propios de conjuntos
conjunto2.update([1,2,5])
print(conjunto2) # agrega los elementos (sin un orden establecido)

print(conjunto1.union(conjunto2)) # imprime uniendo los conjuntos siguiendo un orden
print(conjunto1.intersection(conjunto2)) # imprime solo los elementos que comparten los conjuntos
print(conjunto1.difference(conjunto2)) # imprime los elementos distintos entre los conjuntos

print('***************************')
print('conjunto2 ', conjunto2)
print('conjunto1 ', conjunto1)

conjunto1.difference_update(conjunto2)
print('conjunto2 ', conjunto2) 
print('conjunto1 ', conjunto1) # imprime solo las diferencias con conjunto2