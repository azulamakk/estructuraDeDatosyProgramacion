import sys

# Generamos dos tuplas vacias
tupla=()
print(tupla)
tuplas=tuple()
print(tuplas)

# Generar lista vacia
lista=[]
print(lista)

# Espacios en memoria que ocupan las listas
print('bytes de la tupla vacia ',sys.getsizeof(tupla))
print('bytes de la lista vacia ',sys.getsizeof(lista))

# Agregar informacion a la tupla
tupla=(1,2,3,4,5)
lista=[1,2,3,4,5]

# Espacios en memoria que ocupan listas y tuplas con los mismos datos almacenados
print('bytes de la tupla ',sys.getsizeof(tupla))
print('bytes de la lista ',sys.getsizeof(lista))

# Ejemplo de No es una tupla, es un dato entero
tuplas=(1)
print(tuplas)
print(type(tuplas))

# Ejemplo de tupla con un solo elemento
tuplas=(1,)
print(tuplas)
print(type(tuplas))

# Otra forma de crear tuplas, descompone la secuencia y genera los datos de la tupla
tuplas=('hola')
print(tuplas)

tupla=tuple([1,2,3,4,5])
print(tupla)

tupla=('string', 10, True, [1,2,3,4], (4,5,6))
print(tupla)
print(type(tupla))

# Convertir tuplas en listas
lista=list(tupla)
print(lista)
print(type(lista))

# Convertir lista en tupla
tuplaLista=tuple(lista)
print(tuplaLista)
print(type(tuplaLista))

# Otro manejo de tuplas asignancdo variables
numeros = (1,2,3,4)
a,b,c,d=numeros
print(a,b,c,d)

numeros=(1,2,3,4,5,6,7)
a,b,c,*restodatos=numeros
print(a,b,c)
print(restodatos)

numeros=(1,2,3,4,5,6,7)
a,b,c,*_=numeros
print(a,b,c)

tuplaNueva=numeros+tuplaLista
print(tuplaNueva)

# Manejo de los indicies para obtener subtuplas
# Colocar la tupla al reves

tuplaAlReves=tuplaNueva[::-1]
print(tuplaAlReves)

print(tuplaAlReves[:2])

# Metodos propios de la tupla
print(tuplaAlReves.index(True))
print(tuplaNueva)
print(tuplaNueva.count(1))

print(len(tuplaNueva))

# Utilizar funcion enumerate
tuplaEnumerate=enumerate(tuplaNueva,3)
print(tuplaEnumerate)
tuplaNueva=list(tuplaEnumerate)
print(tuplaNueva)