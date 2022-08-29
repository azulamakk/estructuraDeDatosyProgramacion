#Realizar una función anónima que tenga como parámetro z y regrese 
# si z es par. Realice el llamado de lafunción anónima correctamente y visualice la respuesta obtenida

funcion = lambda numero:numero%2==0

if funcion(3):
    print("Es par")
else:
    print("Es impar")