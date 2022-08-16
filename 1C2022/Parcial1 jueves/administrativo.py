from persona import Persona

class Administrativo(Persona):
    lista_admins = []
    
    def __init__(self, nombre: str, dni: int, edad: int, telefono: str, direccion: str):
        super().__init__(nombre, dni, edad, telefono)
        self.direccion = direccion
        self.legajo = self.nombre[0] + str(self.dni)
        self.lista_admins.append(self)
    
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nDNI: {self.dni}\nEdad: {self.edad}\nTeléfono: {self.telefono}\nDirección: {self.direccion}"
    
    def realizar_venta_cliente():
        pass

Administrativo("Pepe", 123456, 40, "123123123", "Sadaw")