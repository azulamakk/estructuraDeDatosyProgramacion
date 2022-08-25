# lambda
# filter
# map
# zip

# Funciones lambda
# Funciones anonimas (no tienen nombre)
# Funciones anonimas (parametros: un, varios, ningun)
# Funciones anonimas (una sola instruccion)

# Funcion que permita calcular un numero elevado al cuadrado
from doctest import DONT_ACCEPT_TRUE_FOR_1
from itertools import product
from unittest import result


def elevarCuadrado(dato):
    return dato**2

print(elevarCuadrado(4))

# Lambda elevarCuadrado
lambda dato: dato**2
cuadrado = lambda dato: dato**2
print(cuadrado(5))

# Ejemplo donde lambda no tiene datos de entrada
saludo =lambda : "Hola"
print(saludo())

# Suma de numeros
suma=lambda dato,dato1:dato+dato1
print(suma(3,5))

# Generar una matriz que contenga solamente los numeros impares de una lista inicial
lista=[2,3,1,5,8]
listaNueva=lambda lista:[dato for dato in lista if dato%2!=0]
lista1=(listaNueva(lista))
print(lista1)

# Dada una matriz generar una funcion lambda que cree una lista con la suma de las filas de la matriz
matriz=[[2,3,1,5,8],[2,3,1,5,8],[2,3,1,5,8]]
sumaFilas=lambda matriz:[sum(fila) for fila in matriz]
listaSumaFilas=sumaFilas(matriz)
print(listaSumaFilas)

# Devolver una funcion anonima a traves de una funcion no anonima
# Crear un programa que me permita multiplicar un numero dado con un valor desconocido
def multiplicar(n):
    return lambda x:x*n
producto=multiplicar(3)
resultado=producto(5)
print(resultado)