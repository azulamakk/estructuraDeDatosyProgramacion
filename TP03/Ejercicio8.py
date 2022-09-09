#Utilice funciones built-in del caso, para que genere una lista solo con los valores negativos de la lista dada

lista=[-1,2,-3,4,-5,6,7]
negativos=lambda l:[i for i in l if i<0]
print(negativos(lista))