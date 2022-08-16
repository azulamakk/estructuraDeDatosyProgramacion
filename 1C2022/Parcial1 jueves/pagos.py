from compras import Compra
import random
# import menu

class Pago():
    lista_pagos = []
    
    
    def __init__(self, compra: Compra):
        self.compra = compra
        self.codigo_pago = None
        monto_pago = self.compra.calcular_costo()
        print("El monto pagado fue de ", monto_pago)
    
    
    def pagar(self):
        
        prob = random.random() #Este número lo generamos para simular un error, con un 10% de probabilidades de ocurrir.
        
        if prob < 0.9:
            
            if self.compra.codigo_compra not in self.lista_pagos:
                self.lista_pagos.append(self.compra)
                self.codigo_pago = 'P' + self.compra.codigo_compra
                
                print("El pago fue realizado con éxito")
                return
            
            else:
                print("Ya estaba pagado")
                return
        
        else:
            print("Hay un error en el sistema. Contáctese con administración")
            # menu.bienvenida(self.compra.codigo_compra)