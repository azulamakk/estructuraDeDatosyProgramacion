def validacion_tipo(val, tipo):
    """Verifica si la opción ingresada es del tipo permitido"""
    if isinstance(val, tipo):
        return val
    
    error = True
    while error:
        
        try:
            tipo(val)
        except ValueError:
            print("El caracter ingresado no corresponde a los esperado")
            val = input("Vuelva a ingresar el dato: ")
            continue
        
        error = False
    
    return tipo(val)


def validacion_por_num(opcion: int, num_opciones: int, mensaje: str):
    """Verifica si la opción ingresada se encuentra dentro de las opciones numéricas válidas"""
    lista_num = list(range(1, num_opciones+1))
    
    while opcion not in lista_num:
        print(f"Sólo válidas las opciones del {lista_num[0]} al {lista_num[-1]}")
        opcion = int(input(mensaje))
    
    return opcion