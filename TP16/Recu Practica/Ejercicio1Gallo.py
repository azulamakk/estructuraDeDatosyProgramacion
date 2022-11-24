
class Libro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.resenas = []
        self.sumaCalificaciones = 0
        self.cantCalificaciones = 0
        self.promedio = 0

    def agregarResena(self, resena):
        self.resenas.append(resena)
        self.sumaCalificaciones += resena.calificacion
        self.cantCalificaciones += 1
        self.promedio = self.sumaCalificaciones / self.cantCalificaciones
    
    def __str__(self):
        return '''
            Titulo: {}
            Autor: {}
            ISBN: {}
            Calificacion: {}
        '''.format(self.titulo, self.autor, self.ISBN, self.promedio)
    
class Resena:
    def __init__(self, ISBN, comentador, resena, calificacion):
        self.comentador = comentador
        self.resena = resena
        self.calificacion = calificacion
        self.ISBN = ISBN
        
libros = [
    Libro("El principito", "Antoine de Saint-Exupéry", 123456789), 
    Libro("El señor de los anillos", "J.R.R. Tolkien", 987654321),
    Libro("El hobbit", "J.R.R. Tolkien", 123456780),
    Libro("El alquimista", "Paulo Coelho", 123456781),
    Libro("El diario de Ana Frank", "Ana Frank", 123456782),
    Libro("El código Da Vinci", "Dan Brown", 123456783),
    Libro("El arte de la guerra", "Sun Tzu", 123456784),
    Libro("El perfume", "Patrick Süskind", 123456785),
    Libro("El nombre de la rosa", "Umberto Eco", 123456786)    
]
def agregarResena(resena):
    for libro in libros:
        if libro.ISBN == resena.ISBN:
            libro.agregarResena(resena)

# Cargar resenas en libros
agregarResena(Resena(123456789, "Juan", "Muy bueno", 5))
agregarResena(Resena(123456789, "Pedro", "Muy bueno", 5))
agregarResena(Resena(123456789, "Maria", "Muy bueno", 5))
agregarResena(Resena(987654321, "Jose", "Muy bueno", 5))
agregarResena(Resena(987654321, "Maria", "Malo", 1.5))
agregarResena(Resena(987654321, "Jose", "Malo", 1.5))

print('''
1. Visualizar libros disponibles
2. Mostrar libros mejor calificados
''')
opcionIngresada=int(input('Ingrese una opcion: '))
def menuPrincial(opcion):
    if opcion == 1:
        calificacionDada = float(input('Ingrese la calificacion que debe superar'))
        mejores = listadoDisponibles(calificacionDada)
        for libro in mejores:
            print(libro)
    elif opcion == 2:
        cantidad = int(input('Ingrese la cantidad de libros a mostrar: '))
        aImprimir = mostrarMejoresCalificados(cantidad)
        for libro in aImprimir:
            print(libro)


def listadoDisponibles(calificacionMinima):
    libros.sort(key=lambda libro: libro.promedio, reverse=True)
    superanCalificacion = []
    for libro in libros:
        promedio = libro.promedio
        if promedio > calificacionMinima:
            superanCalificacion.append(libro)
    return superanCalificacion

def mostrarMejoresCalificados(cantidad):
    libros.sort(key=lambda libro: libro.promedio, reverse=True)
    topCantidad = []
    for i in range(cantidad):
        topCantidad.append(libros[i])
    return topCantidad
        
menuPrincial(opcionIngresada)

# class Nodo:
#     def __init__(self, dato, prox = None):
#         self.dato = dato
#         self.prox = prox

# class ListaEnlazadaOrdenada:
#     def __init__(self):
#         self.nodoInicial = None
#         self.longitud = 0

#     def agregar(self, dato):
#         nodo = Nodo(dato)

#         if self.esta_vacia():
#             self.nodoInicial = nodo
#             self.longitud = 1
#             return True

#         if dato > self.nodoInicial.dato:
#             nodo.prox = self.nodoInicial
#             self.nodoInicial = nodo
#             self.longitud += 1
#             return True            

        
#         nodoActual = self.nodoInicial
#         while nodoActual.prox != None and nodoActual.prox.dato > dato:
#             if nodoActual.dato == dato:
#                 return False # No meter repetidos

#             nodoActual = nodoActual.prox

#         # dato > nodoActual.prox.dato && dato < nodoActual.dato
#         nodo.prox = nodoActual.prox
#         nodoActual.prox = nodo
#         self.longitud += 1
#         return True
    
#     def eliminar(self, dato):
#         if self.esta_vacia():
#             return

#         if self.nodoInicial.dato == dato:
#             self.nodoInicial = self.nodoInicial.prox
#             self.longitud -= 1
        
#         if self.longitud <= 1:
#             return

#         nodoPrevio = self.nodoInicial
#         nodoActual = nodoPrevio.prox
#         while nodoActual != None:
#             if nodoActual.dato == dato:
#                 nodoPrevio.prox = nodoActual.prox
#                 self.longitud -= 1

#             nodoPrevio = nodoActual
#             nodoActual = nodoActual.prox

#     def tiene_elemento(self, dato):
#         nodoActual = self.nodoInicial
#         while nodoActual != None:
#             if nodoActual.dato == dato:
#                 return True

#             nodoActual = nodoActual.prox

#         return False

#     def esta_vacia(self):
#         return self.longitud == 0

#     def __str__(self):
#         toReturn = ''
#         nodoActual = self.nodoInicial
#         while nodoActual != None:
#             toReturn += str(nodoActual.dato) + ', '
#             nodoActual = nodoActual.prox
#         return toReturn



# listaOrdenada = ListaEnlazadaOrdenada()
# listaOrdenada.agregar(5)
# listaOrdenada.agregar(3)
# listaOrdenada.agregar(1)
# listaOrdenada.agregar(2)
# listaOrdenada.agregar(4)
# listaOrdenada.agregar(6)

# print(listaOrdenada)