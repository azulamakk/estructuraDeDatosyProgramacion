
from operator import le
from listaAlumnos import *
from listaProfesores import *
from listaMaterias import *

from graficaAlumnosXMateria import *
from graficaCantProfesores import *

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
9. Ver Materias de un Estudiante
10. Visualizacion Cantidad de Alumnos por Materia
11. Visualizacion Cantidad de Materias dictadas por un profesor
12. Ver Ayudantes de un profesor
13. Quitar alumnos
14. Quitar profesores
15. Cargar notas de una materia
16. Obtener Promedio de una Materia
17. Cargar notas de un alumno
18. Obtener Promedio de un Alumno
19. Finalizar
Ingrese que accion desea realizar: ''')

while opcionIngresada.isnumeric() == False:
    print('Ingrese un numero de legajo valido')
    opcionIngresada=input('Intente nuevamente ingresar una opcion: ')
opcionIngresada=int(opcionIngresada)

while opcionIngresada != 19:
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
        for materias in alumno.ayudantia:
            agregarAyudanteAMateria(alumno.legajo, materias)
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
            legajoIngresado=input('Intente nuevamente ingresar un legajo: ')
        legajoIngresado=int(legajoIngresado)
        print(obtenerMateriasXProfesor(legajoIngresado))
    elif opcionIngresada == 9:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar un legajo: ')
        legajoIngresado=int(legajoIngresado)
        print(obtenerMateriasXAlumno(legajoIngresado))
    elif opcionIngresada == 10:
        graficaAlumnosXMateria()
    elif opcionIngresada == 11:
        graficaCantMaterias()
    elif opcionIngresada ==12:
        legajoIngresado=input('Ingrese el legajo del profesor: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        materias=obtenerMateriasXProfesor(legajoIngresado)
        obtenerAyudantesXProfesor(materias)
    elif opcionIngresada == 13:
        quitarAlumno(legajoIngresado)
    elif opcionIngresada == 14:
        legajoIngresado=input('Ingrese el legajo del profesor: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        quitarProfesores(legajoIngresado)
    elif opcionIngresada == 15:
        codigoMateriaIngresado=input('Ingrese el codigo de materia: ')
        while codigoMateriaIngresado.isnumeric() == False or codigoExiste(codigoMateriaIngresado)==False:
            print('Ingrese una nota valida')
            codigoMateriaIngresado=input('Intente nuevamente ingresar una nota: ')
        codigoMateriaIngresado=int(codigoMateriaIngresado)
        cargarNotasDeUnaMateria(codigoMateriaIngresado)
    elif opcionIngresada == 16:
        codigoMateriaIngresado=input('Ingrese el codigo de materia: ')
        while codigoMateriaIngresado.isnumeric() == False or codigoExiste(codigoMateriaIngresado)==False:
            print('Ingrese una nota valida')
            codigoMateriaIngresado=input('Intente nuevamente ingresar una nota: ')
        codigoMateriaIngresado=int(codigoMateriaIngresado)
        obtenerPromedioDeMateria(codigoMateriaIngresado)
    elif opcionIngresada==17:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        cargarNotasDeUnAlumno(legajoIngresado)
    elif opcionIngresada == 18:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        obtenerPromedioDeAlumno(legajoIngresado)

    opcionIngresada=input('Ingrese una nueva accion: ')

    while opcionIngresada.isnumeric() == False:
        print('Ingrese un numero de legajo valido')
        opcionIngresada=input('Intente nuevamente ingresar una opcion: ')
    opcionIngresada=int(opcionIngresada)

