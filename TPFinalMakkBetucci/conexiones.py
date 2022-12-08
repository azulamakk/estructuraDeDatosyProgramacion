from routers import *

class Conexion:
    # Set con macs registradas en todos los routers
    macsRegistradas = set()

    # TODO: Agregar arbol historico de conexiones


    def __init__(self, direccionIP: str, direccionMAC: int, fecha, hora, activa: int, routerID: str):
        self.direccionIP = direccionIP
        self.direccionMAC = direccionMAC
        self.fecha = fecha
        self.hora = hora
        self.activa = activa
        self.routerID = routerID

        #Agrego la mac al set de macs activas
        if self.activa == 1 and self.direccionMAC not in Conexion.macsRegistradas:
            Conexion.macsRegistradas.add(self.direccionMAC)
        
        # TODO: Agregar a conexiones historicas


        