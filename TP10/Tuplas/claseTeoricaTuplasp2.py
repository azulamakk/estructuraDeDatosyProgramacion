import sys

tupla=('string', 10, True, [1,2,3,4], (4,5,6))
lista=list(tupla)
tuplaLista=tuple(lista)

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