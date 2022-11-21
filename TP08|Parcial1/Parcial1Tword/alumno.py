from listaEnlazada import *
from nota import *
class Alumno:
    def __init__(self, legajo, nombre, apellido, materias):
        self.legajo=legajo
        self.nombre=nombre
        self.apellido=apellido
        self.materias=materias
        self.ayudanteEn = ListaEnlazada()
        self.notas = []
    def __str__(self):
        return '''
        Legajo: {}
        Nombre: {}
        Apellido: {}
        Materias: {}
        Aydante En: {}
        Notas: {}
        '''.format(self.legajo, self.nombre, self.apellido, self.materias, self.ayudanteEn, self.notas)

    
    