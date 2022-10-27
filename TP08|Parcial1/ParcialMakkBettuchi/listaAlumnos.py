
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
        #listacreditos = CreditosPorAlumno(materiasCursada)
        #while sumaCreditosPorAlumno(listacreditos) < 24:
        materia=input('Ingrese otra materia: ')

    materiasAyudante = []
    materiaAyudantia = input('Por favor ingresar las materias en la que es ayudante: ')

    while materiaAyudantia != '':
        if materiaAyudantia.isnumeric() == False or codigoExiste(int(materiaAyudantia))==False:
            print('Ingrese un codigo de materia valido y no repetido: ')
            return
        materiaAyudantia=int(materiaAyudantia)
        materiasAyudante.append(materiaAyudantia)
        materiaAyudantia=input('Ingrese otra materia: ')
    
    alumno=Alumno(legajo, nombre, apellido, materiasCursada, materiasAyudante)
    listaAlumnos.append(alumno)

    return alumno

def codigoExiste(legajoIngresado):
    for materia in listaMaterias:
        if legajoIngresado == materia.codigo:
            return True
    return False

def quitarAlumno(legajoIngresado):
    for alumno in listaAlumnos:
        if legajoIngresado == alumno.legajo:
            listaAlumnos.pop(alumno)

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

def obtenerMateriasXAlumno(legajoAlumno):
    for alumno in listaAlumnos:
        if legajoAlumno == alumno.legajo:
            return alumno.materias

def cargarNotasDeUnAlumno(legajoAlumno):
    nota = input('Ingrese la nota obtenida por alumno: ')
    if nota > 10 or nota < 0 or nota.isnumeric()==False:
        print('Ingrese una nota valida por favor')
        nota=input('Intentelo nuevamente: ')
    nota=int(nota)
    
    for alumno in listaAlumnos:
        if legajoAlumno == alumno.legajo:
            alumno.notas.append(nota)

def obtenerPromedioDeAlumno(legajoIngresado):
    for alumno in listaAlumnos:
        if legajoIngresado == alumno.legajo:
            nota=sum(alumno.notas)/len(alumno.notas)
    return 'El promedio del alumno es de {}'.format(nota)

def obtenerAyudantesXProfesor(materias): #Recibe una lista
    ayudantesDeProfesor=[]
    for materia in materias:
        for alumno in listaAlumnos:
            if alumno.materia == materia.codigo:
                ayudantesDeProfesor.append(alumno)
    return ayudantesDeProfesor

# def sumaCreditosPorAlumno(listacreditos):
#     sumaCreditos = 0
#     for creditos in listacreditos:
#         sumaCreditos += creditos
#     return sumaCreditos
# def CreditosPorAlumno(materiasCursada):
#     listaCreditos = []
#     for materias in materiasCursada:     
#         for materia in listaMaterias:       
#             if materia.codigo == materias:
#                 listaCreditos.append(materia.creditos)
#     return listaCreditos