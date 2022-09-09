class nodo():
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self) -> str:
        return str(self.dato)

if __name__=='__main__':
    vagon1=nodo('Mango')
    vagon2=nodo('Uvas')
    vagon3=nodo('Peras', vagon1)
    vagon1.prox=vagon2
    print(vagon3)
    print(vagon3.prox)