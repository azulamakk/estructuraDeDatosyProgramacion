from claseTeorica1208 import persona

class empleado(persona):
    def __init__(self, nombre, ident, edad, sexo, cargo, salario, legajo):
        persona.__init__(self, nombre, ident, edad, sexo)
        self.cargo=cargo
        self.salario=salario
        self.legajo=legajo

    def __str__(self):
        return "Me llamo {} y el cargo es {}".format(self.nombre, self.cargo)

class manager(empleado):
    def __init__(self, nombre, ident, edad, sexo, cargo, salario, legajo):
        empleado.__init__(self, nombre, ident, edad,sexo,cargo, salario,legajo)

if __name__ == "main":
    azul=empleado("azul", 123456, 20, "F", "Gerente", 500000, 1121)   
    print(azul)
    azul.edad=21
    print(azul)
    print(azul.mayorEdad())

pedro=persona("Pedro", 654321, "M")
print(pedro)
print(pedro.mayorEdad())