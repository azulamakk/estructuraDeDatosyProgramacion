


class alumnos():
    listadoAlumnos=[]
    listaLegajos=[]
    def __init__(self, nombre, apellido, tipoDocumento, nroDocuemnto, legajoAlumno, nacionalidad, planDeEstudio):
        self.nombre=nombre
        self.apellido=apellido
        self.tipoDocumento=tipoDocumento
        self.nroDocumento=nroDocuemnto
        self.legajoAlumno=int(input('Ingrese el legajo del alumno: '))
        self.nacionalidad=nacionalidad
        self.planDeEstudio=planDeEstudio
        while self.legajoAlumno in alumnos.listaLegajos:
            print('El legajo ingresado ya se encuentra en el sistema, intriduzca otro')
            self.legajo = int(input('Ingrese el legajo del alumno: '))
        else:
            alumnos.listaLegajos.append(self.legajo)
            alumnos.listadoAlumnos.append(self)

    @classmethod
    def listadoAlumnos(self):
        return alumnos.listadoAlumnos

    def mostrarAlumnos(self):
        detalleAlumnos = {}
        for alumno in alumnos.listadoAlumnos():
            detalleAlumnos[alumno.legajoAlumno] = alumno.materias
        return detalleAlumnos
