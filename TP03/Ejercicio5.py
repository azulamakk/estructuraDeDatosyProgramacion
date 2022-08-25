
# Utilice funciones built-in del caso, para crear una nueva lista aañadiendo la palabra ‘Hola’
#  a cada uno delos nombres de las personas que están en una lista dada

listaSaludos=[]
listaNombres=["Ninfa","Nicolas","Juan","Pedro"]
for i in range(len(listaNombres)):
    listaSaludos.append("Hola {}".format(listaNombres[i]))
print(listaSaludos)

