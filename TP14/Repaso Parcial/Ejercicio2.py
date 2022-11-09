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

def guardarClaseDiccionario(nombre, notas):
    alumno = Alumno(nombre, notas)
    diccionario.update(alumno.nombre, alumno.notas)
    return diccionario

print(guardarClaseDiccionario('Azul', [10, 10, 10]))
# guardarClaseDiccionario('Tatu', [10, 20])

# print(diccionario)