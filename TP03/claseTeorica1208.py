# class human():
#     def __init__(self, age=0, sex="?"):
#         self.age = age
#         self.sex = sex
#     def speak(self):
#         print("Hello I am:", self.age, " and ", self.sex)

# man=human()
# woman=human(4)
# print(man)
# man.speak()


# class Myclass:
#     i=12345
#     def f(self):
#         return "hello World"

# x=Myclass()
# print(x.i)
# y=Myclass()
# print(y.i)

# import math

# y=math.pi

class Persona():
    def __init__(self, nombre, ident, edad, sexo):
        self.nombre=nombre
        self.ident=ident
        self.edad=edad
        self.sexo=sexo 
    
    def __str__(self):
        cadena=''
        cadena='La persona llamada {} tiene DNI {}, su edad es {}'.format(self.nombre, self.ident, self.edad)
        return cadena
    
    def mayorEdad(self):
        return self.edad>21
    
azul=Persona("Azul", 123456, 20, "F")
azul.edad=21
print(azul)
print(azul.mayorEdad)