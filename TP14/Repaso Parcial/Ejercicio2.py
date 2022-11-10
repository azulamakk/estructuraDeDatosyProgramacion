# Escriba una función en Python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
# Cada alumno puede tener distinta cantidad de notas.La información de los alumnos debe guardarse en un diccionario cuyas 
# claves serán los nombres y los valores serán listas con las notas de cada alumno, las notas de los alumnos se 
# pedirán hasta que la nota introducida sea negativa.En el programa principal se pedirá el número de alumnos que vamos a introducir y
# mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos

listaAlumnos=[]

class Alumno():
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def __str__(self):
        return str((self.nombre, self.notas))

diccionario = dict()

def cargarManualmente():
    nombre = input('Ingrese el nombre')
    notas = []
    nota = int(input('Ingrese notas. Cuando desee finalizar ingrese un numero negativo'))
    while nota > 0: 
        notas.append(nota)
        nota = int(input('Ingrese otra nota'))
    return nombre, notas

def guardarClaseDiccionario(diccionario, nombre, notas):
    alumno = Alumno(nombre, notas)
    diccionario[alumno.nombre]=alumno.notas
    return diccionario