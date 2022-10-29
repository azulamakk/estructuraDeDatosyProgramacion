from materia import *
from listaProfesores import *

listaMaterias = []

def agregarMateria():
    codigo=input('Por favor ingrese el codigo de materia: ')
    while codigo.isnumeric() == False or codigoExiste(int(codigo))==True:
        print('Ingrese un codigo de materia valido')
        codigo=input('Por favor ingrese el codigo de materia: ')
    codigo=int(codigo)

    nombre=input('Ingrese el nombre: ')

    profesor=input('Ingrese el legajo del profesor: ')

    while profesor.isnumeric() == False or legajoExiste(int(profesor))==False:
        print('Ingrese un codigo de materia valido')
        profesor=input('Por favor ingrese el codigo de materia: ')
    profesor=int(profesor)

    materia=Materia(codigo, nombre, profesor)
    listaMaterias.append(materia)

    return materia

def codigoExiste(legajoIngresado):
    for materia in listaMaterias:
        if legajoIngresado == materia.codigo:
            return True
    return False

def listarMaterias():
    for materia in listaMaterias:
        print(materia)

def profesorXMateria(codigoMateria):
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            return materia.profesor

def agregarAlumnoAMateria(legajo, codigoMateria):
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            materia.alumnos.append(legajo)
