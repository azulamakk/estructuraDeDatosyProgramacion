from alumnos import *
from profesores import *
from materias import *
import six

#### Alumnos ####

juan = Alumnos()
sofia = Alumnos()


listaAlumnosUniversidad = Alumnos.listaDeAlumnos()
detalleAlumnosUniversidad = Alumnos.mostrarAlumnos(Alumnos)
print('Lista de Alumnos de la universidad', listaAlumnosUniversidad)
print('Detalle de los Alumnos', detalleAlumnosUniversidad)

#### Profesores ####
lucia = Profesores()
maria = Profesores()
detalleProfesores = Profesores.mostrarProfesores(Profesores)
print('Detalle de los profesores', detalleProfesores)


#### Conocer los profesores de un determinado Alumno ####
def profesoresDeAlumno(legajoAlumno):
    profesoresDelAlumno = []
    if legajoAlumno in Alumnos.listaLegajos:
        materiasAlumno = detalleAlumnosUniversidad.get(legajoAlumno)    ##cambiar sin dict    
        for materia in materiasAlumno:
            for nombreProfesor, materiasProfesor in six.iteritems(detalleProfesores):
                if materia in materiasProfesor:
                    profesoresDelAlumno.append(nombreProfesor)
    else:
        print('Este legajo no pertenece a un alumno de esta Universidad')
    return profesoresDelAlumno

        
profesoresDeAlumno = profesoresDeAlumno(123456)
print('Los profesores del alumno: ', profesoresDeAlumno)

#### Materias que dicta un Profesor ####
def materiasQueDictaUnProfesor(nombreProfesor):
    materiasDelProfesor = Profesores.mostrarProfesores(Profesores).get(nombreProfesor)
    return materiasDelProfesor
    
materiasProfesor = materiasQueDictaUnProfesor('Lucia')


# Usted es el nuevo CEO del ITBA y encontró inconsistencias en la base de datos, 
# en la cual existenredundancias y decide renovar la base de datos del SGA, 
# para lo cual ha llamado a varias empresas dedesarrollo de software entre ellas incluida la suya, 
# para que le presenten diferentes diseños y entre ellos poder escoger cual sería el nuevo diseño 
# del programa del SGA.Entre los requerimientos que pide están:
# - Quiero un Código que genere una lista de alumnos (que verifique si se repite el legajo o no).
# - Que haya una lista de profesores.
# - Que haya una lista de materias (solo acepta un profesor titular).
# - Deben existir métodos o funciones que nos permitan obtener la lista de profesores de un alumno.
# - Método que permita determinar que materias dicta un profesor.
# Una vez expuestos los diseños de las diferentes empresas,se escogerá un solo diseño, 
# el cual deberá serimplementado por las empresas