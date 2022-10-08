from materia import *
from listaProfesores import *
from listaAlumnos import *

listaMaterias = []

def agregarMateria():
    codigo=input('Por favor ingrese el codigo de materia: ')
    while codigo.isnumeric() == False or codigoExiste(int(codigo))==True:
        print('Ingrese un codigo de materia valido')
        codigo=input('Por favor ingrese el codigo de materia: ')
    codigo=int(codigo)

    nombre=input('Ingrese el nombre: ')

    creditos=input("Inserte la cantidad de creditos de la materias (entre 1 y 6): ")
    while creditos.isnumeric() == False:
        print('Ingrese una cantidad de creditos valida')
        creditos=input('Por favor ingrese la cantidad de creditos: ')
        if creditos<1 or creditos>6:
            creditos=input('Por favor ingrese la cantidad de creditos en el rango indicado: ')
            return
        creditos=int(creditos)

    profesor=input('Ingrese el legajo del profesor valido y no repetido. Presione enter cuando haya finalizado: ')

    while profesor != '':
        if profesor.isnumeric() == False or legajoExiste(int(profesor))==False:
            print('Legajo invalido. Intente nuevamente.')
            return
        profesor=int(profesor)
        profesor=input('Por favor ingrese otro profesor en caso de haberlo: ')

    materia=Materia(codigo, nombre, creditos)
    listaMaterias.append(materia)

    return materia


# def legajoExiste(legajoIngresado):
#     for profesor in listaProfesores:
#         if legajoIngresado == profesor.legajo:
#             return True
#     return False

def codigoExiste(legajoIngresado):
    for materia in listaMaterias:
        if legajoIngresado == materia.codigo:
            return True
    return False

def listarMaterias():
    for materia in listaMaterias:
        print(materia)

def obtenerPromedioDeMateria(codigoIngresado):
    for materia in listaMaterias:
        if codigoIngresado == materia.codigo:
            nota=sum(materia.notas)/len(materia.notas)
    return 'El promedio de la materia es de {}'.format(nota)

def profesorXMateria(codigoMateria):
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            return materia.profesor

def agregarAlumnoAMateria(legajo, codigoMateria):
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            materia.alumnos.append(legajo)

def agregarAyudanteAMateria(legajo, codigoMateria):
    for materia in listaMaterias:
        if codigoMateria == materia.codigo:
            materia.alumnos.append(legajo)

def cargarNotasDeUnaMateria(codigoMateria):
    nota = input('Ingrese la nota obtenida por alumno: ')
    if nota > 10 or nota < 0 or nota.isnumeric()==False:
        print('Ingrese una nota valida por favor')
        nota=input('Intentelo nuevamente: ')
    nota=int(nota)

    for materia in listaMaterias:
        if materia.codigo == codigoMateria:
            materia.notas.append(nota)
    








