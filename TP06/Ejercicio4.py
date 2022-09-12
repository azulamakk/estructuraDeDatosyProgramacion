#Realizar una función que determine si dos vectores son iguales. 
# Dos vectores son iguales si y solo si loselementos de uno de los vectores son igual al cuadrado de los elementos del otro vector, 
# sin importar el orden de los elementos.

vectores =('i', [121, 144, 19, 161, 19, 144, 19, 11])
vector = ('i',[121, 14641, 20736, 361, 25921, 361, 20736, 361])

numerosOriginales=vectores[1]
numerosCuadrados=vector[1]

def comprobacionObjetosCuadrados(numerosOriginales,numerosCuadrados):
    cumple=[]
    for i in range(len(numerosOriginales)):
        numeroAlCuadrado=numerosOriginales[i]^2
        if numeroAlCuadrado not in numerosCuadrados:
            cumple.append(True)
        else:
            cumple.append(False)
    if False in cumple:
        return "Los dos vectores no son iguales"
    else:
        return "Los dos vectores son iguales"

print(comprobacionObjetosCuadrados(numerosOriginales,numerosCuadrados))