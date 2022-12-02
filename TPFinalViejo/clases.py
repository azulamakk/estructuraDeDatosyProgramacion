from datetime import datetime

class Barrio():
    barrios = {}
    def __init__(self,nombre):
        self.nombre = nombre
        Barrio.barrios[self.nombre] = self
        self.bandas = set()
        self.cantidad = 1
        self.generos = {"ROCK":0,"INSTRUMENTAL":0,"INDIE":0,"SOLISTA":0,"PUNK":0,"POP":0,"METAL / HEAVY":0,"SKA / REGGAE":0,"FOLKLORE":0,"JAZZ":0,"TROPICAL / LATINO":0,"BLUES":0,"HIP HOP / RAP":0,"MELODICO":0,"NEW AGE":0,"TANGO":0,"ELECTRO / DANCE":0,"FUNK":0,"PERCUSION":0,"Maximo":0}
        self.maximo = None #str del género
    def __str__(self):
        return self.nombre


class Banda():
    bandas = {}
    por_genero = {"ROCK":[0,0,0,None],"INSTRUMENTAL":[0,0,0,None],"INDIE":[0,0,0,None],"SOLISTA":[0,0,0,None],"PUNK":[0,0,0,None],"POP":[0,0,0,None],"METAL / HEAVY":[0,0,0,None],"SKA / REGGAE":[0,0,0,None],"FOLKLORE":[0,0,0,None],"JAZZ":[0,0,0,None],"TROPICAL / LATINO":[0,0,0,None],"BLUES":[0,0,0,None],"HIP HOP / RAP":[0,0,0,None],"MELODICO":[0,0,0,None],"NEW AGE":[0,0,0,None],"TANGO":[0,0,0,None],"ELECTRO / DANCE":[0,0,0,None],"FUNK":[0,0,0,None],"PERCUSION":[0,0,0,None]}
    # posición 0 --> cantidad de bandas
    # posición 1 --> cantidad de discos
    # posición 2 --> cantidad de integrantes
    # posición 3 --> promedio de integrantes por banda

    por_genero2 = {"ROCK":set(),"INSTRUMENTAL":set(),"INDIE":set(),"SOLISTA":set(),"PUNK":set(),"POP":set(),"METAL / HEAVY":set(),"SKA / REGGAE":set(),"FOLKLORE":set(),"JAZZ":set(),"TROPICAL / LATINO":set(),"BLUES":set(),"HIP HOP / RAP":set(),"MELODICO":set(),"NEW AGE":set(),"TANGO":set(),"ELECTRO / DANCE":set(),"FUNK":set(),"PERCUSION":set(),"Maximo":0}
    genero_maximo = None #género con más estilos

    def __init__(self,solista,genero,estilo,fecha,redes,discos,barrio,integrantes):
       
        self.solista = solista #str
        Banda.bandas[self.solista] = self
        
        self.genero = genero #str
        
        self.estilo = estilo #str
        if len(estilo) != 0:
            Banda.por_genero2[self.genero].add(self.estilo)
            n = len(Banda.por_genero2[self.genero])
            if n > Banda.por_genero2["Maximo"]:
                Banda.genero_maximo = self.genero
                Banda.por_genero2["Maximo"] = n
        
        fecha = fecha.split("/") #fecha está en formato dd/mm/yy
        self.fecha = datetime(int(fecha[2]),int(fecha[1]),int(fecha[0])) #se guarda como yy/mm/dd - Aclaración: el año se guarda como 14, 15, 16, 17 o 18.
        
        self.redes = len(redes) #cantidad de links en la lista (int)
        
        self.discos = discos #lista de discos
        
        self.integrantes = integrantes #int
        
        Banda.por_genero[self.genero][0] += 1
        Banda.por_genero[self.genero][1] += len(self.discos)
        Banda.por_genero[self.genero][2] += self.integrantes
        Banda.por_genero[self.genero][3] = Banda.por_genero[self.genero][2]/Banda.por_genero[self.genero][0] # siempre distinto de 0
        if len(barrio) != 0:
            if barrio not in Barrio.barrios.keys():
                barrio = Barrio(barrio)
            else: 
                barrio = Barrio.barrios[barrio]
                barrio.cantidad += 1
            self.barrio = barrio #objeto de la clase barrio
            self.barrio.bandas.add(self)
            self.barrio.generos[self.genero] += 1
            if self.barrio.generos[self.genero] > self.barrio.generos["Maximo"]: #priorizamos al genero que primero llega a esa antidad de bandas (no ponmos >=)
                self.barrio.generos["Maximo"] = self.barrio.generos[self.genero]
                self.barrio.maximo = self.genero
        else:
            self.barrio = "Sin barrio registrado"
    
    def __str__(self):#validar cuando hay cosas vacías
        return "Solista: "+self.solista+"\nGénero: "+self.genero+"\nEstilo: "+self.estilo+"\nFecha de inscripción: "+str(self.fecha)+"\nCantidad de redes sociales: "+str(self.redes)+"\nDiscos: "+str(self.discos)+"\nBarrio: "+str(self.barrio)+"\nCantidad de integrantes: "+str(self.integrantes)




        
