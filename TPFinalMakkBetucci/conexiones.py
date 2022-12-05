from queue import Queue
from routers import *

class Conexion:
    #Iniciamos la cola de conexiones pendientes
    colaConexionesPendientes = Queue()
    #Diccionario con todas las conexiones extraidas del csv conexiones
    conexionIDRegistrados = dict()

    def __init__(self, direccionIP:str, direccionMAC:int, fecha, hora, activa:int):
        self.direccionIP = direccionIP
        self.direccionMAC = direccionMAC
        self.fecha = fecha
        self.hora = hora
        self.activa = activa

        #Agrego la conexion al diccionario de conexiones
        if self.direccionIP not in Conexion.conexionIDRegistrados:
            Conexion.conexionIDRegistrados[self.direccionIP] = self