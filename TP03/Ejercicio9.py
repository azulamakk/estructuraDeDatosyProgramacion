#Utilice funciones built-in del caso, para que dadas dos listas de enteros las una en una sola lista de lasiguiente manera: 
# Lista1Elemento1, Lista2Elemento1, Lista1Elemento2, Lista2Elemento2, etc. 
# De no seriguales los tamaños de ambas listas, manejarlo apropiadamente

lista=[1,2,-3, 4, 6, -10]
negativos=filter(lambda dato:dato if dato<0 else '', lista)
print(list(negativos))