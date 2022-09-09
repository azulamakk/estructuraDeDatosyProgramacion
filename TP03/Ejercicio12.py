#Utilice funciones built-in del caso que, dada una lista de números enteros genere una nueva lista en la
# cual los números menores de 9000 se les haya sumado 3000

lista1=[1000,500,600,700,5000,90000,17500]
listaFinal=[]
def condicion(x):
    if x<9000:
        listaFinal.append(x+3000)
    else:
        listaFinal.append(x)

list(map(condicion, lista1))
print(listaFinal)