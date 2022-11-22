from alumno import *
from listaMaterias import agregarAlumnoAMateria, codigoExiste, obtenerMateria, listaMaterias
from listaEnlazada import *

listaAlumnos = []

def agregarAlumno():
    legajo=input('Por favor ingrese el numero de legajo: ')
    while legajo.isnumeric() == False or legajoExiste(int(legajo)) == True:
        print('Ingrese un numero de legajo valido')

    legajo=int(legajo)

    nombre=input('Ingrese el nombre: ')

    apellido=input('Ingrese el apellido: ')

    materiasCursada=ListaEnlazada()
    materia=input('Por favor ingrese las materias que esta cursando. Presione enter cuando haya finalizado: ')

    while materia != '':
        if materia.isnumeric() == False or codigoExiste(int(materia))==False:
            print('Ingrese un codigo de materia valido y no repetido: ')
            return
        materia=int(materia)
        materiasCursada.agregar(materia)
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

def agregarMateriaAAlumno(legajo, codigoMateria):
    for alumno in listaAlumnos:
        if alumno.legajo == legajo:
            alumno.materias.agregar(codigoMateria)

def eliminarMateriaDeAlumno(legajo, codigoMateria):
    for alumno in listaAlumnos:
        if alumno.legajo == legajo:
            alumno.materias.eliminar(codigoMateria)

def agregarAyudante(legajoAlumno, codigoMateria):
    for alumno in listaAlumnos:
        if alumno.legajo == legajoAlumno:
            alumno.ayudanteEn.agregar(codigoMateria)

def eliminarAyudante(legajoAlumno, codigoMateria):
    for alumno in listaAlumnos:
        if alumno.legajo == legajoAlumno:
            alumno.ayudanteEn.eliminar(codigoMateria)

def visualizarAyudantias(legajoAlumno):
    for alumno in listaAlumnos:
        if alumno.legajo == legajoAlumno:
            nodoActual = alumno.ayudanteEn.nodoInicial
            if nodoActual == None:
                print('El alumno no es ayudante en ninguna materia')
            while nodoActual != None:
                codigoMateria = nodoActual.dato
                materia = obtenerMateria(codigoMateria)
                print(materia)
                nodoActual = nodoActual.prox

def visualizarMateriasCursadas(legajoAlumno):
    for alumno in listaAlumnos:
        if alumno.legajo == legajoAlumno:
            nodoActual = alumno.materias.nodoInicial
            while nodoActual != None:
                codigoMateria = nodoActual.dato
                materia = obtenerMateria(codigoMateria)
                print(materia)  
                nodoActual = nodoActual.prox

def agregarNota(legajoAlumno, codigoMateria, nota):
    for alumno in listaAlumnos:
        if alumno.legajo == legajoAlumno:
            alumno.notas.append(NotaMateria(nota, codigoMateria))
    
    for materia in listaMaterias:
        if materia.codigo == codigoMateria:
            materia.notas.append(NotaAlumno(nota, legajoAlumno))

def promedioAlumno(legajo):
    cantidadNotas = 0
    sumaNotas = 0
    for alumno in listaAlumnos:
        if alumno.legajo == legajo:
            for nota in alumno.notas:
                cantidadNotas += 1
                sumaNotas += nota.nota
    if cantidadNotas > 0:
        promedio = sumaNotas / cantidadNotas
        print('El promedio del alumno {} es {}'.format(legajo, promedio))
    else:
        print('El alumno aun no tiene notas') 

materias = ListaEnlazada()
materias.agregar(1)
alumno1 = Alumno(2, 'Azul', 'Makk', materias)
listaAlumnos.append(alumno1)

agregarAlumnoAMateria(2, 1)


# nodoActual = lista.nodoInicial
# while nodoActual != None:
#     # Codigo



#     nodoActual = nodoActual.prox