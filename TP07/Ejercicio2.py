#Escriba un método permita ingresar un nodo a la lista por referencia, 
# es decir dado el valor de un dato enla lista introducir un nuevo nodo inmediatamente después del anterior

lista=[1,2,4,6,100,3,8,0,123]
valorDado=int(input('Ingrese el valor buscado: '))
posicionNodoNuevo=lista.index(valorDado)+1
nodoNuevo=int(input('Inserte el valor nuevo: '))
lista.insert(posicionNodoNuevo, nodoNuevo)
print(lista)