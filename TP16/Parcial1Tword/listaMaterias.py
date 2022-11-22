from materia import *
from listaProfesores import *
from listaEnlazada import *

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
        print('Ingrese un legajo valido')
        profesor=input('Por favor ingrese el legajo del profesor: ')
    profesor=int(profesor)

    creditos=input('Ingrese la cantidad de creditos: ')
    
    while creditos.isnumeric() == False or int(creditos) <= 0:# or int(creditos) > 6:
        creditos = input('Cant de creditos invalida. Creditos: ')
    creditos = int(creditos)

    profesores = ListaEnlazada()
    profesores.agregar(profesor)
    materia=Materia(codigo, nombre, creditos, profesores)

    listaMaterias.append(materia)

    return materia

def obtenerMateria(codigoMateria):
    for materia in listaMaterias:
        if materia.codigo == codigoMateria:
            return materia

    return None
 
def codigoExiste(legajoIngresado):
    for materia in listaMaterias:
        if legajoIngresado == materia.codigo:
            return True
    return False

def listarMaterias():
    for materia in listaMaterias:
        print(materia)

def profesoresXMateria(codigoMateria):
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            return materia.profesores

def agregarAlumnoAMateria(legajo, codigoMateria):
    from listaAlumnos import obtenerMateriasXLegajo, agregarMateriaAAlumno

    materiasCursadas = obtenerMateriasXLegajo(legajo)
    creditosTotales = 0
    for materia in listaMaterias:
        if materiasCursadas.tiene_elemento(codigoMateria):
            creditosTotales += materia.creditos

    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            if creditosTotales + materia.creditos <= 24:
                materia.alumnos.agregar(legajo)
                agregarMateriaAAlumno(legajo, codigoMateria)
            else:
                print('No puede cursar mas de 24 creditos')
            

def eliminarAlumnoDeMateria(legajo, codigoMateria):
    from listaAlumnos import eliminarMateriaDeAlumno

    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            materia.alumnos.eliminar(legajo)
            eliminarMateriaDeAlumno(legajo, codigoMateria)


def agregarProfesorAMateria(legajo, codigoMateria):
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            materia.profesores.agregar(legajo)
    
    for profesor in listaProfesores:
        if legajo == profesor.legajo:
            profesor.materias.agregar(codigoMateria)

def eliminarProfesorDeMateria(legajo, codigoMateria):
    pudoEliminar = False
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            if materia.profesores.longitud > 1:
                pudoEliminar = True
                materia.profesores.eliminar(legajo)
            else:
                print('No se pudo quitar profesor. Tiene que haber al menos 1')
    
    if pudoEliminar:
        for profesor in listaProfesores:
            if legajo == profesor.legajo:
                profesor.materias.eliminar(codigoMateria)

    
def promedioMateria(codigo):
    cantidadNotas = 0
    sumaNotas = 0
    for materia in listaMaterias:
        if materia.codigo == codigo:
            for nota in materia.notas:
                cantidadNotas += 1
                sumaNotas += nota.nota
    if cantidadNotas > 0:
        promedio = sumaNotas / cantidadNotas
        print('El promedio de la materia {} es {}'.format(codigo, promedio))
    else:
        print('La materia aun no tiene notas') 

profesorMateria1 = ListaEnlazada()
profesorMateria1.agregar(1)
materia1 = Materia(1, 'EDD', 6, profesorMateria1)

listaMaterias.append(materia1)


