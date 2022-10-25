# Crear estructura de datos set

# Utilizando su constructor
conjunto=set()
print(conjunto)

# Utilizar {}
conjunto1={}
print(conjunto1)

# Crear conjunto con elementos
conjunto1={1,2,3,4,5}
print(conjunto1)

conjunto2={'Ninfa', 'Delgado', 'Estructura de datos', 2022}
print(conjunto2)

conjunto2=('Ninfa', 'Delgado', 'Estructura de datos', 2022, 'Ninfa', 2022)
print(conjunto2)

# Crear un conjunto utilizando su constructor
conjunto3=set('amiga')
print(conjunto3)
conjunto3=set('amiga', )
print(conjunto3)

conjunto=set([1,2,3,4,])
print(conjunto)

# Como recorrer un conjunto
for elemento in conjunto2:
    print(elemento)

# Agregar elemento al conjunto

# Agregar mas de un elemento al conjunto
conjunto2.update(['Antonieta', 'Maria'])
print(conjunto2)

conjunto2.update(('Joaquin', 'Tomas'))
print(conjunto2)

# Eliminar elementos del conjunto
conjunto2.pop()
print(conjunto2)

# Uso de los metodos propios de conjuntos
print(conjunto2)
conjunto2.update([1,2,5])
print(conjunto2)
print(conjunto1)

print(conjunto1.union(conjunto2))
print(conjunto1.intersection(conjunto2))
print(conjunto1.difference(conjunto2))

print('***************************')
print('conjunto2 ', conjunto2)
print('conjunto1 ', conjunto1)

conjunto1.difference_update(conjunto1)
print('conjunto2 ', conjunto2)
print('conjunto1 ', conjunto1)