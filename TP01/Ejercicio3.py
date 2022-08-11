'Se tiene una lista de palabras, todas en minúscula.'
'Hacer una función que genere la lista de palabras a la manera de un diccionario,'
'esto es: sin repetir,agrupadas por inicial, escribiendo la inicial al principio de la lista de palabras que empiezan por esa letra.'
'La lista de palabras quedará al final ordenada por inicial'

def armarDiccionario(lista):
    letras = []
    matriz = []
    for palabra in lista:
        letra = palabra[0].lower()
        if letra not in letras:
            letras.append(letra)
    letras.sort()
    for i in range(len(letras)):
        matriz.append([letras[i]])
        for palabra in lista:
            if palabra[0] == letras[i] and palabra not in matriz[i]:
                matriz[i].append(palabra)
    return matriz

listaPalabras = ["cotorra", "caballero", "arbol", "zapato", "familia", "habitacion"]

print("diccionario =", armarDiccionario(listaPalabras))
