class Nota:
    def __init__(self,  nota):
        self.nota = nota
    
class NotaMateria(Nota):
    def __init__(self, nota, materia):
        Nota.__init__(self, nota)
        self.materia = materia

class NotaAlumno(Nota):
    def __init__(self, nota, alumno):
        Nota.__init__(self, nota)
        self.alumno = alumno