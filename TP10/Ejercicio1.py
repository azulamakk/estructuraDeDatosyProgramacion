# Crear una clase persona sino lo ha hecho, la cual tiene como atributos el nombre (string), un id(int) y laedad(int), 
# a partir de la cual se defina un Conjunto (set) de personas dentro de una función main().Se deben crear 4 personas 
# las cuales se deberán añadir al Conjunto. Una vez añadidas 
# las 4 personas alConjunto se debe visualizar el Conjunto total usando :el método __str__ ( de la clase persona)

class Persona:
    def __init__(self, nombre, id, leaedad):
        self.nombre=str(nombre)
        self.id=int(id)
        self.leaedad=int(leaedad)
    
    def __str__(self, conjunto):
        return conjunto

conjunto={}
persona1=Persona('aaa', 1111, 20)
persona2=Persona('bbb', 2222, 20)
persona3=Persona('ccc', 3333, 20)
persona4=Persona('ddd', 4444, 20)
conjunto.update(persona1)
conjunto.update(persona2)
conjunto.update(persona3)
conjunto.update(persona4)

if __name__=='__main__':
    persona=Persona()

