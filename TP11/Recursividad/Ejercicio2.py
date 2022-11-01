# Escribir un método recursivo que permita sumar los dígitos de un número entero positivo. 
# Por ejemplo, si elnúmero es 1234 la respuesta será 10.

str='1234'

def sumarDigitos(str):
    acumulado=0
    for i in range(len(str)):
        acumulado+=int(str[i])
    return acumulado

print(sumarDigitos(str))