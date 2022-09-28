#Escriba un método iterativo que tiene como entrada una lista de datos enteros y elimina de la misma los nodos de posiciones pares

lista=[1,2,4,6,10,100,3,8,0,123]

for i in range(len(lista)):
    if i%2==0 and i<len(lista):
        lista.pop(i-1)

print(lista)