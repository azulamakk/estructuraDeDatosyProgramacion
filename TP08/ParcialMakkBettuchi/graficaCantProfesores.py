import matplotlib.pyplot as plt
from listaProfesores import *

def graficaCantMaterias():
    profesores = listaProfesores
    cantidadMateriasXProfesor=[]

    for profesor in listaProfesores:
        cantidadMateriasXProfesor.append(len(listaProfesores.materias))

    plt.pie(cantidadMateriasXProfesor, labels=profesores, autopct='%.2f%%')
    plt.title(label='Cantidad de materias por profesor',
        loc='center',
        color='black')

    plt.show()
