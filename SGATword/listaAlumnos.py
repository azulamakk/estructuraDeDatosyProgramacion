from alumno import *
from listaMaterias import *

listaAlumnos = []

def agregarAlumno():
    legajo=input('Por favor ingrese el numero de legajo: ')
    if legajo.isnumeric() == False or legajoExiste(int(legajo))==True:
        print('Ingrese un numero de legajo valido')
        return
    legajo=int(legajo)

    nombre=input('Ingrese el nombre: ')

    apellido=input('Ingrese el apellido: ')

    materiasCursada=[]
    materia=input('Por favor ingrese las materias que esta cursando. Presione enter cuando haya finalizado: ')

    while materia != '':
        if materia.isnumeric() == False or codigoExiste(int(materia))==False:
            print('Ingrese un codigo de materia valido y no repetido: ')
            return
        materia=int(materia)
        materiasCursada.append(materia)
        materia=input('Ingrese otra materia: ')

    alumno=Alumno(legajo, nombre, apellido, materiasCursada)
    listaAlumnos.append(alumno)

    return alumno

def legajoExiste(legajoIngresado):
    for alumno in listaAlumnos:
        if legajoIngresado == alumno.legajo:
            return True
    return False

def listarAlumnos():
    for alumno in listaAlumnos:
        print(alumno)

def obtenerMateriasXLegajo(legajoAlumno):
    for alumno in listaAlumnos:
        if alumno.legajo == legajoAlumno:
            return alumno.materias
