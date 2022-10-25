import matplotlib.pyplot as plt
from listaMaterias import *

def graficaAlumnosXMateria():
    materias = listaMaterias
    cantidadAlumnosXMateria=[]
    for materia in listaMaterias:
        cantidadAlumnosXMateria.append(len(listaMaterias.alumnos))

    plt.title(label="Cantidad de alumnos por materia", fontsize=20, color='black')
    plt.xlabel('Materias')
    plt.ylabel('Cantidad de alumnos')


    plt.bar(materias, cantidadAlumnosXMateria, color='green', width=0.5)
    plt.show()