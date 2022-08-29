
def mayorMenor(dato1, dato2):
    if dato1>dato2:
        return True
    else:
        return False

#print(mayorMenor(41,5))

# Lambda --> sin sombre
# Solo puedo escribir una expresion

dato=4
dato1=120
verificar=lambda dato, dato1:dato>dato1
print(verificar(dato,dato1))

# Filter
# Tenemos una lista de palabras y vamos a crear otra 
# lista con las palabras de la lista que empiecen con c

lista=['hola', 'como', 'estas', 'con', 'tu', 'nueva', 'casa']
def estaLetra(lista):
    listaNueva=[]
    for palabra in lista:
        if (palabra[0].lower()=='c'):
            listaNueva.append(palabra)
        return listaNueva

print(estaLetra(lista))

# Sintaxis
# filter(funcion, iterable)

def buscarC(palabra):
    if palabra[0].lower() == 'c':
        return palabra

# print(buscarC('como'))
listaC=list(filter(buscarC, lista))
print(listaC)

listaC =list(filter(lambda palabra: palabra if palabra[0].lower()=='c' else '', lista))
print(listaC)

listaC =list(filter(lambda palabra:palabra[0].lower()=='c', lista))
print(listaC)

# pedir dato al usuario
def pedirDato():
    letra=input('Introduzca letra')
    return letra.lower()

def buscarLetra(letra):
    return lambda palabra:palabra[0].lower()==letra

letra=pedirDato()
ListaUy=list(filter(buscarLetra(letra), lista))
print(ListaUy)