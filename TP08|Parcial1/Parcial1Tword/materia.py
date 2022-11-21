from listaEnlazada import *

class Materia:
    def __init__(self, codigo, nombre, creditos, profesores):
        self.codigo=codigo
        self.nombre=nombre
        self.profesores=profesores
        self.creditos=creditos
        self.alumnos=ListaEnlazada()
        self.notas=[]
    def __str__(self):
        return '''
        Codigo: {}
        Nombre: {}
        Profesor: {}
        Alumnos: {}
        Creditos: {}
        Notas: {}
        '''.format(self.codigo, self.nombre, self.profesores, self.alumnos, self.creditos, self.notas)
    
