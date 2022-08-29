# Utilice funciones built-in del caso, para que a partir de dos listas de enteros se cree una lista que contengala suma 
# de los elementos de las listas de la siguiente manera: Lista1Elemento1+ Lista2Elemento1,Lista1Elemento2+Lista2Elemento2, etc. 
# De no ser iguales los tamaños de ambas listas, manejarloapropiadamente.
from itertools import zip_longest

lista1=[1,2,3,4]
lista2=[2,3,4,5,100,90,80]

listaSuma=[sum(n) for n in zip_longest(lista1, lista2, fillvalue=0)]

print(listaSuma)
