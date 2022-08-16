class Cliente:
    lista_clientes = []
    
    def __init__(self, nombre: str, dni: int, edad: int, telefono: str):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.telefono = telefono
        self.num_cliente = self.nombre[0] + str(dni)
        self.lista_clientes.append(self)
    
    def __str__(self):
        cadena = 'Nombre: ' + self.nombre + '\nDni: ' + str(self.dni) + '\nEdad: ' + str(self.edad) + '\nTelefono: ' + self.telefono + '\nNúmero de Cliente: ' + self.num_cliente
        return cadena
    
    def modificar(self):
        atributo_a_cambiar = input("¿Qué desea cambiar de su usuario?\n1. Nombre\n2. Dni\n3. Edad\n4. Telefono\n5. Nada más\n")
        nums_posibles = ['1', '2', '3', '4', '5']
        
        while atributo_a_cambiar not in nums_posibles:
            print("Solo números del 1 al 5")
            atributo_a_cambiar = input("¿Qué desea cambiar de su usuario?\n1. Nombre\n2. Dni\n3. Edad\n4. Telefono\n5. Nada más\n")
        
        while atributo_a_cambiar != '5':
            if atributo_a_cambiar == '1':
                self.nombre = input("Ingrese el nuevo nombre: ")
            elif atributo_a_cambiar == '2':
                self.dni = int(input("Ingrese el nuevo dni: "))
            elif atributo_a_cambiar == '3':
                self.edad = int(input("Ingrese la nueva edad: "))
            elif atributo_a_cambiar == '4':
                self.telefono = input("Ingrese el nuevo telefono: ")
            else:
                return
            
            atributo_a_cambiar = input("¿Qué desea cambiar de su usuario?\n1. Nombre\n2. Dni\n3. Edad\n4. Telefono\n5. Nada más\n")
            
            while atributo_a_cambiar not in nums_posibles:
                print("Solo números del 1 al 5")
                atributo_a_cambiar = input("¿Qué desea cambiar de su usuario?\n1. Nombre\n2. Dni\n3. Edad\n4. Telefono\n5. Nada más\n")

if __name__ == '__main__':
    cliente1 = Cliente('Jorge', 40404040, 22, '1514714892')
    print(cliente1)
    cliente1.modificar()
    print(cliente1)