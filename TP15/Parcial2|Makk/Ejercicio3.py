# Usted tiene un food truck, que sirve platos de distintas comidas, y 
# que cambia su menú todos los días.Los distintos platos precocinados (hamburguesa, milanesa, sopa, 
# o lo que sea que se venda en ese día enparticular) por lo general se dan de alta al principio de la jornada, 
# antes de abrir, aunque ocasionalmente ocurre que un proveedor llega tarde o se lo llama en el medio del día a reforzar stock. 
# Para garantizar la calidad, el excedente de productos al final del día se dona a la caridad, nada se conserva de días anteriores,
# por lo que cada día el stock comienza vacío.Para agilizar el servicio, los platos recién salidos se priorizan sobre los viejos que 
# nadie ha venido a buscar,por lo que la persona cuyo plato salió hace 10 segundos tiene prioridad por sobre la persona que olvidó
# retirar su plato, salido hace 1 minuto.El sistema debe disponer de métodos para que el cajero registre un pedido, para que el cocinero 
# tome el pedido y prepare el plato, y para que el cliente retire el plato.El food truck debe cerrar sus puertas a nuevos pedidos en el 
# momento en que no pueda completarse unpedido por falta de stock, y solo las reabrirá al día siguiente.

platosDisponibles = {'milanesa':0, 'sopa':0, 'pastel de papa':0} 
# Utilizamos un set debido a que segun los dias pueden variar los menues caracteristicos y cantidad de oferta

class NodoPila:
    def __init__(self, headvalue, plato, prox=None):
        self.plato = plato
        self.headvalue=headvalue
        self.prox=prox

class Pila:
    def __init__(self):
        self.tope = None

    def agregarAPila(self, valor, plato):
        aAgregar = NodoPila(valor, plato, self.tope)
        self.tope = aAgregar

    def sacarDePila(self):
        if self.estaVacia():
            return None
        else:
            aSacar=self.tope.headvalue
            self.tope=self.tope.prox
            return aSacar

    def estaVacia(self):
        if self.tope == None:
            return True
        else: 
            return False

    def __str__(self):
        return print(self.plato)

    def mostrarTope(self):
        if self.estaVacia():
            return 'Esta vacio'
        return self.tope

stock = Pila()
# Llega stock de proveedor 
for i in range(20): # Cantidad de un producto incorporado
    stock.agregarAPila(1, 'sopa') 
for i in range(200):
    stock.agregarAPila(1, 'pastel de papa') 
for i in range(500):
    stock.agregarAPila(1, 'pastel de papa') 
for i in range(250):
    stock.agregarAPila(1, 'chocotorta') 

def registrarLlegadaProveedor():
    cantidad = int(input('Ingrese cantidad: '))
    plato = input('ingrese plato: ').lower()
    stock.agregarAPila(cantidad, plato)

def registrarPedido():
    if stock.estaVacia():
        print('No hubo ingresos por el dia de hoy. La healdera esta vacia')
    else:
        stock.sacarDePila()
        return stock.mostrarTope

# print(stock.mostrarTope()) # Este fue el ultimo ingreso 
# print(registrarLlegadaProveedor())
print(registrarPedido())