# El banco para el que trabaja necesita un sistema que le permita administrar las cuentas de los usuarios y las
# transacciones que realizan.Las transacciones pueden ser: depósitos o retiros de cantidades arbitrarias de dinero y 
# están asociadas a una cuenta que las realiza.
# Las cuentas corresponden a personas humanas de las cuales se debe conocer el nombre completo, el DNI y el género, además se 
# identifican por un número único de cuenta (CBU). Solo puede existir una cuenta por persona humana.
# El sistema debe permitir añadir y visualizar transacciones para una determinada cuenta, además de visualizar los datos del 
# titular de esta, y su balance. Por último, el sistema debe persistir su información entre usos del mismo es decir que el cierre 
# y posterior reapertura del programa no debe implicar pérdida alguna de información. 
# Asuma que la única forma de cerrar el programa será mediante la opción correspondiente en el menú

DNIsRegistrados = set()
CBUsRegistrados = set()
diccionario = dict()
balances=dict.fromkeys(diccionario, [])
dictBalances = dict()
setTotalTransacciones = set()

# Creacion de clientes
class Cliente:
    def __init__(self, DNI, CBU, nombreCompleto, genero):
        self.DNI = DNI
        self.CBU = CBU
        self.nombreCompleto = nombreCompleto
        self.genero = genero

        # Debido a que tanto el DNI como el CBU son unicos:
        try:
            while isinstance(self.DNI, int) == False:
                self.DNI = input('ingrese nuevamente el DNI. No olvide que debe ser un valor NUMERICO')

            while self.DNI in DNIsRegistrados:
                self.DNI = input('Por favor ingrese un numero de DNI no registrado')
            else: 
                DNIsRegistrados.add(self.DNI)   

            while isinstance(self.CBU, int) == False:
                self.CBU = input('ingrese nuevamente el CBU. No olvide que debe ser un valor NUMERICO')

            while self.CBU in CBUsRegistrados:
                self.CBU = input('Por favor ingrese un numero de CBU no registrado')
            else:
                CBUsRegistrados.add(self.CBU)
        
        except:
            print('Dato de tipo erroneo') 

# Añadimos un cliente al programa


def guardarClaseDiccionario(DNI, CBU, nombreCompleto, genero):
    cliente = Cliente(DNI, CBU, nombreCompleto, genero)
    diccionario[cliente.CBU]=[cliente.DNI, cliente.nombreCompleto, cliente.genero]
    return diccionario

azul = guardarClaseDiccionario(44451568, 1, 'Azul de los Angeles Makk', 'F')
print(diccionario)

def almacenar(mensaje): # Con el objetivo de no perder la informacion, se almacena en un archivo TXT
    with open('/Users/azulmakk/Desktop/Estructura de Datos/TP15/Parcial2|Makk/historialTransacciones.TXT', 'w') as fileTXT:
        fileTXT.write(mensaje)

# Menu principal
def anadirYVisualizarTransacciones():
    try:
        CBUcliente = int(input('Ingrese el CBU que busca realizar una transaccion'))
        
        # if CBUcliente not in CBUsRegistrados:
        #     print('No se ha encontrado el CBU. Intente nuevamente.')
        #     return
        # else:
        #     print(diccionario.get(CBUcliente))

        print('Informacion del cliente: ')
        print(diccionario.get(CBUcliente))

        depoOExtraccion=int(input('''
        ¿Desea extraer o depositar dinero?
        1. Si desea extraer
        2. Si desea depositar
        El monto ingresado debe ser positivo. No hay limite maximo.'''))
        while isinstance(depoOExtraccion, int) == False:
            depoOExtraccion = input('Ingrese un valor numerico por favor')
        
        valor=0
        if depoOExtraccion == 1:
            valorNumerico1=int(input('Ingrese el monto que desea extraer. No se admiten centavos: '))
            # while isinstance(valorNumerico1, int) == False and valorNumerico1 > 0:
            #     valorNumerico1 = input('Ingrese un valor numerico valido por favor')    
            valor = (-1) * int(valorNumerico1)
        elif depoOExtraccion == 2:
            valorNumerico2=input('Ingrese el monto que desea depositar. No se admiten centavos: ')
            # while isinstance(valorNumerico2, int) == False and valorNumerico2 > 0:
            #     valorNumerico2 = input('Ingrese un valor numerico valido por favor')  
            valor = int(valorNumerico2)    
        else:
            print('Intentelo de nuevo. La opcion no es valida') 
            return       
        
        # valorAnterior = dictBalances.get(CBUcliente)
        # if valor == None: 
        #     valor 
        # valorActual = valor + valorAnterior
        # dictBalances[CBUcliente] = valorActual

        setTotalTransacciones.add((CBUcliente, valor))
        # for transaccion in dictBalances:
        #     if CBUcliente in CBUsRegistrados:
        #         balances[transaccion.CBUcliente] += valor
        #         setTotalTransacciones.add(transaccion)
        almacenar('Cliente {} ha afectado {} pesos de su cuenta'.format(CBUcliente, valor)) 
        print('Transaccion ha sido anadida')
        for transaccion in setTotalTransacciones:
            if CBUcliente == transaccion[0]:
                print(transaccion)
                
        print('Balance del cliente:')
        # if balances.get(CBUcliente) == None:
        #     print('No se ha encontrado el CBU. Intente nuevamente.')
        #     return
        # else:
        print(dictBalances.get(CBUcliente))

    except:
        print('Ocurrio un error')

def visualizarTransacciones():
    CBUcliente = int(input('Ingrese el CBU que quiere visualizar: '))
    
    # if diccionario.get(CBUcliente) == None:
    #     print('No se ha encontrado el CBU. Intente nuevamente.')
    #     return
    # else:
    print('Informacion del cliente: ')
    print(diccionario.get(CBUcliente))
    print('Las transacciones realizadas son: ')
    for transaccion in setTotalTransacciones:
        if CBUcliente == transaccion.CBUcliente:
            print(transaccion)

    if balances.get(CBUcliente) == None:
        print('')
        return
    else:
        print(balances.get(CBUcliente))

print('''
Ingrese la opcion que desea realizar:
1. Añadir transacciones
2. Visualizar transacciones
3. Exit
''')

def menuPrincipal(opcionIngresada):
    if opcionIngresada == 1:
        anadirYVisualizarTransacciones()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()       

    if opcionIngresada == 2:
        visualizarTransacciones()
        if ingresoNuevo()==True:
            opcionElegida=int(ingresoOpcion())
            menuPrincipal(opcionElegida)
        else:
            exit()     

def ingresoOpcion():
    opcionIngresada=input('Por favor ingrese una opcion: ')
    try:
        if int(opcionIngresada)>13 or int(opcionIngresada)<0:
            opcionIngresada=ingresoOpcion()
        print(opcionIngresada)
        return opcionIngresada
    except ValueError:
        print('Carga de opcion incorrecta')
        opcionIngresada=ingresoOpcion()
        return opcionIngresada

def ingresoNuevo():
    print('¿Desea ingresar otra opcion?')
    opcionNueva=input('Indique Y/N: ').capitalize()
    if opcionNueva == 'Y':
        return True
    elif opcionNueva == 'N':
        return False
    else:
        print('Ingrese Y/N')
        opcionNueva=ingresoNuevo()

opcionElegida=int(ingresoOpcion())

menuPrincipal(opcionElegida)
