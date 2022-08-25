# def imprimirSaludo():
#     print("Buenos dias, bienvenidos otra vez")

# imprimirSaludo()

# def imprimirSaludo(saludo):
#     print(saludo)

# saludo='''Menu:
# 1- Agregar DataSource
# 2- Mostrar promedio
# 3- Salir'''

# imprimirSaludo(saludo)

# def potenciaDatos(base, exp):
#     potencia=base**exp
#     return potencia, potencia>200

# dato, dato1=potenciaDatos(base=3, exp=4)
# print(dato)
# print(dato1)

# dato, dato1=potenciaDatos(exp=4, base=8)
# print(dato)
# print(dato1)

# dato, dato1=potenciaDatos(4, 8)
# print(dato)
# print(dato1)

# def areaCirculo(radio, pi=3.14):
#     return pi*(radio*2)

# print(areaCirculo(radio=2))
# print(areaCirculo(radio=2,pi=3.1415267))

# def computeAndPrint(x,y):
#     val=x**44.0-x**33.0 - 3*x*x + y
#     print("Llamamos a computeAndPrint (" + str(x)+","+str(y))
#     return val

# print(computeAndPrint(6,5))

def cambiaDatos(lista):
    lista[2]=8

datos=[2,5,0,2]
cambiaDatos(datos)
print(datos)

animal='Leon'

def imprimirAnimal():
    animal='Ballena'
    print(animal)
    print(id(animal))

imprimirAnimal()

def imprimirAnimal2():
    global animal
    animal="Gato"
    print(animal)

imprimirAnimal2()