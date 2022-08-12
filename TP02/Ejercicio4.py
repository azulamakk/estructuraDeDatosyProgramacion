#Realizar una función que dadas dos cadenas de caracteres de igual longitud N, 
# verifique si existe algunapermutación posible en cualquiera de las cadenas, 
# de modo que cada carácter de una cadena sea mayor oigual a cada carácter de la otra cadena, en el índice correspondiente. 
# La función debe devolver verdaderosi es posible la permutación en caso contrario devolverá falso.


def verificacionPermutaciones(cadena1, cadena2):
    if len(cadena1) != len(cadena2):
        print("Las cadenas no tienen la misma longitud")
        exit()



    for i in range(len(cadena1)):
        sorted1 = cadena1.sort()
        sorted2 = cadena2.sort()
        if sorted1[i] >= sorted2[i]:
            esPosible=True
        else:
            esPosible=False
            print("Es posible?"+esPosible)
            exit()
        print("Es posible?"+esPosible) #Deberia ser True en este caso

cadena1='aaaa'
cadena2='bbbb'

verificacionPermutaciones(cadena1, cadena2)