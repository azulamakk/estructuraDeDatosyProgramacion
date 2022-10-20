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