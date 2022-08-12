#Realizar una función que, dada una cadena de caracteres reemplace las letras minúsculas por mayúsculas y viceversa.

import string

cadena= "Welcome to w3resource.com"
cadenaNueva = ""

for i in range(len(cadena)):
    if (cadena[i].isnumeric() or cadena[i] in string.whitespace or cadena[i] in  string.punctuation):
        cadenaNueva+=cadena[i]
    elif cadena[i] in string.ascii_lowercase:
        cadenaNueva+=cadena[i].upper()
    elif cadena[i] in string.ascii_uppercase:
        cadenaNueva+=cadena[i].lower()

print(cadenaNueva)