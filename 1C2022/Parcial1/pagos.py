from compras import Compra

class Pago():
    
    lista_pagos = []
    
    def __init__(self, compra: Compra):
        self.compra = compra
        self.codigo_pago = None
    
    def pagar(self):
        
        if self.compra.codigo_compra not in self.lista_pagos:
            self.lista_pagos.append(self.compra)
            monto_pago = self.compra.calcular_costo()
            self.codigo_pago = 'P' + self.compra.codigo_compra
        
        else:
            print("Ya está pago")