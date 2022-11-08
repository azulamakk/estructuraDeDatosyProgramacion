# Escribir el siguiente programa con un diccionario.programa que implemente una agenda. 
# En la agenda se podrán guardar nombres y números de teléfono.El programa nos dará el siguiente menú:
# 1.Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debemostrar el teléfono y, opcionalmente, 
# permitir modificarlo si no es correcto. Si el nombreno se encuentra, debe permitir ingresar el teléfono correspondiente.
#2.Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactoscuyos nombres comiencen por dicha cadena.
# 3.Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de laagenda.
# 4.Listar: Nos muestra todos los contactos de la agenda

agenda = {'Azul': 11111111, 'Tatu': 2222222}
print(agenda)
print('''
1. Añadir/modificar
2. Buscar
3. Borrar
4. Listar
''')

opcionIngresada = int(input('Ingrese una opcion: '))

def anadirOModificar(diccionario):
    llave = input('Ingrese el valor que busca modificar o añadir: ')
    if diccionario.get(llave) == None: # Agrega
        valor=input('Ingrese el numero para {}: ').format(llave)
        diccionario[llave] = valor
    else: # Modifica
        valor=input('Ingrese el numero para {}: ').format(llave)
        diccionario.update(llave = valor)

def buscar(diccionario):
    llave = input('Ingrese el valor que quiere buscar: ')
    if diccionario.get(llave) == None:
        print('No se ha encontrado el valor')
    else:
        print(diccionario.get(llave))

def borrar(diccionario):
    llave = input('Ingrese el valor que quiere borrar: ')    
    if diccionario.get(llave) == None:
        print('No se ha encontrado el valor')
    else:
        diccionario.pop(llave)
        print(diccionario)

def listar(diccionario):
    return print(*diccionario.items(), sep='\n')
    
if opcionIngresada == 1:
    anadirOModificar(agenda)
elif opcionIngresada == 2:
    buscar(agenda)
elif opcionIngresada == 3:
    borrar(agenda)
elif opcionIngresada == 4:
    listar(agenda)



