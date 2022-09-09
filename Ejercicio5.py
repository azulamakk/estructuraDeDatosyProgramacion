#Diseña una función que, dada una matriz, determine si la suma de los elementos de cualquiera de sus 
# filas es igual a la suma de los elementos de cualquiera de sus columnas.

from ipaddress import summarize_address_range
import numpy as np

Matriz1=np.array([[ 50, 75, 46],[ 22, 80, 125]])
Matriz=Matriz1[0]
listaSumasColumnas=[]
listaSumasFilas=[]

def comprobacionSumas():
    for i in range(len(Matriz)):
        listaSumasFilas.append(sum(Matriz[i]))
        for j in range(len(Matriz[i])):
            listaSumasColumnas[j]+= Matriz[i][j]
        if listaSumasFilas[i] in listaSumasColumnas:
            return "Estas matrices son iguales"
        else:
            return 'Estas matrices no son iguales'
    
print(comprobacionSumas())