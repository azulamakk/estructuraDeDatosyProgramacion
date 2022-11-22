import csv

lista1 = [1,2,3,4,5,6,7,8]
lista2 = [1,2,3,9]

def compararListas(lista1, lista2):
    if len(lista1) <= len(lista2):
        for i in range(len(lista1)):
            if lista1[i] not in lista2:
                return False
            
        return True
    else:
        for i in range(len(lista2)):
            if lista2[i] not in lista1:
                return False
            
        return True

if compararListas(lista1, lista2):
    print('Es subconjunto')
else:
    print('No es subconjunto')

with open('TP16/Recu Practica/recuej4.csv', 'w', newline='') as csvFile:
    writer=csv.writer(csvFile)
    for elemento in lista1:
        writer.writerow([elemento])