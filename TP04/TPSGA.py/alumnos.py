class Alumnos():
    listaAlumnos = []
    listaLegajos = []
    def __init__( self ):
        self.nombre   = input('Ingrese el nombre del alumno: ')
        self.legajo   = int(input('Ingrese el legajo del alumno: '))
        self.materias = input('Ingrese las materias que cursa el alumno: ').split(',')
        while self.legajo in Alumnos.listaLegajos:
            print('El legajo ingresado ya se encuentra en el sistema, introduzca otro')
            self.legajo = int(input('Ingrese el legajo del alumno: '))
        else:
            Alumnos.listaLegajos.append(self.legajo)
            Alumnos.listaAlumnos.append(self)
            
    @classmethod #-- si usamos el classmethod no tenemos que pasarle la clase cuando llamamos a la funcion-- porque es una funcion directa de la clase y no sobre el objeto
    def listaDeAlumnos( self ):
        return Alumnos.listaAlumnos
    
    def mostrarAlumnos(self):
        detalleAlumnos = {}
        for alumno in Alumnos.listaDeAlumnos():
            detalleAlumnos[alumno.legajo] = alumno.materias
        return detalleAlumnos