
from listaAlumnos import *
from listaProfesores import *
from listaMaterias import *
from graficaMateria import *
from graficaAlumnos import *


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
9. Agregar profesor a materia
10. Quitar profesor de materia
11. Agregar alumno a materia
12. Quitar alumno de materia
13. Agregar alumno como ayudante
14. Quitar alumno como ayudante
15. Ver materias en las cuales un alumno es ayudante
16. Ver materias que cursa un alumno
17. Cargar una nota
18. Ver promedio de un alumno
19. Ver promedio de una materia
20. Graficar alumnos por materia
21. Graficar profesor por cantidad de materias
22. Ver ayudantes de un profesor
23. Salir
Ingrese que accion desea realizar: ''')

while opcionIngresada.isnumeric() == False:
    print('Ingrese un numero de legajo valido')
    opcionIngresada=input('Intente nuevamente ingresar una opcion: ')
opcionIngresada=int(opcionIngresada)

while opcionIngresada != 23:
    if opcionIngresada == 1:
        agregarProfesor()
    elif opcionIngresada == 2:
        listarProfesores()
    elif opcionIngresada == 3:
        materia = agregarMateria() #Agregamos una materia
        print(materia.profesores)
        profesor = materia.profesores.nodoInicial.dato
        agregarMateriaAProfesor(profesor, materia.codigo)
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
            profesores = profesoresXMateria(listadoMateriasXAlumno[i])
            profesorNodo = profesores.nodoInicial
            while profesorNodo != None:
                nombreApellidoProfesor=obtenerProfesorXLegajo(profesorNodo.dato)
                listadoProfesoresXAlumno.append(nombreApellidoProfesor)
                profesorNodo = profesorNodo.prox

        print(listadoProfesoresXAlumno)
    elif opcionIngresada == 8:
        legajoIngresado=input('Ingrese el legajo del profesor: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        print(obtenerMateriasXProfesor(legajoIngresado))
    elif opcionIngresada == 9:
        legajoIngresado=input('Ingrese el legajo del profesor: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        
        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')
        materiaIngresada=int(materiaIngresada)
        agregarProfesorAMateria(legajoIngresado, materiaIngresada)
    elif opcionIngresada == 10:
        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')
        materiaIngresada=int(materiaIngresada)

        legajoIngresado=input('Ingrese el legajo del profesor: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        eliminarProfesorDeMateria(legajoIngresado, materiaIngresada)
    elif opcionIngresada == 11:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        
        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')

        materiaIngresada=int(materiaIngresada)
        agregarAlumnoAMateria(legajoIngresado, materiaIngresada)
    elif opcionIngresada == 12:
        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')
        materiaIngresada=int(materiaIngresada)

        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)
        eliminarAlumnoDeMateria(legajoIngresado, materiaIngresada)
    elif opcionIngresada == 13:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)

        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')
        materiaIngresada=int(materiaIngresada)

        agregarAyudante(legajoIngresado, materiaIngresada)
    elif opcionIngresada == 14:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)

        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')
        materiaIngresada=int(materiaIngresada)

        eliminarAyudante(legajoIngresado, materiaIngresada)
    elif opcionIngresada == 15:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)

        visualizarAyudantias(legajoIngresado)
    elif opcionIngresada == 16:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)

        visualizarMateriasCursadas(legajoIngresado)       
    elif opcionIngresada == 17:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)        

        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')
        materiaIngresada=int(materiaIngresada)
        
        nota=input('Ingrese la nota: ')        
        while nota.isnumeric() == False:
            print('Ingrese una nota')
            nota=input('Intente nuevamente ingresar una opcion: ')
        nota=int(nota)
        agregarNota(legajoIngresado, materiaIngresada, nota)
    elif opcionIngresada == 18:
        legajoIngresado=input('Ingrese el legajo del alumno: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)                
        promedioAlumno(legajoIngresado)
    elif opcionIngresada == 19:
        materiaIngresada=input('Ingrese el codigo de materia: ')        
        while materiaIngresada.isnumeric() == False:
            print('Ingrese un codigo de materia')
            materiaIngresada=input('Intente nuevamente ingresar una opcion: ')
        materiaIngresada=int(materiaIngresada)    
        promedioMateria(materiaIngresada)    
    elif opcionIngresada == 20:       
        graficarAlumnosXMateria()
    elif opcionIngresada == 21: 
        graficarMateriasXProfesor()
    elif opcionIngresada == 22:
        legajoIngresado=input('Ingrese el legajo del profesor: ')
        while legajoIngresado.isnumeric() == False:
            print('Ingrese un numero de legajo valido')
            legajoIngresado=input('Intente nuevamente ingresar una opcion: ')
        legajoIngresado=int(legajoIngresado)                        
        visualizarAyudantesDeProfesor(legajoIngresado)
    elif opcionIngresada == 23:
        exit()
    opcionIngresada=input('Ingrese una nueva accion: ')

    while opcionIngresada.isnumeric() == False:
        print('Ingrese un numero de legajo valido')
        opcionIngresada=input('Intente nuevamente ingresar una opcion: ')
    opcionIngresada=int(opcionIngresada)

