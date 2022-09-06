
listadoMaterias = []

from profesores import profesores
from alumnos import alumnos

class materias(profesores):
    def __init__(self, codigoMateria, cuatrimestre, nombre, profesor, departamento, legajoProfesor, legajoAlumno):
        self.codigoMateria=codigoMateria
        self.nombre=nombre
        self.cuatrimestre=cuatrimestre
        self.profesor=profesor
        self.departamento=departamento
        profesores.__init__(self, legajoProfesor)
        alumnos.__init__(self, legajoAlumno)

