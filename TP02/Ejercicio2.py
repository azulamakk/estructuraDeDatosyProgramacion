#Realizar una función que, dada una cadena de caracteres y un 
#carácter como parámetros, encuentre la cantidad máxima de ocurrencias del carácter en la cadena.

cadena= "Welcome to w3resource.com"

caracterBuscado= input("Por favor ingrese el caracter buscado: ")

ocurrencias = 0

for i in range(len(cadena)):
    if cadena[i] == caracterBuscado:
        ocurrencias += 1

print("Cantidad de veces que se repitió: "+str(ocurrencias))

