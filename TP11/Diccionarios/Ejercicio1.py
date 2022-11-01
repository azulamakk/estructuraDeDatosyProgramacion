# Utilizando la información de las ventas de las diferentes zonas de influencia de cada uno los vendedores de
# la empresa “Si se puede”, usted debe realizar un programa que permita realizar las siguientes tareas:
# 1. Crear un diccionario que permita manejar la información de las ventas en cada zona de cada vendedor.
# 2. Preguntar al usuario si desea modificar alguna información existente en la data, de ser así pedir
# nombre del vendedor, la zona de influencia y el valor de la venta a modificar.
# 3. Visualizar las ventas totales de la empresa
# 4. Visualizar la zona de mayores ventas.

class Venta():
    def __init__(self, vendedor, zona, fecha,monto):
        self.vendedor=vendedor
        self.zona=zona
        self.fecha=fecha
        self.monto=monto

opcionIngresada=input('Ingrese una opcion')
def menuPrincipal():
    print('''
    
    ''')

