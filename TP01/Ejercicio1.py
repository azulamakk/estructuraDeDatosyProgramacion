def menu_principal():
    Opcion=input("""Sistema de Registro automotor
              1.Registro
              2.Examen
              3.Verificación
              4.Salir
              """)
    Opcion=int(Opcion)
    return Opcion

def pedir_registro() :
    DNI=str(input("ingrese DNI: "))
    while len(DNI)!=8:
        DNI=str(input("ingrese DNI: "))
        
    Codigo=(str(input("Empleado: "))).upper()
    # while len(Codigo)!=5:
    #     Codigo=(str(input("Empleado: "))).upper()
    for i in range(0,3):
        while ord(Codigo[i])<65 or ord(Codigo[i])>90:
            Codigo=(str(input("Empleado: "))).upper()
    for i in range(3,4):
        while ord(Codigo[i])<48 or ord(Codigo[i])>57:
            Codigo=(str(input("Empleado: "))).upper()
    
    Tipo=(str(input("Tipo: "))).upper()   
    while Tipo!='PAR' and Tipo!='PRO':
        Tipo=(str(input("Tipo: "))).upper()

    Item=DNI+Codigo+Tipo
    #Datos.append(Item)
    print("El numero de tramite es: ",Item)
    return Item

def segundo_menu():
    AoB=(str(input("Validar por DNI (opción A) o validar por número de trámite (opción B): "))).upper()
    if (AoB=='A'):
        Comprobacion=input("Ingrese DNI:")
    elif (AoB=='B'):
        Comprobacion=input("Ingrese numero de tramite")
    return Comprobacion

def comprobar_registro(Datos,Comprobacion):
    i=0
    total=[]
    for i in range(len(Datos)):
        resultado=Datos[i].find(Comprobacion)
        total.append(resultado)
        i+=1
    i=0
    for j in total:
        if(j!=-1):
            return i
        i+=1

def nota_promedio():
    n1=int(input("Ingrese nota teorico: "))
    n2=int(input("ingrese nota practico: "))
    return ((n1+n2)/2)


Datos=[]
Nota=[]
i=0
Opcion=int(menu_principal())

while (Opcion!=4):
    if (Opcion==0):
        Opcion=int(menu_principal())

    elif(Opcion==1):
        tramite=pedir_registro()
        Datos.append(tramite)
        Opcion=int(menu_principal())
        print(Datos[i])
        i+=1

    elif(Opcion==2):
        Comprobacion=segundo_menu()
        print(Comprobacion)
        dato=comprobar_registro(Datos,Comprobacion)
        if dato>=0:
            print("Se encontro")
            nota=nota_promedio()
            Nota.insert(dato,nota)
        else:
            print("no se encontro")
        Opcion=int(menu_principal())
        
    elif (Opcion==3):
        Comprobacion=segundo_menu()
        print(Comprobacion)
        dato=comprobar_registro(Datos,Comprobacion)
        if dato>=0:
            print(Nota[dato])
            if Nota[dato]>=70:
                print("Aprobo")
            else:
                print("No aprobo")
        Opcion=int(menu_principal())
    else:
        Opcion=int(menu_principal())
        
print(">>>Fin")