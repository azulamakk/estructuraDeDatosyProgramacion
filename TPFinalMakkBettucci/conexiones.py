from datetime import datetime
from listaEnlazada import ListaEnlazada
import routers

class Conexion:
    # Set con macs registradas en todos los routers
    macsRegistradas = set()

    conexionesHistoricas = ListaEnlazada()

    def __init__(self, direccionIP: str, direccionMAC: int, fecha, hora, activa: int, routerID: str):
        if routerID not in routers.Router.diccionarioRouter:
            raise Exception("Router no encontrado")

        self.direccionIP = direccionIP
        self.direccionMAC = direccionMAC
        self.fechaYHora = datetime.strptime(fecha + " " + hora, "%d/%m/%Y %H:%M:%S")
        self.activa = activa
        self.routerID = routerID

        # Agrego la mac al set de macs activas
        if self.activa == 1 and self.direccionMAC not in Conexion.macsRegistradas:
            Conexion.macsRegistradas.add(self.direccionMAC)
        
        Conexion.conexionesHistoricas.agregar(self)

    # Para orden en lista
    def __lt__(self, other: 'Conexion'):
        return self.fechaYHora < other.fechaYHora
    
    def __str__(self):
        return f"{self.fechaYHora} - {self.direccionIP} - {self.direccionMAC} - {self.activa} - {self.routerID}"