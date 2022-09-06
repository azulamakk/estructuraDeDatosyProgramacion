
from Ejercicio3 import persona

class persona:
    def __init__(self):
        self.nombre=input('Ingrese el nombre: ')
        self.edad=input("Ingrese la edad: ")
        self.DNI=input("Ingrese el DNI: ")
        self.sexo=input("Ingrese el sexo")
        self.mayorEdad=self.mayorDeEdad()

    def mayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    
ninfa=persona()
azul=persona()
agustin=persona()
print(ninfa)
print(azul)
print(agustin)