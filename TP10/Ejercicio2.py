#Realizar un programa que permita mantener actualizada la información de los diferentes hoteles que
# forman parte de la cadena de hoteles “Estructuras y nada más”. De cada Hotel se deben mantener
# actualizados los atributos nombre(string),idHotel (int), zona(string), y precio (int).
# Las zonas donde podrán estar los hoteles son: "playa", "montaña" o "rural". 
# El precio por noche supondremosque es un dato en euros que podrá tomar valores entre 40 y 150.
# Los id de los hoteles son únicos e irrepetibles, para el almacenamiento de los hoteles deberá usar un conjunto.
# El programa realizará las siguientes tareas:
# 1. Carga de Data
# 2. Visualización de los hoteles que tiene la cadena de hoteles
# 3. Dada una zona por el usuario mostrar los hoteles disponibles y el precio por noche.
# ESTA MAL
hotelesCargados=[]


class Hotel:
    def __init__(self):
        idHoteles={}

        self.nombre=input('Ingrese nombre')
        self.idHotel=input('Ingrese ID')
        self.zona=input('Ingrese zona')
        self.precio=input('Ingrese precio')
        
        if zonaCumple()==False:
            print('ingrese una zona posible')
            self.zona=input('intente nuevamente')
        
        if self.precio<=40 and self.precio>=150:
            print('ingrese un monto entre 40 y 150 euros')
            self.precio=input('intente nuevamente')
            
        if self.idHotel in idHoteles:
            print('ingrese un id no registrado')
            self.idHotel=input('intente nuevamente')
        else:
            idHoteles.update((self.idHotel))


        def zonaCumple(self, zona):
            zonasPosibles=('playa', 'montaña', 'rural')
            if zona not in zonasPosibles:
                return False
            else:
                return True 
        
    def agregarHotel(self, hotelCargado):
        return hotelesCargados.append(hotelCargado)
    
def hotelDeCadaZona(self, zonaBuscada):
    for hotel in range(len(hotelesCargados)):
        if zonaBuscada==hotel[2]:
            print(hotelesCargados[hotel[2]] , hotelesCargados[hotel[3]])

print('''
    1. Cargar data
    2. Visualizacion de hoteles de la cadena
    3. Hoteles disponibles y precio por noche
    ''')

opcionIngresada=input(str('Ingrese una opcion: '))

def menuPrincipal(opcion):
    if opcion=='1':
        hotelCargado=Hotel()
        hotelCargado.agregarHotel()
    elif opcion=='2':
        print(hotelesCargados)
    elif opcion=='3':
        zonaBuscada=input('ingrese la zona que esta buscando')
        hotelDeCadaZona(zonaBuscada)
    else:
        print('La opcion ingresada no es valida')
        menuPrincipal(input('Ingrese nuevamente una opcion'))
    return

menuPrincipal(opcionIngresada)
hotel1=Hotel('aaa', 1, 'rural', 50)
hotel2=Hotel('bbb', 2, 'playa', 40)
hotel3=Hotel('ccc', 3, 'montaña', 60)