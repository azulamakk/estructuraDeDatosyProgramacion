
# Filter(funcion, iterable)

from subprocess import list2cmdline


lista=[2,3,1,5,8]
#creamos lista con los elementos impares de la lista original
def impares(dato):
    return dato%2!=0

# primer forma de solucion
listaImpares = list(filter(impares, lista))
print(listaImpares)

# segunda forma de solucion
listaImpares=list(filter(lambda dato:dato%2!=0, lista))
print(listaImpares)

# tercer forma de solucion
listaImpares=list(filter(lambda dato : dato if dato%2!=0 else ' ',lista))
print(listaImpares)

# Ejemplo 2
# Dada una lista de nombres vamos a generar una nueva lista con los nombres que empiecen con vocal
nombres=['Ninfa', 'Abril', 'Facundo', 'Agustina', 'Ian', 'Maria']
vocales=['a', 'e', 'i', 'o', 'u'] 

# primera forma de solucion
listaNombres=list(filter(lambda nombre:nombre[0] if nombre[0].lower() in vocales else '',nombres))
print(listaNombres)

# segunda forma de solucion
listaNombres=list(filter(lambda nombre:nombre[0].lower() in vocales,nombres))
print(listaNombres)

# Map
# Sintaxis 
# map(funcion, iterable)

# Ejemplo 1
# priemra forma de solucion
sumar=lambda dato:dato+2
print(list(map(sumar, lista)))

# segunda forma de solucion
sumar=list(map(lambda dato:dato+2, lista))
print(sumar)

# Dada una lista de palabras generar una nueva lista con la longitud de cada una de las primeras
palabras=['saturno', 'bata', 'mate', 'Qatar']
print(list(map(lambda palabra:len(palabra), palabras)))

####### ZIP #######
paises=['China', 'India', 'Estados Unidos', 'Indonesia']
poblaciones= [1391,1364, 327, 264]

lista=list(zip(paises, poblaciones))
print(lista)

# Ejemplo 2
paises=['China', 'India', 'Estados Unidos', 'Indonesia']
poblaciones= [1391,1364, 327, 264]
codigosPostales=[86, 91, 1]

lista=list(zip(paises, poblaciones, codigosPostales))
print(lista)

# Ejemplo 3
# Usar zip con un ciclo . zip contiene 
for pais, codigosPostales in zip(paises, codigosPostales):
    print(pais, 'Su codigo postal es ', codigosPostales)

# Ejemplo 4
# Desempaquetar
lista=['a1', 'a2', 'a3', 'a4']
listaFinal=list(zip(*lista))
print(listaFinal)