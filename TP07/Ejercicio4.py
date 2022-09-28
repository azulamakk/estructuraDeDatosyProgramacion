#Escriba un método que toma dos listas de enteros y las une en una sola lista de la siguiente manera:
# Lista1Elemento1, Lista2Elemento1, Lista1Elemento2, Lista2Elemento2, etc. 
# De no ser iguales los tamañosde ambas listas, 
# al final de la lista generada deben quedar los elementos de la lista más grande.

lista=[1,2,4,6,10,100,3,8,0,123]
lista2=[3,8,0,123]
listaFinal=[]

for i in range(len(lista)):
    listaFinal.append(lista[i])
    if i < len(lista2):
        listaFinal.append(lista2[i])

print(listaFinal)
