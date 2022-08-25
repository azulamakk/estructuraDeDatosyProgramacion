#Usted es el nuevo CEO del ITBA y encontró inconsistencias en la base de datos, en la cual existenredundancias y 
# decide renovar la base de datos del SGA, para lo cual ha llamado a varias empresas de desarrollo de software entre ellas 
# incluida la suya, para que le presenten diferentes diseños y entre ellos poder escoger cual sería el nuevo diseño del programa del SGA.
# Entre los requerimientos que pide están:
# - Quiero un Código que genere una lista de alumnos (que verifique si se repite el legajo o no).
# - Que haya una lista de profesores.
# - Que haya una lista de materias (solo acepta un profesor titular).
# - Deben existir métodos o funciones que nos permitan obtener la lista de profesores de un alumno.
# - Método que permita determinar que materias dicta un profesor.
# Una vez expuestos los diseños de las diferentes empresas, se escogerá un solo diseño, el cual deberá serimplementado por las empresas


class alumnos():
    def __init__(self, nombre, apellido, tipoDocumento, nroDocuemnto, legajo, nacionalidad, planDeEstudio):
        self.nombre=nombre
        self.apellido=apellido
        self.tipoDocumento=tipoDocumento
        self.nroDocumento=nroDocuemnto
        self.legajo=legajo
        self.nacionalidad=nacionalidad
        self.planDeEstudio=planDeEstudio
        
    


