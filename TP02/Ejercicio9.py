cadena ="esteeparaestee"
K = 2

for i in range(len(cadena)):
    try:
        if cadena[i:i+K] == cadena[i]*K:
            cadena = cadena.replace(cadena[i:i+K],"")
    except IndexError:
        pass
print(cadena)