from cliente import Cliente
from administrativo import Administrativo
from compras import Compra
from pagos import Pago
from validaciones import *
import pandas as pd
from datetime import datetime


def crear_cliente():
    print("Ingresar datos del cliente")
    nombre = input("Nombre: ")
    nombre = validacion_tipo(nombre, str)
    
    dni = input("DNI: ")
    dni = validacion_tipo(dni, int)
    
    edad = input("Edad: ")
    edad = validacion_tipo(edad, int)
    
    while edad < 18:
        print("No es mayor de edad. Ingrese de nuevo")
        edad = input("Edad: ")
        edad = validacion_tipo(edad, int)
    
    telefono = input("Telefono: ")
    telefono = validacion_tipo(telefono, str)
    
    return Cliente(nombre, dni, edad, telefono)


def crear_administrativo():
    print("Ingresar datos del perfil administrativo")
    nombre = input("Nombre: ")
    nombre = validacion_tipo(nombre, str)
    
    dni = input("DNI: ")
    dni = validacion_tipo(dni, int)
    
    edad = input("Edad: ")
    edad = validacion_tipo(edad, int)
    
    while edad < 18:
        print("No es mayor de edad. Ingrese de nuevo")
        edad = input("Edad: ")
        edad = validacion_tipo(edad, int)
    
    telefono = input("Telefono: ")
    telefono = validacion_tipo(telefono, str)
    
    direccion = input("Dirección: ")
    direccion = validacion_tipo(direccion, str)
    
    return Administrativo(nombre, dni, edad, telefono, direccion)


def iniciar_sesion():
    mensaje = "Elija el método de inicio\n1. DNI\n2. Número de cliente\n"
    
    metodo_inicio = input(mensaje)
    metodo_inicio = validacion_tipo(metodo_inicio, int)
    metodo_inicio = validacion_por_num(opcion=metodo_inicio, num_opciones=2, mensaje=mensaje)
    
    if metodo_inicio == 1:
        
        dni = input("Ingrese el DNI: ")
        dni = validacion_tipo(dni, int)
        dni_hallado = False
        
        while not dni_hallado:
            
            for persona in Cliente.lista_clientes:
            
                if dni == persona.dni:
                    cliente = persona
                    dni_hallado = True
                    print(f"¡Bienvenido {persona.nombre}!")
                    break
            
            if not dni_hallado:
                print("DNI no hallado en la base de datos")
                dni = input("Ingrese el DNI: ")
                dni = validacion_tipo(dni, int)
    
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
            
            if not num_cliente_hallado:
                print("Número de cliente no hallado en la base de datos")
                num_cliente = input("Ingrese el número de cliente: ")
                num_cliente = validacion_tipo(num_cliente, str)
    
    return cliente


def iniciar_sesion_admin():
    legajo = input("Ingrese el legajo: ")
    legajo_hallado = False
    
    while not legajo_hallado:
        
        for persona in Administrativo.lista_admins:
            
            if legajo == persona.legajo:
                admin = persona
                legajo_hallado = True
                print(f"Bienvenido {persona.nombre}")
                break
        
        if not legajo_hallado:
            print("Legajo no hallado en la base de datos")
            legajo = input("Ingrese el legajo: ")
            legajo = validacion_tipo(legajo, str)
    
    return admin


def ver_compras(cliente: Cliente):
    compras_cliente = []
    
    for compra_cliente in Compra.lista_compras:
        if cliente.num_cliente == compra_cliente.codigo_compra.split()[0]:
            compras_cliente.append(compra_cliente)
    
    rango_compras = max(-4, -1-len(compras_cliente))
    #Si tiene 3 compras al menos, entonces llegamos a -4, que pasa a ser el valor máximo. Antes los valores máximos eran -1 para 0 compras, -2 para 1 compra, etc.
    for i in range(-1, rango_compras, -1):
        print(compras_cliente[i])
        print()


def realizar_compras(cliente: Cliente):
    opcion_seguir_comprando = 1
    while opcion_seguir_comprando == 1:
        fecha_uso = input("Fecha para su uso: ")
        
        cant_adultos = input("Cantidad de adultos: ")
        cant_adultos = validacion_tipo(cant_adultos, int)
        
        cant_menores = input("Cantidad de menores: ")
        cant_menores = validacion_tipo(cant_menores, int)
        
        cant_mayores = input("Cantidad de mayores: ")
        cant_mayores = validacion_tipo(cant_mayores, int)
        
        mensaje_parque = "¿A cuál parque quiere ir?\n1. Acuático\n2. Esportland\n3. Aventura\n4. Multipase\n"
        opcion_parque = input(mensaje_parque)
        opcion_parque = validacion_tipo(opcion_parque, int)
        opcion_parque = validacion_por_num(opcion=opcion_parque, num_opciones=4, mensaje=mensaje_parque)
        
        compra = Compra(fecha_uso, cant_adultos, cant_menores, cant_mayores, cliente, opcion_parque)
        
        pago = Pago(compra)
        pago.pagar()

        mensaje_seguir_comprando = "¿Quiere seguir comprando?\n1. SI\n2. NO\n"
        opcion_seguir_comprando = input(mensaje_seguir_comprando)
        opcion_seguir_comprando = validacion_tipo(opcion_seguir_comprando, int)
        opcion_seguir_comprando = validacion_por_num(opcion=opcion_seguir_comprando, num_opciones=2, mensaje=mensaje_seguir_comprando)


