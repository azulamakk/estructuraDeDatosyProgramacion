from tkinter import N
from camiones import camion

class empresa(camion):
    def __init__(self, nombreEmpresa, CUIT, cantTotalCamiones):
        self.nombreEmpresa=nombreEmpresa