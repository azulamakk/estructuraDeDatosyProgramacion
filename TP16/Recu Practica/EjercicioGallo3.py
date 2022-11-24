class Alumno:
    listaAlumnos=[]
    def __init__(self, nombre:str, dni:int, edad:int):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        Alumno.listaAlumnos.append(self)
    
    def __str__(self):
        return '''
        Nombre: {}
        DNI: {}
        Edad: {}
        '''.format(self.nombre, self.dni, self.edad)
    
    def verLista(self):
        for alumno in Alumno.listaAlumnos:
            print(alumno)

a1=Alumno('Azu', 4444444444, 20)
a2=Alumno('Azu', 4444444444, 20)
a3=Alumno('Azu', 4444444444, 20)
a1.verLista()