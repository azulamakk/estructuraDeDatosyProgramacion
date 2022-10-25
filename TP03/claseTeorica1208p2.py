from claseTeorica1208 import Persona

class Empleado(Persona):
    def __init__(self, nombre, ident, edad, sexo, cargo, salario, legajo):
        Persona.__init__(self, nombre, ident, edad, sexo)
        self.cargo=cargo
        self.salario=salario
        self.legajo=legajo

    def __str__(self):
        return "Me llamo {} y el cargo es {}".format(self.nombre, self.cargo)

class Manager(Empleado):
    def __init__(self, nombre, ident, edad, sexo, cargo, salario, legajo):
        Empleado.__init__(self, nombre, ident, edad,sexo,cargo, salario,legajo)
        Persona.__init__(self,nombre,ident,edad,sexo)

if __name__ == "main":
    azul=Empleado("azul", 123456, 20, "F", "Gerente", 500000, 1121)   
    print(azul)
    azul.edad=21
    print(azul)
    print(azul.mayorEdad())

pedro=Persona("Pedro", 654321, "M")
print(pedro)
print(pedro.mayorEdad())