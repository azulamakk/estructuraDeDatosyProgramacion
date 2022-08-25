# Utilice funciones built-in del caso, para que a partir de dos listas de enteros se cree una lista que contengala suma 
# de los elementos de las listas de la siguiente manera: Lista1Elemento1+ Lista2Elemento1,Lista1Elemento2+Lista2Elemento2, etc. 
# De no ser iguales los tamaños de ambas listas, manejarloapropiadamente.

lista1=[1,2,3,4]
lista2=[2,3,4,5,10]
listaSuma = []

if len(lista1)>= len(lista2)== True:
    for i in range(len(lista1)):
        listaSuma.append(lista1[i]+lista2[i])
else:
    for i in range(len(lista2)):
        listaSuma.append(lista1[i]+lista2[i])

print(listaSuma)

#ESTA MAL
