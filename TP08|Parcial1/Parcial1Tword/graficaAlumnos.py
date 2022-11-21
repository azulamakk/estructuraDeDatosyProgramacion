import matplotlib.pyplot as plt
from listaMaterias import *

def graficarAlumnosXMateria():
    cantAlumnos = []
    for materia in listaMaterias:
        cantAlumnos.append(materia.alumnos.longitud)
    materias = [str(materia.codigo) for materia in listaMaterias]
    plt.title(label="Grafico Alumnos X Materia", fontsize=20, color='black')
    plt.xlabel('Materias')
    plt.ylabel('Cantidad de Alumnos')

    plt.bar(materias, cantAlumnos, color='green', width=0.5)
    plt.show()
