from matplotlib import pyplot as plt

listaCamiones=[]
class Camion:
    def __init__(self, patente, toneladasCarga:float, ruta, piloto:int, copiloto:int):
        # Los pilotos y copilotos los identificamos por DNI
        self.patente=patente
        self.toneladasCarga=toneladasCarga
        self.ruta=ruta
        self.piloto=piloto
        self.copiloto=copiloto

    def __str__(self):
        return '''
            Patente: {}
            Toneladas de carga: {}
            Ruta: {}
            Piloto: {}
            Copiloto: {}
        '''.format(self.patente, self.toneladasCarga, self.ruta, self.piloto,self.copiloto)

camion1=Camion('AAA111', 10, 'Nacional', 12345678, 87654321)
listaCamiones.append(camion1)
camion2=Camion('AAB112', 15, 'Internacional', 12345678, 87654321)
listaCamiones.append(camion2)
camion3=Camion('AAB112', 9, 'Internacional', 12345678, 87654321)
listaCamiones.append(camion3)

class Persona:
    def __init__(self, dni, nombreCompleto):
        self.dni=dni
        self.nombreCompleto=nombreCompleto
    def __str__(self):
        return '''
            DNI: {}
            Nombre Completo: {}
        '''.format(self.dni, self.nombreCompleto)    

class Empleado(Persona):
    def __init__(self, dni, nombreCompleto, puesto, tipoLicencia:list): # Se indica que tipo de licencia puede ser mas de una 
        Persona.__init__(self, dni, nombreCompleto)
        self.puesto=puesto
        self.tipoLicencia=tipoLicencia
    def __str__(self):
        return '''
            DNI: {}
            Nombre Completo: {}
            Puesto: {}
            Tipo licencia: {}
        '''.format(self.dni, self.nombreCompleto, self.puesto, self.tipoLicencia)        

def camionesSegunRuta():
    camionNacional=0
    camionInternacional=0
    for camion in listaCamiones:
        if camion.ruta=='Nacional':
            camionNacional+=1
        elif camion.ruta=='Internacional':
            camionInternacional+=1
    print('En total hay registrados {} camiones nacionales y {} camiones internacionales'.format(camionNacional, camionInternacional))
camionesSegunRuta()

def hacerGrafica10Ton():
    supera=0
    nosupera=0
    for camion in listaCamiones:
        if camion.toneladasCarga>10:
            supera+=1
        else:
            nosupera+=1
    SuperaONo=['Supera', 'No Supera']
    sumatoria=[supera,nosupera]
    plt.pie(sumatoria, labels=SuperaONo, autopct='%.2f%%')
    plt.title(label='Camiones que superan las 10 toneladas', loc='center', color='black')
    plt.show()
hacerGrafica10Ton()

