from profesor import *

listaProfesores = []

def agregarProfesor():
    legajo=input('Por favor ingrese el numero de legajo: ')
    while legajo.isnumeric() == False or legajoExiste(int(legajo))==True:
        print('Ingrese un numero de legajo valido')
        legajo=input('Intentelo de nuevo: ')
        return
    legajo=int(legajo)

    nombre=input('Ingrese el nombre: ')

    apellido=input('Ingrese el apellido: ')

    profesor=Profesor(legajo, nombre, apellido)
    listaProfesores.append(profesor)

    return profesor

def legajoExiste(legajoIngresado):
    for profesor in listaProfesores:
        if legajoIngresado == profesor.legajo:
            return True
    return False

def obtenerProfesorXLegajo(legajoProfesor):
    for profesor in listaProfesores:
        if legajoProfesor == profesor.legajo:
            return profesor.nombre+' '+profesor.apellido

def agregarMateriaAProfesor(profesorLegajo, codigoMateria):
    for profesor in listaProfesores:
        if profesorLegajo == profesor.legajo:
            profesor.agregarMateria(codigoMateria)

def listarProfesores():
    for profesor in listaProfesores:
        print(profesor)

def obtenerMateriasXProfesor(legajoProfesor):
    for profesor in listaProfesores:
        if legajoProfesor == profesor.legajo:
            return profesor.materias