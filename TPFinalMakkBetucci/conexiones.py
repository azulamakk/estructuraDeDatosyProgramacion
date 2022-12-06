from queue import Queue
from routers import *

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        return self.items.popleft()
    
    def primero(self):
        return self.items[0]
    
    def estaVacia(self):
        return len(self.items) == 0
        
    def tamano(self):
        return len(self.items)
        
    def __str__(self):
        return str(self.items)
     
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