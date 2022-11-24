#A la empresa de Estructuras de datos la ha contactado la librería LEER NO TE HACE DAÑO, 
# con el fin de buscar un software orientado a objetos que les permita mantener actualizada 
# la informacion de su stock de libros.Una vez terminadas las reuniones con el cliente se decide 
# realizar dos clases, una de ellas es la Clase Autor y la otra la Clase Libro.
# Del Autor es importante tener la informacion: nombre, email y genero (H,M), debe tener presente 
# que por seguridad estos atributos deben ser privados.
# De los libros es importante tener la informacion: nombre del libro, autor 
# (sólo tendra un autor por libro), precio y cantidad de libros disponibles, 
# al igual que para la clase Autor estos datos deben ser privados.


#Se acordó implementar para cada una de las clases:
# • métodos constructores
# • El método que permita visualizar la información de cada objeto
# • Crear 3 objetos libros.
# • Mostrar la cantidad de libros disponibles en toda la librería, debe usar para esto una variable.
# • Mostrar dado el nombre de un autor cuantos libros de los introducidos fueron escritospor él (Método)
# • Mostrar cual es el libro de los introducidos más costoso. (Método)
# • Mostrar la información de cada objeto.
listaAutores=[]
listaLibros=[]

class Autor:
    def __init__(self, nombreAutor:str, email:str, genero:str):
        self.nombreAutor=nombreAutor
        self.email=email
        self.genero=genero
    def __str__(self):
        return ''''
        Nombre: {}
        Email: {}
        Genero: {}
        '''.format(self.nombreAutor, self.email, self.genero)

class Libro():
    def __init__(self, nombreAutor:str, nombreLibro:str, precio:float, cantidadDisponibles:int):
        self.nombreAutor=nombreAutor
        self.nombreLibro=nombreLibro
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        self.precio=self.precio
    def __str__(self):
        return ''''
        Nombre autor: {}
        Titulo: {}
        Precio: {}
        Cantidad disponibles: {}
        '''.format(self.nombreAutor, self.nombreLibro, self.precio, self.cantidadDisponibles)

autor1=Autor('AZUL', 'azulamakk@gmail.com', 'F')

libro1=Libro('AZUL', 'aaaa', 10, 3)
libro2=Libro('NINFA', 'bbbb', 20, 9)
libro3=Libro('AZUL', 'cccc', 30, 5)

listaLibros.append(libro1)
listaLibros.append(libro2)
listaLibros.append(libro3)

def calcularCantidad():
    cantAcumulada=0
    for libro in listaLibros:
        cantAcumulada+=libro.cantidadDisponibles
    return cantAcumulada

def librosXAutor(autor):
    listaLibrosXAutor=[]
    for libro in listaLibros:
        if libro.nombreAutor == autor:
            listaLibrosXAutor.append(libro)
    for libro in listaLibrosXAutor:
        print(libro)
    return listaLibrosXAutor

def cantLibrosXAutor(autor):
    cantLibros=0
    for libro in listaLibros:
        if libro.nombreAutor == autor:
            cantLibros+=1
    return cantLibros

def maxPrecio():
    maxPrecio = 0
    for libro in listaLibros:
        if libro.precio >= maxPrecio:
            maxPrecio=libro.precio
    
    for libro in listaLibros:
        if libro.precio == maxPrecio:
            libroMasCaro = libro
    
    return libroMasCaro

def visualizarLibros():
    for libro in listaLibros:
        print(libro)

librosXAutor('AZUL')
print(maxPrecio())
print(cantLibrosXAutor('AZUL'))
print(calcularCantidad())
visualizarLibros()