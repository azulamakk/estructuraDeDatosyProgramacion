#Realizar una función que dadas dos cadenas de caracteres de igual longitud N, 
# verifique si existe algunapermutación posible en cualquiera de las cadenas, 
# de modo que cada carácter de una cadena sea mayor oigual a cada carácter de la otra cadena, en el índice correspondiente. 
# La función debe devolver verdaderosi es posible la permutación en caso contrario devolverá falso.

#funciones propias
def comparar (cadenaa,cadenab):
    menor=True
    for i in range(len(cadenaa)):
        if cadenaa[i]<cadenab[i]:
            menor=False
    return menor
          
def ordenar(cadena):
    for  i in range(len(cadena)-1):
        for j in range(i+1,len(cadena)):
            if ord(cadena[i])>ord(cadena[j]):
                aux=cadena[i]
                cadena[i]=cadena[j]
                cadena[j]=aux
    return cadena

def grande(cadena1, cadena2):
    if comparar(cadena1,cadena2) or comparar(cadena2,cadena1): 
        print('Verdadero')
    elif comparar(ordenar(cadena1),ordenar(cadena2)) or comparar(ordenar(cadena1),ordenar(cadena2)): 
        print('Después de la permutación: \n','Cadena1:',cadena1,'\n cadena2:',cadena2)
        print('Verdadero')
    else:
        print('Falso')

cadena1=str(input('ingresa una cadena por favor: '))
cadena2=str(input('ingresa otra cadena más por favor: '))
while len(cadena1) != len(cadena2):
    cadena2=str(input('no tienen la misma cantidad de caracteres. \n ingresa otra cadena más, con', len(cadena1),'caracteres por favor: '))
grande(cadena1, cadena2)