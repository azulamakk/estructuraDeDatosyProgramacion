

class alumnos():
    def __init__(self, tipoDocumento, nroDocumento, nombre, apellido, legajo):
        self.tipoDocumento=tipoDocumento
        self.nroDocumento=nroDocumento
        self.nombre=nombre
        self.apellido=apellido
        self.legajo=legajo

class profesores():
    def __init__(self, tipoDocumento, nroDocumento, nombre, apellido, matricula, ):
        self.tipoDocumento=tipoDocumento
        self.nroDocumento=nroDocumento
        self.nombre=nombre
        self.apellido=apellido
        self.matricula=matricula

class materias():
    def __init__(self, codigo, nombre, departamento):
        self.codigo=codigo
        self.nombre=nombre
        self.departamento=departamento