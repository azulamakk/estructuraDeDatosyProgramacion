from municipios import *

class Router():
    routerIDRegistrados = set()
    def __init__(self, routerID:int, identificador:str, ubicacion, latitud:float, longitud:float, municipioID:str, provinciaID:str, departamentoID:int):
        self.routerID = routerID
        self.identificador = identificador
        self.ubicacion = ubicacion
        self.latitud = latitud
        self.longitud = longitud
        self.municipioID = municipioID
        self.provinciaID = provinciaID
        self.departamentoID = departamentoID

        if self.provinciaID not in Provincia.provinciaIDRegistrados:
            raise Exception("Provincia no registrada")
        if self.departamentoID not in Depantamento.departamentoIDRegistrados:
            raise Exception("Departamento no registrado")
        if self.municipioID not in Municipio.municipioIDRegistrados:
            raise Exception("Municipio no registrado")
            
        if self.routerID not in Router.routerIDRegistrados:
            Router.routerIDRegistrados.add(self.routerID)