def calcular_ventas():
    def filtrar_parques(parque, compra):
        if compra.parque == parque:
            return compra
    
    def filtrar_mes(mes, compra):
        fecha = pd.Timestamp(compra.fecha_uso)
        if fecha.month == mes:
            return compra
    
    for i in range(1, 4):
        compras_parque = filter(lambda comp: filtrar_parques(i, comp), Compra.lista_compras)
        compras_parque = list(filter(lambda comp: filtrar_mes(datetime.now().month, comp), compras_parque))
        
        cant_total_parque = 0
        for compra_parque in compras_parque:
            cant_total_parque += compra_parque.cant_total
        
        if i == 1:
            print("Cantidad total vendida del parque Acuático en el mes", datetime.now().month, "es", cant_total_parque)
        elif i == 2:
            print("Cantidad total vendida del parque Esportland en el mes", datetime.now().month, "es", cant_total_parque)
        else:
            print("Cantidad total vendida del parque Aventura en el mes", datetime.now().month, "es", cant_total_parque)


def bienvenida(codigo_compra_error = ""):
    print("¡Bienvenido al Parque de la Costa!")
    
    mensaje_general = "¿Es usted un cliente o un personal administrativo?"
    print(mensaje_general)
    opcion_general = input("1. Cliente\n2. Administrativo\n")
    opcion_general = validacion_tipo(opcion_general, int)
    opcion_general = validacion_por_num(opcion=opcion_general, num_opciones=2, mensaje=mensaje_general)
    
    if opcion_general == 2:
        mensaje_admin = "1. Crear usuario administrativo\n2. Ingresar\n3. Salir\n"
        opciones_admin = input(mensaje_admin)
        opciones_admin = validacion_tipo(opciones_admin, int)
        opciones_admin = validacion_por_num(opcion=opciones_admin, num_opciones=3, mensaje=mensaje_admin)
        
        if opciones_admin == 1:
            admin = crear_administrativo()
        elif opciones_admin == 2:
            admin = iniciar_sesion_admin()
        else:
            print("¡Vuelva pronto!")
            return
        
        seguir = 1
        while seguir == 1:
            mensaje_tareas_admin = "1. Realizar venta\n2. Ver información de las ventas del mes de cada uno de los parques\3. Ver gráfica de barras de las ventas de cada día del mes de todo el parque\n"
            opciones_tareas_admin = input(mensaje_tareas_admin)
            opciones_tareas_admin = validacion_tipo(opciones_tareas_admin, int)
            opciones_tareas_admin = validacion_por_num(opcion=opciones_tareas_admin, num_opciones=3, mensaje=mensaje_tareas_admin)
            
            if opciones_tareas_admin == 1:
                pago = Pago(codigo_compra_error)
                pago.pagar()
            
            elif opciones_tareas_admin == 2:
                calcular_ventas()
            
            mensaje_seguir = "¿Quiere seguir realizando tareas?\n1. SI\n2. NO\n"
            seguir = input("¿Quiere seguir realizando tareas?\n1. SI\n2. NO\n")
            seguir = validacion_tipo(seguir, int)
            seguir = validacion_por_num(opcion=seguir, num_opciones=2, mensaje=mensaje_seguir)
    
    else:
    
        mensaje_usuario = "¿Ya tiene usuario?\n1. SI\n2. NO\n"
        opcion_ingreso = input(mensaje_usuario)
        opcion_ingreso = validacion_tipo(opcion_ingreso, int)
        opcion_ingreso = validacion_por_num(opcion=opcion_ingreso, num_opciones=2, mensaje=mensaje_usuario)
        
        if opcion_ingreso == 1:
            cliente = iniciar_sesion()
        else:
            cliente = crear_cliente()
        
        seguir = 1
        while seguir == 1:
            mensaje_tareas = "¿Qué desea hacer?\n1. Modificar tus datos\n2. Ver tus últimas 3 compras\n3. Comprar boletos\n"
            opcion_tarea = input(mensaje_tareas)
            opcion_tarea = validacion_tipo(opcion_tarea, int)
            opcion_tarea = validacion_por_num(opcion=opcion_tarea, num_opciones=3, mensaje=mensaje_tareas)
            
            if opcion_tarea == 1:
                cliente.modificar()
            
            elif opcion_tarea == 2:
                ver_compras(cliente)
            
            else:
                realizar_compras(cliente)
            
            mensaje_seguir = "¿Quiere seguir realizando tareas?\n1. SI\n2. NO\n"
            seguir = input("¿Quiere seguir realizando tareas?\n1. SI\n2. NO\n")
            seguir = validacion_tipo(seguir, int)
            seguir = validacion_por_num(opcion=seguir, num_opciones=2, mensaje=mensaje_seguir)


if __name__== '__main__':
    cliente1 = Cliente('Jorge', 40404040, 22, '1514714892')
    bienvenida()