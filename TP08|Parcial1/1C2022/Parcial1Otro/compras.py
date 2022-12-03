from cliente import Cliente
import time

class Compra():
    costo_boleto_normal = 300
    costo_boleto_multipase = 1000
    descuento_menores = 0.3
    descuento_mayores = 0.5
    
    lista_compras = []
    
    
    def __init__(self, fecha_uso: str, cant_adultos: int, cant_menores:int , cant_mayores: int, cliente: Cliente, parque: int):
        self.fecha_uso = fecha_uso
        self.cant_adultos = cant_adultos
        self.cant_menores = cant_menores
        self.cant_mayores = cant_mayores
        self.cant_total = self.cant_adultos + self.cant_menores + self.cant_mayores
        
        self.cliente = cliente
        self.parque = parque
        
        self.codigo_compra = self.cliente.num_cliente + ' ' + str(time.time())
        self.lista_compras.append(self)
    
    
    def __str__(self):
        cadena = f"Fecha uso: {self.fecha_uso}\nCantidad de adultos: {self.cant_adultos}\nCantidad de menores {self.cant_menores}\nCantidad de mayores {self.cant_mayores}"
        
        if self.parque == 1:
            cadena += '\nParque: Acuático'
        elif self.parque == 2:
            cadena += '\nParque: Esportland'
        elif self.parque == 3:
            cadena += '\nParque: Aventura'
        else:
            cadena += '\nParque: Multipase'
        
        cadena += '\nCódigo de compra: ' + self.codigo_compra
        
        return cadena
    
    
    def calcular_costo(self):
        if self.parque == 4:
            costo_total = (self.cant_adultos + self.cant_menores * self.descuento_menores + self.cant_mayores * self.descuento_mayores) * self.costo_boleto_multipase
        else:
            costo_total = (self.cant_adultos + self.cant_menores * self.descuento_menores + self.cant_mayores * self.descuento_mayores) * self.costo_boleto_normal
        
        return costo_total


# Verificaciones dentro del módulo
# if __name__=='__main__':
cliente = Cliente('pepe', 120102, 25, '124041912')
compra1 = Compra('2020-4-12', 3, 2, 1, cliente, 1)
compra2 = Compra('2020-4-2', 2, 3, 0, cliente, 2)
compra3 = Compra('2020-4-12', 3, 2, 1, cliente, 3)
compra4 = Compra('2020-4-3', 2, 3, 0, cliente, 4)
compra5 = Compra('2020-4-4', 3, 2, 1, cliente, 1)
compra6 = Compra('2020-4-5', 2, 3, 0, cliente, 2)
compra7 = Compra('2020-4-4', 3, 2, 1, cliente, 3)
compra8 = Compra('2020-4-4', 2, 3, 0, cliente, 4)
compra9 = Compra('2020-4-5', 3, 2, 1, cliente, 1)
compra10 = Compra('2020-4-6', 2, 3, 0, cliente, 2)
compra11 = Compra('2020-4-7', 3, 2, 1, cliente, 3)
compra12 = Compra('2020-4-8', 2, 3, 0, cliente, 4)

    # print(compra1.codigo_compra)
    # print(compra2.codigo_compra)
    # print(compra1.calcular_costo())
    # print(compra2.calcular_costo())
    # print(Compra.lista_compras[0].codigo_compra)