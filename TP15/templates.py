import datetime

###############################################
# INGRESAR FECHA Y HORA
###############################################
def IngresoFechayHora():
    try:
        diaFecha= obtenerInt('Ingrese un dia: ', 0, 31)

        mesFecha= obtenerInt('Ingrese un mes: ', 0, 12)

        anioFecha= obtenerInt('Ingrese un año: ', 2019, 2022)

        horaFecha= obtenerInt('Ingrese una hora: ', 0, 23)

        minutosFecha= obtenerInt('Ingrese un minuto: ', 0, 59)

        fecha = datetime.datetime(anioFecha, mesFecha, diaFecha, horaFecha, minutosFecha)
        print(fecha)
        return fecha
    except:
        'Hubo un error en la informacion'
    
    return fecha

def obtenerInt(mensaje, minimo, maximo):
    try:    
        numero = int(input(mensaje))

        if numero < minimo or numero > maximo:
            print('Numero de fecha incorrecto. Intente de nuevo')
            return obtenerInt(mensaje, minimo, maximo)
        else:
            return numero

    except ValueError or TypeError:
        print('Dato de tipo erroneo')
        return obtenerInt(mensaje, minimo, maximo)

