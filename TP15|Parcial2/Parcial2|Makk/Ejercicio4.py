# Diseñe la clase Pedido para una tienda única.El constructor recibe un identificador único numérico del pedido, 
# y dos diccionarios: uno de ellos es un catálogo que indica qué productos existen y su precio. El otro es el 
# contenido del pedido, que indica que productos se desea comprar y cuántas unidades de c/u.La clase debe tener 
# una propiedad correspondiente al precio total de la orden.Debe existir un mecanismo para calcular el precio total 
# promedio de todas las órdenes.
# Realice todas las validaciones correspondientes, garantizando que no pueda crearse un pedido inválido.

catalogo = dict()
catalogo['blusa'] = 100
catalogo['zapatos'] = 200
catalogo['tornillos'] = 50
catalogo['motosierra'] = 1000
pedido = dict()
pedido['blusa'] = 3
pedido['zapatos'] = 1
pedido['motosierra'] = 5

setIDS = set()

class Pedido:
    def __init__(self, IDPedido, catalogo, pedido):
        self.IDPedido = IDPedido
        self.catalogo = catalogo
        self.pedido = pedido

        if self.IDPedido in setIDS: 
            self.CBU = input('Este ID de pedido ya fue utilizado previamente. Intente de nuevo')
        else:
            setIDS.add(self.IDPedido)

pedido1 = Pedido(1, catalogo, pedido)

total = 0
for key in pedido.keys():
    monto = catalogo.get(key)
    cantidad = pedido.get(key)
    aSumar = monto * cantidad
    total += aSumar

print('El monto total a pagar es ${}'.format(total))

