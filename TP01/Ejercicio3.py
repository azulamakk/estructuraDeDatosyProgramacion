'Se tiene una lista de palabras, todas en minúscula.'
'Hacer una función que genere la lista de palabras a la manera de un diccionario,'
'esto es: sin repetir,agrupadas por inicial, escribiendo la inicial al principio de la lista de palabras que empiezan por esa letra.'
'La lista de palabras quedará al final ordenada por inicial'

def armarDiccionario(listaPalabras):
    letras = []
    matriz = []
    for palabra in listaPalabras:
        letra = palabra[0].lower()
        if letra not in letras:
            letras.append(letra)
    letras.sort()
    for i in range(len(letras)):
        matriz.append(letras[i])
        for palabra in listaPalabras:
            if palabra[0] == letras[1] and palabra not in matriz[1]:
                matriz[i].append(palabra)
    return matriz

listaPalabras = ["cotorra", "caballero", "arbol", "zapato", "familia", "habitacion"]
