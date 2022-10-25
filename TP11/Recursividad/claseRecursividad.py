# Factorial
# Solucion: proceso iterativo
# 5!= 1*2*3*4*5
# 7!= 1*2*3*4*5*6*7
# Factorial de un numero es un producto acumulativo desde 1 hasta el numero
# Generar desde 1 hasta un numero: for o while

def factorialIterativos(dato):
    acumumulti=1
    for i in range(1, dato+1):
        acumumulti*=i
    return (acumumulti)

print(factorialIterativos(7))

# Proceso recursivo
# Funcion que se llame a ella misma
# 5!= 5*4!
# 4!= 4*3!
# 3!= 3*2!
# 2!= 2*1!
# 1!= 1*0!
# 0!= 1

def factorialRecursiva(dato):
    if (dato==0 or dato==1): # Caso base
        return 1
    else:
        return dato*factorialRecursiva(dato-1)

print((factorialIterativos(int(4))))
print((factorialRecursiva(int(4))))

print('****************************')
# Calculo la potencia de a**b en forma recursiva
# a**b recursivamente
# 3**4 --> 3*3*3*3 iterativa
# Recursiva:
# 3**4 = 3**(4-1)
# 3**3 = 3**(3-1)
# 3**2 = 3**(2-1)
# 3**1 = 3**(1-1)
# 3**0 = 1 ---> caso base

def potencialRecursiva(dato, potencia):
    if potencia==0:
        return 1
    else:
        return 3*potencialRecursiva(dato, potencia-1)

print(potencialRecursiva(3,2)) 