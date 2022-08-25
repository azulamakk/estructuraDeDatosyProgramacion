#Realizar una función anónima que tenga como parámetro z y regrese 
# si z es par. Realice el llamado de lafunción anónima correctamente y visualice la respuesta obtenida

from code import interact
from operator import ifloordiv


def nroEsPar(z):
    cociente = z / 2
    if isinstance(cociente, float) == False:
        print("{} no es par".format(z))
    else:
        print("{} es par".format(z))

z=2
nroEsPar(z)