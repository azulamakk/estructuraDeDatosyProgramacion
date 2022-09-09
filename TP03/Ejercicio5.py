# Utilice funciones built-in del caso, para crear una nueva lista aañadiendo la palabra ‘Hola’
#  a cada uno delos nombres de las personas que están en una lista dada

listaNueva=[]
listaNombres=["Ninfa","Nicolas","Juan","Pedro"]

listaNueva=list(map(lambda dato: 'Hola '+dato, listaNombres))
print(listaNueva)

