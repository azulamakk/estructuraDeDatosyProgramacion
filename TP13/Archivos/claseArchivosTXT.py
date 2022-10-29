import sys
import os.path

# 3 acciones basicas
# Abrir ---> open('nombre_ubicacion', procesar)
# Procesar ---> leer ---> r
#               escribir ---> w
#               agregar informacion ---> a
# Cerrar ---> close()

# # Abrir el archivo
# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP08|Parcial1/correccion.txt')
# #print(archivo)
# archivo.close()

# # Abrir el achivo y leerlo
# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP08|Parcial1/correccion.txt')
# #print(archivo.read())
# archivo.close()

# # Abrir el achivo y leerlo
# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP08|Parcial1/correccion.txt', 'r')
# print(archivo.read(5)) # cant caracteres que quiero que lea
# archivo.close()

# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP08|Parcial1/correccion.txt', 'r')
# #print(archivo.readable()) 
# archivo.close()

# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'w')
# print(archivo.readable()) 
# archivo.close()

# # Lee la primera linea del archivo
# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'r')
# print(archivo.readline()) 
# archivo.close()

# # Leer todas las lineas del archivo
# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'r')
# print(archivo.readlines()) 
# archivo.close()

# archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'r')
# print(archivo.readlines()) 
# archivo.close()

# Leer un archivo utilizando el operador with
# Ventaja es que automaticamente cierra el achivo 
with open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'r') as archis:
    print(archis.readlines())

# Leer primera linea de un archivo
# Primera forma
with open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'r') as archis:
    for linea in archis:
        print(linea)

archivo=open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'r')
for linea in archivo:
    print(linea)
archivo.close()

print('******* saco cambio de linea de cada linea del archivo')
with open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', 'r') as archis:
    for linea in archis:
        if (linea[-1]=='\n'):
            linea=linea[:-1]
        print(linea)

# Cambiar el nombre del archivo
os.rename('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolito.txt', '/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolote.txt')
os.remove('/Users/azulmakk/Desktop/Estructura de Datos/TP13/arbolote.txt')