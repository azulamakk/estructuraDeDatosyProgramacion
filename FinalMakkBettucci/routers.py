from municipios import *
from conexiones import Conexion
from queue import Queue


class Router():
    diccionarioRouter: dict[str,'Router'] = dict()
    
    def __init__(self, id:int, identificador:str, ubicacion, latitud:float, longitud:float, municipioID:str, provinciaID:str, departamentoID: str):
        if provinciaID not in Provincia.diccionarioProv:
            raise Exception("Provincia no registrada")
        
        prov = Provincia.diccionarioProv[provinciaID]
        if departamentoID not in prov.diccionarioDptos:
            raise Exception("Departamento no registrado")
        
        depto = prov.diccionarioDptos[departamentoID]
        if municipioID not in depto.diccionarioMunicipios:
            raise Exception("Municipio no registrado")
        
        self.id = id
        self.identificador = identificador
        self.ubicacion = ubicacion
        self.latitud = latitud
        self.longitud = longitud
        self.provinciaID = provinciaID
        self.departamentoID = departamentoID
        self.municipioID = municipioID

        self.conexiones = dict()
        self.colaConexionesPendientes: Queue[Conexion] = Queue()
        
        if self.identificador not in Router.diccionarioRouter:
            Router.diccionarioRouter[self.identificador] = self        
            
    #Metodo para agregar las conexiones extraidas a los routers asociados entre direccionIP-routerID
    #Llamar a esta funcion cuando se esten leyendo las conexiones del csv, para saber si appendearlas a la lista
    #de conexiones del router o mandarla a la cola de espera
    def agregarConexion(self, conexion: Conexion):
        if len(self.conexiones) <= 20:
            self.conexiones[conexion.direccionMAC] = conexion
        else:
            self.colaConexionesPendientes.put_nowait(conexion)

    def quitarConexion(self, direccionMAC: int):
        if direccionMAC in self.conexiones:
            self.conexiones[direccionMAC].activa = 0
            del self.conexiones[direccionMAC]
            
            if not self.colaConexionesPendientes.empty(): 
                # Si tenia alguna conexion pendiente la agrego
                aAgregar = self.colaConexionesPendientes.get_nowait()

                self.conexiones[aAgregar.direccionMAC] = aAgregar
        else:
            raise Exception("Conexion no registrada")


    def __str__(self):
        return self.identificador