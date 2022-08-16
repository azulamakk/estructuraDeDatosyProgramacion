from cliente import Cliente
import time

class Compra():
    costo_boleto_normal = 300
    costo_boleto_multipase = 1000
    descuento_menores = 0.3
    descuento_mayores = 0.5
    lista_compras = []
    
    def __init__(self, fecha_uso, cant_adultos, cant_menores, cant_mayores, cliente: Cliente, parque):
        self.fecha_uso = fecha_uso
        self.cant_adultos = cant_adultos
        self.cant_menores = cant_menores
        self.cant_mayores = cant_mayores
        self.cliente = cliente
        self.parque = parque
        self.codigo_compra = self.cliente.num_cliente + ' ' + str(time.time())
        self.lista_compras.append(self)
    
    def __str__(self):
        cadena = 'Fecha uso: ' + self.fecha_uso + '\nCantidad de adultos: ' + str(self.cant_adultos) + '\nCantidad de menores' + str(self.cant_menores) + '\nCantidad de mayores' + str(self.cant_mayores)
        if self.parque == '1':
            cadena += '\nParque: Acuático'
        elif self.parque == '2':
            cadena += '\nParque: Esportland'
        elif self.parque == '3':
            cadena += '\nParque: Aventura'
        else:
            cadena += '\nParque: Multipase'
        
        cadena += '\nCódigo de compra: ' + self.codigo_compra
        
        return cadena
    
    def calcular_costo(self):
        if self.parque == '4':
            costo_total = (self.cant_adultos + self.cant_menores * self.descuento_menores + self.cant_mayores * self.descuento_mayores) * self.costo_boleto_multipase
        else:
            costo_total = (self.cant_adultos + self.cant_menores * self.descuento_menores + self.cant_mayores * self.descuento_mayores) * self.costo_boleto_normal
        
        return costo_total

if __name__=='__main__':
    cliente = Cliente('pepe', 120102, 25, '124041912')
    compra1 = Compra('30-12-2020', 3, 2, 1, cliente, '1')
    compra2 = Compra('30-12-2020', 2, 3, 0, cliente, '4')

    print(compra1.codigo_compra)
    print(compra2.codigo_compra)
    print(compra1.calcular_costo())
    print(compra2.calcular_costo())
    print(Compra.lista_compras[0].codigo_compra)