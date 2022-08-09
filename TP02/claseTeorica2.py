#Fecha Clase 2 08/08/2022

def crearMatriz(filas, columnas):
    lista=[None]*filas
    for i in range(filas):
        lista[i] = [None] * columnas
    return lista

def verMatriz(lista):
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            print(lista[i][j], end="\t")
        print()

lista = crearMatriz(3,5)
print(lista)
verMatriz(lista)
lista[1][3] = 8
print(lista)
verMatriz(lista)


