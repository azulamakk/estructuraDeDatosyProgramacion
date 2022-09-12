#Diseña una función que, dado un vector de números enteros, visualice el vector que la suma de suselementos sea la mayor

import numpy as np 

Array= np.array([ [1,2,3], [4,5,6], [10,11,12], [7,8,9]])

listaSumas=[]
def vectorMayor(Array):
    for i in range(len(Array)):
        listaSumas.append(sum(Array[i]))
    maximo=max(listaSumas)
    posicionMaximo = listaSumas.index(maximo)
    return Array[posicionMaximo]
    
print(vectorMayor(Array))
        


