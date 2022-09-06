frase ="abc"
lista = []
texto = ""
for char in frase:
    if char not in lista:
        lista.append(char)
lista.reverse()
for char in lista:
    texto += str(hex(frase.count(char)))[2:]+char
print(texto)