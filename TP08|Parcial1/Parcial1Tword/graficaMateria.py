from matplotlib import pyplot as plt
from listaProfesores import *

def graficarMateriasXProfesor():
    cantMaterias = []
    for profesor in listaProfesores:
        cantMaterias.append(profesor.materias.longitud)
    profesores = [str(profesor.legajo) for profesor in listaProfesores]
    plt.title(label="Grafico Materias X Profesor", fontsize=20, color='black')
    plt.xlabel('Profesores')
    plt.ylabel('Cantidad de Materias')

    plt.bar(profesores, cantMaterias, color='green', width=0.5)
    plt.show()
