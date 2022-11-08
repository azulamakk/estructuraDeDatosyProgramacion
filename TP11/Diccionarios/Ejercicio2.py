# Realizar una función que dada una lista de palabras y un diccionario que contiene cuantos puntos vale cada
# letra, devolver la palabra cuyo puntaje sea máximo.El puntaje total, 
# se calcula sumando los puntajes de cada una de las letras que la componen 
# (de manera similar a la del juego Scrabble'’).Las letras que no están en el diccionario otorgan 1 punto cada una.
# Las letras que sí están en el diccionario otorgan el valor indicado en el diccionario

puntajesYLetras=dict()
puntajesYLetras={'a':2,'n':3,'f': 5,'z':5}

palabras=['cono','mazazo','fanzine','fhan','marsupial']

listaAcumulado=[]

for palabra in palabras:
    acumulado=0
    for j in range(len(palabra)):
        if palabra[j] in puntajesYLetras:
            acumulado += puntajesYLetras[palabra[j]]
    listaAcumulado.append(acumulado)

print(listaAcumulado)