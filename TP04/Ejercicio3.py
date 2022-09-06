from random import randint


class persona():
    def __init__(self, nombre='', edad=0, DNI=randint(0,99999999), sexo=''):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
        self.sexo=sexo
        if sexo != "H" and sexo != "M" and sexo != '':
            self.sexo=input('Ingrese nuevamente el sexo. -Opciones válidas: M y H-: ')
    
    def mayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    
    def __str__(self):
        return ('''
        La persona creada recibe el nombre de {}
        Su edad es de {} años. Es mayor de edad? {}
        Su DNI es {} y su sexo es {}
        '''.format(self.nombre, str(self.edad), str(self.mayorDeEdad()), str(self.DNI), self.sexo))

azul=persona()
print(azul)