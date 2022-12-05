from municipios import *
from conexiones import *
from queue import Queue


class Router():
    diccionarioRouter: dict[str,'Router'] = dict()
    
    def __init__(self, routerID:int, identificador:str, ubicacion, latitud:float, longitud:float, municipioID:str, provinciaID:str, departamentoID:int):
        self.routerID = routerID
        self.identificador = identificador
        self.ubicacion = ubicacion
        self.latitud = latitud
        self.longitud = longitud
        self.municipioID = municipioID
        self.provinciaID = provinciaID
        self.departamentoID = departamentoID
        self.conexiones = []
        self.colaConexionesPendiente = Queue()

        if self.provinciaID not in Provincia.diccionarioProv:
            raise Exception("Provincia no registrada")
        if self.departamentoID not in Provincia.diccionarioProv[self.provinciaID].diccionarioDptos:
            raise Exception("Departamento no registrado")
        if self.municipioID not in Provincia.diccionarioProv[self.provinciaID].diccionarioDptos[self.departamentoID].diccionarioMunicipios:
            raise Exception("Municipio no registrado")
        
        if self.routerID not in Router.diccionarioRouter:
            Router.diccionarioRouter[self.routerID] = self        
            
    #Metodo para agregar las conexiones extraidas a los routers asociados entre direccionIP-routerID
    #Llamar a esta funcion cuando se esten leyendo las conexiones del csv, para saber si appendearlas a la lista
    #de conexiones del router o mandarla a la cola de espera
    # def agregarConexion(conexion):
    #     for conexion.direccionIP in Conexion.conexionIDRegistrados.keys():
    #         for router in Router.diccionarioRouter.keys():
    #             if router == conexion.direccionIP:
    #                 if len(router.conexiones) <= 20: #si el router tiene menos de 20 conexiones, agregar la conexion
    #                     router.conexiones.append(conexion)
    #                 else:
    #                     Router.colaConexionesPendiente.put_nowait() #agrego la conexion a la cola de pendientes

    def __str__(self):
        return self.identificador

    
        