#Diseña una función que, mueva todos los ceros (0) que aparezcan en un vector al final de este.

from unittest import result


vector= ('i',[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1])


def moverCeros(vector):
    listaDeCerosEliminados = []
    listaSinCeros = []
    listaFinal = []
    vectorATrabajar=vector[1]
    for i in range(len(vectorATrabajar)):
        if vectorATrabajar[i] == 0:
            listaDeCerosEliminados.append(0)
        else:
            listaSinCeros.append(vectorATrabajar[i])
    listaFinal = listaSinCeros + listaDeCerosEliminados
    return listaFinal


print(moverCeros(vector))
