import numpy as np

class Barco:
    def _init_(self, posiciones):
        self.posiciones = posiciones
        self.restantes = len(posiciones)

class BatallaNaval:
    def _init_(self, barcosJugador1, barcosJugador2):
        self.tablero1 = np.empty(shape=(5,5), dtype=Barco)
        self.tablero2 = np.empty(shape=(5,5), dtype=Barco)

        for barco in barcosJugador1:
            for posicion in barco.posiciones:
                self.tablero1[posicion] = barco
                        
        for barco in barcosJugador2:
            for posicion in barco.posiciones:
                self.tablero2[posicion] = barco

        self.turnoJugador1 = True
        self.barcosRestantes1 = len(barcosJugador1)
        self.barcosRestantes2 = len(barcosJugador2)
    
    def atacar(self, fila, columna):
        tablero = self.tablero2 if self.turnoJugador1 else self.tablero1
        barco = tablero[fila,columna]
        if barco == None:
            print("Agua")
        else:
            barco.restantes -= 1

            if barco.restantes == 0:
                print("Hundido")
                if self.turnoJugador1:
                    self.barcosRestantes2 -= 1
                else:
                    self.barcosRestantes1 -= 1
            else:
                print("Tocado")
            
            tablero[fila,columna] = None

            self.chequearFinalizado()
        
        self.turnoJugador1 = not self.turnoJugador1

    def chequearFinalizado(self):
        if self.barcosRestantes1 == 0:
            print("Jugador 2 gana")
        elif self.barcosRestantes2 == 0:
            print("Jugador 1 gana")

            

barco1 = Barco([(0,0), (0,1)])
barco2 = Barco([(1,0)])
barco3 = Barco([(2,0)])
barco4 = Barco([(3,0), (3,1)])


batalla = BatallaNaval([barco1, barco2], [barco3, barco4])
batalla.atacar(2, 0)
batalla.atacar(0, 0)
batalla.atacar(0, 1)
batalla.atacar(0, 1)
batalla.atacar(1, 0)
batalla.atacar(1, 0)