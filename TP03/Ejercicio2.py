#Realizar una función que tenga como parámetro z y regrese el valor de z al cuadrado. 
# Realice el llamado dela función y visualice la respuesta obtenida

def numeroAlCuadrado(numero):
    return numero**2

num = int(input("ingrese un numero: "))
print(num, " elevado al cuadrado es ", numeroAlCuadrado(num))