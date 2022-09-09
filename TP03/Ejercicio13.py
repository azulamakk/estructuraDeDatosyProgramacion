#Utilice funciones built-in del caso que, dada una lista de números enteros genere una nueva lista en la con
# los números menores de 9000 y se les haya sumado 3000.

lista=[1000,500,600,700,5000,90000,17500]
valores= lambda l: [i+3000 for i in l if i < 9000]
print(valores(lista))