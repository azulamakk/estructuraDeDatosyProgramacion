import numpy as np 

class BatallaNaval:
    def __init__(self, posicionBarco111, posicionBarco112,posicionBarco121, posicionBarco122, posicionBarco21, posicionBarco22):
        self.posicionBarco111=posicionBarco111
        self.posicionBarco112=posicionBarco112
        self.posicionBarco121=posicionBarco121
        self.posicionBarco122=posicionBarco122
        self.posicionBarco21=posicionBarco21
        self.posicionBarco22=posicionBarco22
        self.tablero=BatallaNaval.armartablero(self)

    def armartablero(self):
        tablero = np.zeros([5,5], dtype=int)
        
        tablero[self.posicionBarco111][self.posicionBarco112]=1
        tablero[self.posicionBarco121][self.posicionBarco122]=1
        tablero[self.posicionBarco21][self.posicionBarco21]=1
        print(tablero)
        return tablero 
    
    def atacar(self, ejex, ejey):
        if self.tablero[ejex][ejey]==1:
            print('Hundido.')
            self.tablero[ejex][ejey]=0
        else:
            print('Agua. Siga participando.')
        print(self.tablero)
        if self.tablero[self.posicionBarco111][self.posicionBarco112]==0 and self.tablero[self.posicionBarco121][self.posicionBarco122]==0 and self.tablero[self.posicionBarco21][self.posicionBarco21]==0:
            print('Se han derribado todos los barcos. Enhorabuena! Has ganado')

juego1=BatallaNaval(1, 1, 1, 2, 4,4)
juego1.atacar(1,1)
juego1.atacar(1,2)
juego1.atacar(4,3)