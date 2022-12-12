class Provincia():
    diccionarioProv: dict[str, 'Provincia'] = dict()

    def __init__(self, provinciaID: str, provincia: str):
        if provinciaID == None:
            raise Exception("Provincia no posee identificador")
        
        if provinciaID in Provincia.diccionarioProv:
            return
            # raise Exception("Provincia ya registrada")

        self.provinciaID = provinciaID
        self.provincia = provincia

        self.diccionarioDptos: dict[str, 'Departamento'] = dict()

        Provincia.diccionarioProv[self.provinciaID] = self


    def __str__(self):
        return self.provincia

class Departamento():

    def __init__(self, provinciaID:str, provincia:str, departamentoID:int, departamento:str):
        self.provinciaID = provinciaID
        self.provincia = provincia        
        self.departamentoID = departamentoID
        self.departamento = departamento

        self.diccionarioMunicipios: dict[str, 'Municipio'] = dict()

        if self.departamentoID == None:
            raise Exception("Departamento no posee identificacion")

        if self.provinciaID not in Provincia.diccionarioProv:
            raise Exception("Provincia no registrada")
        
        prov = Provincia.diccionarioProv[self.provinciaID]

        if self.departamentoID not in prov.diccionarioDptos:
            prov.diccionarioDptos[self.departamentoID] = self
                    
    def __str__(self):
        return self.departamento

class Municipio():

    def __init__(self, provinciaID:str, provincia:str, departamentoID:int, departamento:str, municipioID:str, municipio:str):
        self.provinciaID = provinciaID
        self.provincia = provincia        
        self.departamentoID = departamentoID
        self.departamento = departamento
        self.municipioID = municipioID
        self.municipio = municipio
        
        if self.municipioID == None:
            raise Exception("Municipio no posee identificacion")
        
        if self.provinciaID not in Provincia.diccionarioProv:
            raise Exception("Provincia no registrada")

        prov: Provincia = Provincia.diccionarioProv[self.provinciaID]
        if self.departamentoID not in prov.diccionarioDptos:
            raise Exception("Departamento no registrado")
    
        dpto = prov.diccionarioDptos[self.departamentoID]

        if self.municipioID not in dpto.diccionarioMunicipios:
            dpto.diccionarioMunicipios[self.municipioID] = self

    def __str__(self):
        return self.municipio
