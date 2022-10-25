class Alumno:
    def __init__(self, legajo, nombre, apellido, materias, ayudantia):
        self.legajo=legajo
        self.nombre=nombre
        self.apellido=apellido
        self.materias=materias
        self.ayudantia=ayudantia
        self.notas=[]

    def __str__(self):
        return '''
        Legajo: {}
        Nombre: {}
        Apellido: {}
        Materias: {}
        Cantidad de ayudantias: {}
        Notas: {}
        '''.format(self.legajo, self.nombre, self.apellido, self.materias, self.ayudantia, self.notas)

    
    