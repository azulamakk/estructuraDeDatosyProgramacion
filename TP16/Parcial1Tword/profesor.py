from listaEnlazada import *

class Profesor:
    def __init__(self, legajo, nombre, apellido):
        self.legajo=legajo
        self.nombre=nombre
        self.apellido=apellido
        self.materias=ListaEnlazada()

    def __str__(self):
        return '''
        Legajo: {}
        Nombre: {}
        Apellido: {}
        Materias: {}
        '''.format(self.legajo, self.nombre, self.apellido, self.materias)
    
    def agregarMateria(self, codigoMateria):
        self.materias.agregar(codigoMateria)
    