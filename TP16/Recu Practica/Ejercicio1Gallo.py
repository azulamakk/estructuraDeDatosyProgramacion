
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
    
    # def calcularPromedio(self):
    #     cantCalificaciones = self.calificaciones.longitud
    #     sumaCalificaciones = 0
    #     for calificacion in self.calificaciones:
    #         sumaCalificaciones += calificacion.dato
    #     promedio = sumaCalificaciones / cantCalificaciones
    #     return promedio
    
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

# Cargar resenas en libros
libros[0].agregarResena(Resena(123456789, "Juan", "Muy bueno", 5))
libros[0].agregarResena(Resena(123456789, "Pedro", "Muy bueno", 5))
libros[0].agregarResena(Resena(123456789, "Maria", "Muy bueno", 5))
libros[1].agregarResena(Resena(987654321, "Jose", "Muy bueno", 5))
libros[1].agregarResena(Resena(987654321, "Maria", "Malo", 1.5))
libros[1].agregarResena(Resena(987654321, "Jose", "Malo", 1.5))

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

