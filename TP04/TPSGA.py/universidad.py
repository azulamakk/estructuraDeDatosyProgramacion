from alumnos import *
from profesores import *
from materias import *

class Universidad():
    def __init__(self,nombre, profesores, alumnos, materias):
        self.nombre = nombre
        self.profesores = profesores
        self.alumnos = alumnos
        self.materias = materias
        
    

itba = Universidad('ITBA', Profesores.listaDeProfesores, Alumnos.listaDeAlumnos, Materias.listaDeMaterias)

    