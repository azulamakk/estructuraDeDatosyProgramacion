from math import pi

class punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 'X={} y Y={}'.format(self.x, self.y)
    def obtieneX(self):
        return 'X={}'.format(self.x)
    def obtieneY(self):
        return 'Y={}'.format(self.y)

class circulos:
    def __init__(self, radio):
        self.radio=radio
    def __str__(self):
        return 'Circulo de radio {}'.format(self.radio)
    def obtieneRadio(self):
        return 'Radio: {}'.format(self.radio)
    def obtieneArea(self):
        return 'Area: {}'.format((self.radio**2)*pi)
    def obtieneDiametro(self):
        return 'Diametro: {}'.format(self.radio*2)