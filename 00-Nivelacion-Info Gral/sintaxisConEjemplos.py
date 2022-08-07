miVar = 7
miVar += 0.3
miVar = "hola"

numero = 7
if numero < 7:
    print("el numero es menor que 7")
elif numero > 7:
    print("el numero es mayor que 7")
else:
    print('el numero es 7')

contador = 0
while contador < numero:
    print(contador)
    contador += 1

print("ingrese un numero entre 1 y 10")

numero = input("ingrese numero: ")

if numero.isnumeric() == False:
    print("Error! El dato ingresado no es un numero")
    exit()

numero = int(numero)

booleanoComoString = str(True)

puntoFlotante = float("1.7")

booleano = bool("False")

print(booleanoComoString)

#comentario

print(numero * 2)

def potencia(numero, exponente):
    resultado = numero
    while exponente > 1:
        resultado *= numero
        exponente -= 1

    return resultado

numeroAlCuadrado = potencia(2, 3)
print(numeroAlCuadrado)

lista = []
lista.append("Nico")
lista.append("Martin")
lista.append("Martin")
lista.append("Augusto")
print(len(lista))

print(lista[len(lista) - 1])



print(lista)


def imprimirLista(lista):
    contador = 0
    while contador < len(lista):
        print(lista[contador])
        contador +=1

def imprimirLista2(lista):
    for elemento in lista:
        print(elemento)

def imprimirLista3(lista):
    for i in range(len(lista)):
        print(lista[i])

imprimirLista2(lista)

numeros = [1, 2, 3, 4, 5]

def duplicarNumerosEnLista(lista):
    contador = 0
    while contador < len(lista):
        lista[contador] *= 2
        contador +=1

#range(N): [0, N)
#range(M, N): [M, N)
for i in range(5):
    print(i)

listaDeListas = [
    [1, 2, 3],
    [4, 5, 6]
]

print(listaDeListas[0][1])