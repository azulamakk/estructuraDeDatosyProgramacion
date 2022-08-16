from persona import Persona
from validaciones import *


class Cliente(Persona):
    lista_clientes = []
    
    def __init__(self, nombre: str, dni: int, edad: int, telefono: str):
        super().__init__(nombre, dni, edad, telefono)
        self.num_cliente = self.nombre[0] + str(dni)
        self.lista_clientes.append(self)
    
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nDNI: {self.dni}\nEdad: {self.edad}\nTeléfono: {self.telefono}\nNúmero de cliente: {self.num_cliente}"
    
    
    def modificar(self):
        mensaje = "¿Qué desea cambiar de su usuario?\n1. Nombre\n2. DNI\n3. Edad\n4. Telefono\n5. Nada más\n"
        cambio_atributo = int(input(mensaje))
        cambio_atributo = validacion_por_num(opcion=cambio_atributo, num_opciones=5, mensaje=mensaje)
        
        while cambio_atributo != 5:
            if cambio_atributo == 1:
                self.nombre = input("Ingrese el nuevo nombre: ")
            elif cambio_atributo == 2:
                self.dni = int(input("Ingrese el nuevo DNI: "))
            elif cambio_atributo == 3:
                self.edad = int(input("Ingrese la nueva edad: "))
            elif cambio_atributo == 4:
                self.telefono = input("Ingrese el nuevo telefono: ")
            else:
                return
            
            cambio_atributo = int(input(mensaje))
            cambio_atributo = validacion_por_num(opcion=cambio_atributo, num_opciones=5, mensaje=mensaje)