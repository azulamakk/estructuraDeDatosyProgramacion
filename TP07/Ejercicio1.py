#Escriba un método permita ingresar un nodo a la lista después de una posición determinada

from array import array

lista=[]
lista=[1,2,4,6,3,8,0,123]

posicion=int(input('Ingrese posicion por favor: '))
nodo=int(input("Ingrese un nodo: "))

lista.insert(posicion, nodo)

print(lista)
    
