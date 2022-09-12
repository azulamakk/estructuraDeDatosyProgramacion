class Materias():
    listaMaterias = []
    listaProfesorTitular = []
    def __init__(self):
        self.nombre = input('Ingrese el nombre de la materia: ')
        self.profesorTitular = [ input('Ingrese nombre del profesor titular: ') ]
        Materias.listaMaterias.append(self)
        Materias.listaProfesorTitular.append(self.profesorTitular)
        while len(self.profesorTitular) > 1:
            print('La materia solo puede tener un profesor titular, introduzca otro')
            self.profesorTitular = [ input('Ingrese nombre del profesor titular: ') ]
        else:
            Materias.listaMaterias.append(self)
            Materias.listaProfesorTitular.append(self.profesorTitular)
            
            
    @classmethod
    def listaDeMaterias(self):
        return self.listaMaterias