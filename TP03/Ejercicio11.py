#Utilice funciones built-in del caso que, dada una cadena de caracteres genere una lista con las vocales
# (mayúsculas y minúsculas )que se encuentren en ella.

def vocal(letra):
    vocales='aeiouAEIOU'
    if letra in vocales:
        return letra

cadena = "Estructura de datos"
lista=list(filter(vocal, cadena))
print(lista)