from cliente import Cliente
from compras import Compra
from pagos import Pago

def crear_cliente():
    print("Ingresar datos del cliente")
    nombre = input("Nombre: ")
    dni = int(input("Dni: "))
    
    edad = int(input("Edad: "))
    while edad < 18:
        print("No es mayor de edad. Ingrese de nuevo")
        edad = int(input("Edad: "))
    
    telefono = input("Telefono: ")
    
    return Cliente(nombre, dni, edad, telefono)


def iniciar_sesion():
    metodo_inicio = input("Elija el método de inicio\n1. DNI:\n2. Número de cliente\n")
    
    while metodo_inicio not in ['1', '2']:
        print("Solo puede ingresar 1 o 2")
        metodo_inicio = input("Elija el método de inicio\n1. DNI:\n2. Número de cliente\n")
    
    if metodo_inicio == '1':
        
        dni = int(input("Ingrese el dni: "))
        dni_hallado = False
        
        while not dni_hallado:
            for persona in Cliente.lista_clientes:
                print(persona.dni)
                if dni == persona.dni:
                    cliente = persona
                    dni_hallado = True
                    print(f"Bienvenido {persona.nombre}")
                    break
            
            print("Dni no hallado en la base de datos")
            dni = int(input("Ingrese el dni: "))
    
    else:
        
        num_cliente = input("Ingrese el número de cliente: ")
        num_cliente_hallado = False
        
        while not num_cliente_hallado:
           
            for persona in Cliente.lista_clientes:
                if num_cliente == persona.num_cliente:
                    cliente = persona
                    num_cliente_hallado = True
                    print(f"Bienvenido {persona.nombre}")
                    break
            
            print("Número de cliente no hallado en la base de datos")
            num_cliente = input("Ingrese el número de cliente: ")
    
    return cliente


def bienvenida():
    print("¡Bienvenido al Parque de la Costa!")
    existe_usuario = input("¿Ya tiene usuario?\n1. SI\n2. NO\n")
    
    if existe_usuario == '1':
        cliente = iniciar_sesion()
    
    else:
        cliente = crear_cliente()
    
    opciones = input("¿Qué desea hacer?\n1. Modificar tus datos\n2. Ver tus últimas 3 compras\n3. Comprar boletos")
    
    while opciones not in ['1', '2', '3']:
        print("Solo opciones entre 1 y 3")
        opciones = input("¿Qué desea hacer?\n1. Modificar tus datos\n2. Ver tus últimas 3 compras\n3. Comprar boletos")
    
    if opciones == '1':
        cliente.modificar()
    
    elif opciones == '2':
        compras_cliente = []
        
        for compra_cliente in Compra.lista_compras:
            if cliente.num_cliente == compra_cliente.codigo_compra.split()[0]:
                compras_cliente.append(compra_cliente)
        
        for i in range(-1, -4, -1):
            print(compras_cliente[i])
    
    else:
        seguir = '1'
        
        while seguir == '1':
            fecha_uso = input("Fecha para su uso: ")
            cant_adultos = int(input("Cantidad de adultos: "))
            cant_menores = int(input("Cantidad de menores: "))
            cant_mayores = int(input("Cantidad de mayores: "))
            
            parque = input("¿A cuál parque quiere ir?\n1. Acuático\n2. Esportland\n3. Aventura\n4. Multipase")
            while parque not in ['1', '2', '3', '4']:
                print("Solo válidos números del 1 al 4")
                parque = input("¿A cuál parque quiere ir?\n1. Acuático\n2. Esportland\n3. Aventura\n4. Multipase")
            
            compra = Compra(fecha_uso, cant_adultos, cant_menores, cant_mayores, cliente, parque)
            
            pagar_o_no = input("¿Quiere pagar?\n1. SI\n2. NO\n")
            while pagar_o_no not in ['1', '2']:
                print("Solo válidos los números 1 y 2")
                pagar_o_no = input("¿Quiere pagar?\n1. SI\n2. NO\n")
            
            if pagar_o_no == '1':
                pago = Pago(compra)
                pago.pagar()
        
            seguir = input("¿Quiere seguir comprando?\n1. SI\n2. NO\n")
        
        bienvenida()


cliente1 = Cliente('Jorge', 40404040, 22, '1514714892')
bienvenida()