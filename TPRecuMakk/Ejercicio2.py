
listaProductos=[]

class Producto:
    def __init__(self, nombre, codigo, precio):
        self.nombre=nombre
        self.codigo=codigo
        self.precio=precio
    def __str__(self):
        return'''
        Nombre: {}
        Codigo: {}
        Precio: {}
        '''.format(self.nombre, self.codigo, self.precio)

producto1=Producto('TOMATE', 11, 10)
producto2=Producto('AJ0', 22, 20)
producto3=Producto('FIDEOS', 33, 40)

def agregarAListaProductos(productoNuevo):
    codigoNuevo=productoNuevo.codigo
    for producto in listaProductos:
        if codigoNuevo == producto.codigo:
            print('Codigo ya registrado, intente de nuevo')
            codigoNuevo=input('Ingreselo nuevalmente')
            while codigoNuevo.isnumeric()==False:
                codigoNuevo=input('Ingreselo nuevalmente')
            codigoNuevo=int(codigoNuevo)
    listaProductos.append(productoNuevo)

agregarAListaProductos(producto1)
agregarAListaProductos(producto2)
agregarAListaProductos(producto3)

# for producto in listaProductos:
#     print(producto)

productosVendidos=[]
class VentaDeProducto:
    def __init__(self, codigo, nombre, precio, cantidadLlevada):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.cantidadLlevada=cantidadLlevada
        self.total=cantidadLlevada*precio

    def __str__(self):
        return'''
        {}        {}         {}       {}
        '''.format(self.nombre, self.cantidadLlevada, self.precio, self.total)

comprado1=VentaDeProducto(producto1.codigo, producto1.nombre, producto1.precio, 2)
productosVendidos.append(comprado1)
comprado2=VentaDeProducto(producto2.codigo, producto2.nombre, producto2.precio, 4)
productosVendidos.append(comprado2)
comprado3=VentaDeProducto(producto3.codigo, producto3.nombre, producto3.precio, 9)
productosVendidos.append(comprado3)

def imprimirTicket():
    sumaTotal=0
    print('        Nombre    Cantidad    Precio    Total')
    for producto in productosVendidos:
        print(producto)
        sumaTotal+=producto.total
    print('El monto total de la venta es: {}'.format(sumaTotal))

imprimirTicket()