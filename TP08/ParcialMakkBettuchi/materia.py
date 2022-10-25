class Materia:
    def __init__(self, codigo, nombre, creditos):
        self.codigo=codigo
        self.nombre=nombre
        self.creditos=creditos
        self.profesor=[]
        self.alumnos=[]
        self.notas=[]
        self.ayudantes=[]

    def __str__(self):
        print('''
        Codigo: {}
        Nombre: {}
        Creditos: {}
        Profesores: {}
        Alumnos: {}
        Notas: {}
        ''').format(self.codigo, self.nombre, self.creditos, self.profesor, self.alumnos, self.notas)
    