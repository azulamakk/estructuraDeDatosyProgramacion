
from listaAlumnos import *
from listaProfesores import *
from listaMaterias import *

#Primero se cargan los profesores, despues las materias y al final los alumnos
opcionIngresada= input('''
1. Cargar Profesor
2. Listar Profesores
3. Cargar Materias
4. Listar Materias
5. Cargar alumno
6. Listar alumnos
7. Ver Profesores de un Alumno
8. Ver Materias de un Profesor
9. Finalizar
Ingrese que accion desea realizar: ''')

while opcionIngresada.isnumeric() == False:
    print('Ingrese un numero de legajo valido')
    opcionIngresada=input('Intente nuevamente ingresar una opcion: ')
opcionIngresada=int(opcionIngresada)

while opcionIngresada != 9:
    if opcionIngresada == 1:
        agregarProfesor()
    elif opcionIngresada == 2:
        listarProfesores()
    elif opcionIngresada == 3:
        materia = agregarMateria() #Agregamos una materia
        agregarMateriaAProfesor(materia.profesor, materia.codigo)
    elif opcionIngresada == 4:
        listarMaterias()
    elif opcionIngresada == 5:
        alumno = agregarAlumno()
        for materia in alumno.materias:
            agregarAlumnoAMateria(alumno.legajo, materia)
    elif opcionIngresada==6:
        listarAlumnos()
    elif opcionIngresada == 7:   
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        listadoMateriasXAlumno = obtenerMateriasXLegajo(legajoIngresado)
        listadoProfesoresXAlumno=[]
        for i in range(len(listadoMateriasXAlumno)):
            nombreApellidoProfesor=obtenerProfesorXLegajo(profesorXMateria(listadoMateriasXAlumno[i]))
            listadoProfesoresXAlumno.append(nombreApellidoProfesor)
        print(listadoProfesoresXAlumno)
    elif opcionIngresada == 8:
        legajoIngresado=input('Ingrese el legajo del profesor: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        print(obtenerMateriasXProfesor(legajoIngresado))

    opcionIngresada=input('Ingrese una nueva accion: ')

    while opcionIngresada.isnumeric() == False:
        print('Ingrese un numero de legajo valido')
        opcionIngresada=input('Intente nuevamente ingresar una opcion: ')
    opcionIngresada=int(opcionIngresada)

