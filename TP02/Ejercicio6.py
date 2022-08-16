#Realizar una función que, dada una cadena de caracteres, 
# cuente la cantidad de cada uno de los caracteres que se encuentran en la cadena



def contarCaracteres(cadena):
    caracter = []
    apariencias = []
    for i in range(len(cadena)):
        caracter[i] == cadena[i]
        if cadena[i] in caracter[i]:
            apariencias[i] += 1

        print(caracter[i]+ '    ' +apariencias[i])

cadena="manzana"

contarCaracteres(cadena)
