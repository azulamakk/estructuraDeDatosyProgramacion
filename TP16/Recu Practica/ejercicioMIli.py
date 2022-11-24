#Usted debe implementar la clase Alumno en la cual tiene los atributos de nombre, 
# edad y DNI único de los alumnos que cursan en una escuela. 
# El listado de todos los alumnos debe poderse imprimir en cualquier momento. 
# Utilice una sola estructura que permita lograr este objetivo y límite su código a la clase Alumno.
# Suponga que otro desarrollador es el encargado de escribir el main, usted puede hacer 
# uno para probar laclase creada pero no forma parte de la nota. 
# Garantice que no existirán Alumnos inválidos
listaAlumnos = []

class Alumno:
    def __init__(self, nombre, dni, edad):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        listaAlumnos.append(self)

    def __str__(self):
        return ''''
        Nombre: {}
        DNI: {}
        Edad: {}
        '''.format(self.nombre, self.dni, self.edad)
        

def agregarAlumno():
    nombre=str(input('Ingrese nombre del estudiante: '))

    dni = input('Ingrese DNI del estudiante: ')
    while dni.isnumeric()==False or len(dni)!=8:
        print('Ingrese un codigo de materia valido')
        dni = input('Ingrese DNI del estudiante: ')
    if dni in listaAlumnos:
        print('El dni se encuentra registrado, intente de nuevo')
        dni = input('Ingrese DNI del estudiante: ')
    
    edad = input('Ingrese la edad estudiante: ')
    while edad.isnumeric()==False or edad<0 or edad>100:
        print('Ingrese una edad valida')
        dni = input('Ingrese edad del estudiante: ')
    alumno = Alumno(nombre, dni, edad)

azul = Alumno('Azul',44451568, 20)
tatu = Alumno('Tatu',44451568, 22)
# print(azul)

def visualizarAlumnos(lista):
    for alumno in lista:
        print(alumno)
visualizarAlumnos(listaAlumnos)