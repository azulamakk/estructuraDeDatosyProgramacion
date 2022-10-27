def divide(x,y):
    try:
        resultado=x/y
    except ZeroDivisionError:
        print("Division por Cero")
    else:
        print(resultado)
    finally:
        print("La ejecucion de la funcion ha terminado")
        

#divide(2,0)
#divide(2,2)
divide(2,"1")