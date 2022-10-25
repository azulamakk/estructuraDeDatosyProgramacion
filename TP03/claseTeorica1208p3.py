class Padre():
    def __init__(self, ojos, cejas):
        self.ojos=ojos
        self.cejas=cejas 
    
    def __str__(self):
        return "ojos color {} y cejas color {}".format(self.ojos,self.cejas)

class Madre():
    def __init__(self, brazos, piernas):
        self.brazos=brazos
        self.piernas=piernas
    def __str__(self):
        return "brazos {} y piernas {}".format(self.brazos,self.piernas)

class Hijo(Padre,Madre):
    def __init__(self, ojos, cejas, cara, brazos, piernas):
        Madre.__init__(self,brazos,piernas)
        Padre.__init__(self,ojos,cejas)
        self.cara=cara
    def __str__(self):
        return "brazos {} y piernas {}".format(self.brazos,self.piernas)

sixto=Padre("cafe","cafe")
print(sixto)

ninfa=Madre(2,2)
print(ninfa)

nicolas=Hijo("cafe", "cafe", "larga", 2,2)
print(nicolas.ojos)