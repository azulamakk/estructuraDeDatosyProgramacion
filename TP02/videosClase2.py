
import string

# print(string.digits)
# print(string.punctuation)
# print(string.ascii_letters)

# print('a' in string.digits)
# print('a' in string.ascii_letters)

frase = "Anita lava la tina"
# print(frase.find("la"))
# print(frase.find("la", 8, 11))

# print(frase.index("la"))

# print(frase.count("a"))

# print(frase.replace("i", "o"))
# print(frase)
# frase = frase.replace("i", "o")
# print(frase)

# print(frase.strip())
# lista = frase.split()
# print(lista)

fecha = "11.03/2022"
listaFecha = fecha.split("/")
print(listaFecha)

frase1 = ".".join(listaFecha)
print(frase1)
# print(type(frase1))

# print(frase.isdigit())
# print(frase.isalpha())

numero="11223344"
print("El numero introducido fue {}".format(numero))