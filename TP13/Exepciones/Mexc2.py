def divide(x,y):
    try:
        resultado=x/y
    except TypeError:
        print("Ingrese caracteres validos")
    else:
        print(resultado)
    finally:
        print("La ejecucion de la funcion ha terminado")
        

#divide(2,0)
#divide(2,2)
divide(2,"1")