#Realizar una función que, dada una cadena de caracteres encuentre y visualice la palabra mas larga y lamás pequeña dentro de esta.

cadena = "Estructura de Datos"

cadenaDividida = cadena.split(" ")


cantidadCaracteres = []
cadenaCorta=""
cadenaLarga=""

for i in range(len(cadenaDividida)):
    for j in cadenaDividida[i]:
        cantidadCaracteres[j] = len(cadenaDividida[i][j])   



print(cantidadCaracteres)