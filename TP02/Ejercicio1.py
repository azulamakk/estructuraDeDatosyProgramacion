#Realizar una función que permita contar la cantidad total de caracteres alfabéticos, 
#dígitos o caracteresespeciales en una cadena.

import string

cadena= "Welcome to w3resource.com"

alfabeticos=0
digitos=0
caracterEspecial=0

for i in range(len(cadena)):
    if cadena[i].isnumeric():
        digitos+=1
    if cadena[i].isalpha():
        alfabeticos+=1
    if cadena[i] in string.punctuation or cadena[i] in string.whitespace:
        caracterEspecial+=1

print("Cantidad de letras: "+str(alfabeticos))
print("Cantidad de numeros: "+str(digitos))
print("Cantidad de caracteres especiales: "+str(caracterEspecial))
