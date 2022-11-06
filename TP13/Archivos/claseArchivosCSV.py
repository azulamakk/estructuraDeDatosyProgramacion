import csv

# crear archivo csv

# with open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/archivoEjemploCSV.csv', 'w', newline='') as csvFile:
#     writer=csv.writer(csvFile)
#     writer.writerow(['she loves you', 'sep 1963'])
#     writer.writerow(['i want to hold your hand', 'dic 1963'])
#     writer.writerow(['can buy my love', 'abr 1964'])

# # Leer archivo CSV
# print('vamos a leer nuesto primer archivo csv')
# with open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/archivoEjemploCSV.csv', newline='') as csvFile:
#     reader=csv.reader(csvFile)
#     for linea in reader:
#         print(*linea, sep=',')

# Crear nombres a la columna
# Crear archivo con columnas

with open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/archivoEjemploCSV.csv','w', newline='') as csvFile:
    encabezados=['NOMBRE', 'APELLIDO', 'RESULTADO']
    writer=csv.DictWriter(csvFile, fieldnames=encabezados)
    writer.writeheader()
    writer.writerow(
        {'NOMBRE':'Ninfa',
        'APELLIDO':'Delgado',
        'RESULTADO': 100}
    )
    writer.writerow(
        {'NOMBRE':'Tomas',
        'APELLIDO':'Apellido',
        'RESULTADO': 100}
    )

with open('/Users/azulmakk/Desktop/Estructura de Datos/TP13/archivoEjemploCSV.csv', newline='') as csvFile:
    reader=csv.DictReader(csvFile)
    for heading in reader.fieldnames:
        print(heading, end='\t')
    print()
    for linea in reader:
        print(linea['NOMBRE'], '\t', linea['APELLIDO'], '\t', linea['RESULTADO'])