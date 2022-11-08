# Escribir un método recursivo, que calcule la suma de los elementos de una lista secuencial.

lista =[1,2,3,4,5,6]

def sumaLista(lista, acumulado):
    if len(lista) == 0:
        return acumulado
    
    acumulado += lista[0]
    lista.pop(0)
    return sumaLista(lista, acumulado)

print(sumaLista(lista, 0))