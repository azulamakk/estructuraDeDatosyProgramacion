import sys
import os.path

sys.path.append('/Users/azulmakk/Desktop/Estructura de Datos/TP03/claseTeorica1208.py')
from TP03.claseTeorica1208 import *

# Primera forma de crear un diccionario
ninfa=Persona('Ninfa', 555555, 20, 'F')
dana=Persona('Dana', 911111, 20, 'F')
maria=Persona('Maria', 932222, 20, 'F')

diccionario={}
print(diccionario)

# Segunda forma de crear un diccionario
diccionario1=dict()
print(diccionario1)

# Llenar diccionario Primer forma de llenado
diccionario['ninfa']=ninfa
diccionario['pedro']=dana
diccionario['maria']=maria

print(diccionario)
print(diccionario['pedro'])

diccionario['pedro']=ninfa
print(diccionario['pedro'])

diccionario['dana']=dana
print(diccionario['dana'])

print(len(diccionario))

# Segunda forma de crear un diccionario
diccionario1={'total':55, 10: 'Estructura de datos', 'a':25}
print(diccionario1)

# Verificar si una clave esta en un diccionario
if 'total' in diccionario1:
    print(True)
else:
    print(False)

print(11 in diccionario1)

# Llaves de un diccionario
print(diccionario1.keys())

# Valores en un diccionario
print(diccionario1.values())

# Todos los items del diccionario
print(diccionario1.items())

for keys, values in diccionario1:
    print(keys, '------->', values)