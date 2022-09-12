class Profesores():
    listaProfesores = []   
    def __init__( self):
        self.nombre   = input('Ingrese el nombre del profesor: ')
        self.materias = input('Ingrese las materias que dicta el profesor: ').split(',')
        Profesores.listaProfesores.append(self)
        
    @classmethod
    def listaDeProfesores( self ):
        return self.listaProfesores

    def mostrarProfesores( self ):
        detalleProfesores = {}
        for profesor in Profesores.listaDeProfesores():
            detalleProfesores[profesor.nombre] = profesor.materias
        return detalleProfesores
    
# agostina = Profesores('Agostina', ['Estructura de Datos'])
# ninfa = Profesores('Ninfa', ['Informatica General'])
        