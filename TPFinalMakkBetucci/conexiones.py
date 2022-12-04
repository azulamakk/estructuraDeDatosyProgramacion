class Conexion:
    def __init__(self, direccionIP:int, direccionMAC:int, fecha, hora, activa:int):
        self.direccionIP = direccionIP
        self.direccionMAC = direccionMAC
        self.fecha = fecha
        self.hora = hora
        self.activa = activa