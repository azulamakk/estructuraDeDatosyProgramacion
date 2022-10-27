class Materia:
    def __init__(self, codigo, nombre, profesor):
        self.codigo=codigo
        self.nombre=nombre
        self.profesor=profesor
        self.alumnos=[]

    def __str__(self):
        return '''
        Codigo: {}
        Nombre: {}
        Profesor: {}
        Alumnos: {}
        '''.format(self.codigo, self.nombre, self.profesor, self.alumnos)
    