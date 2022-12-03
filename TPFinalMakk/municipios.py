
class Provincia():
    provinciaIDRegistrados = set()
    def __init__(self, provinciaID:str, provincia:str):
        self.provinciaID = provinciaID
        self.provincia = provincia
        if self.provinciaID not in Provincia.provinciaIDRegistrados:
            Provincia.provinciaIDRegistrados.add(self.provinciaID)

    def __str__(self):
        return self.provincia

class Depantamento():
    departamentoIDRegistrados = set()
    def __init__(self, provinciaID:str, provincia:str, departamentoID:int, departamento:str):
        self.provinciaID = provinciaID
        self.provincia = provincia        
        self.departamentoID = departamentoID
        self.departamento = departamento
        if self.departamentoID not in Depantamento.departamentoIDRegistrados:
            Depantamento.departamentoIDRegistrados.add(self.departamentoID)
    
    def __str__(self):
        return self.departamento

class Municipio():
    municipioIDRegistrados = set()
    def __init__(self, provinciaID:str, provincia:str, departamentoID:int, departamento:str, municipioID:str, municipio:str):
        self.provinciaID = provinciaID
        self.provincia = provincia        
        self.departamentoID = departamentoID
        self.departamento = departamento
        self.municipioID = municipioID
        self.municipio = municipio
        if self.municipioID not in Municipio.municipioIDRegistrados:
            Municipio.municipioIDRegistrados.add(self.municipioID)
    
    def __str__(self):
        return self.municipio
