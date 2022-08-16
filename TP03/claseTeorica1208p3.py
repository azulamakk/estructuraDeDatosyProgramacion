class padre():
    def __init__(self, ojos, cejas):
        self.ojos=ojos
        self.cejas=cejas 
    
    def __str__(self):
        return "ojos color {} y cejas color {}".format(self.ojos,self.cejas)

class madre():
    def __init__(self, brazos, piernas):
        self.brazos=brazos
        self.piernas=piernas
    def __str__(self):
        return "brazos {} y piernas {}".format(self.brazos,self.piernas)

class hijo(padre,madre):
    def __init__(self, ojos, cejas, cara, brazos, piernas):
        madre.__init__(self,brazos,piernas)
        padre.__init__(self,ojos,cejas)
        self.cara=cara
    def __str__(self):
        return "brazos {} y piernas {}".format(self.brazos,self.piernas)

sixto=padre("cafe","cafe")
print(sixto)

ninfa=madre(2,2)
print(ninfa)

nicolas=hijo("cafe", "cafe", "larga", 2,2)
print(nicolas.ojos)