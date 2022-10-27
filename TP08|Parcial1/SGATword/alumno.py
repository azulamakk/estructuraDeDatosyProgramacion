class Alumno:
    def __init__(self, legajo, nombre, apellido, materias):
        self.legajo=legajo
        self.nombre=nombre
        self.apellido=apellido
        self.materias=materias

    def __str__(self):
        return '''
        Legajo: {}
        Nombre: {}
        Apellido: {}
        Materias: {}
        '''.format(self.legajo, self.nombre, self.apellido, self.materias)

    
    