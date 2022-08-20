import string

frase = 'abc'
cadena=[]
for i in string.ascii_lowercase:
    repeticiones = frase.count(i)
    if repeticiones != 0:
        fraseNueva = i + hex(repeticiones).replace('Ox', '')
        cadena.append(fraseNueva)
        
