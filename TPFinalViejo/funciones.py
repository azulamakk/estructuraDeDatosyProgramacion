from clases import * 
from datetime import datetime
import matplotlib.pyplot as plt

def cargar_datos():
    with open("/Users/azulmakk/Desktop/Estructura de Datos/TPFinalViejo/bandas-inscriptas.txt","r") as file:
        for line in file:
            line = line.split(";")
            if line[0] != "NOMBRE_DEL_SOLISTA_DE_LA_BANDA": #evitamos la primer fila
                solista = line[0]
                genero = line[1]
                estilo = line[2] #puede ser vacío
                fecha = line[3]
                redes = [line[4],line[5]]+line[6].split(",")
                n = redes.count("")
                for i in range(n):
                    redes.remove("")
                discos = line[7].split(",") # puede ser vacío
                barrio = line[10] # puede ser vacío
                integrantes = int(line[11])
                banda = Banda(solista,genero,estilo,fecha,redes,discos,barrio,integrantes)
    return

def opciones_barrio():
    i = 1
    barrios = dict()
    for barrio in Barrio.barrios.keys():
        barrios[i] = barrio #se va gnerando un dict con la clave i para poder asociar la respuesta del usuario
        print(i,")",barrio)
        i += 1
    seguir = True
    while seguir:
        try:
            rta = int(input("Seleccionar barrio: "))
            if rta not in range(1,i):
                raise Exception("\nOpción no válida\n")
            else:
                seguir = False
        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.')
        except Exception as e:
            print(e)
    return barrios[rta]

def opcion1():
    barrionombre = opciones_barrio()
    barrio = Barrio.barrios[barrionombre]
    with open("Bandas por barrio.txt","w") as filetxt:
        print("La cantidad de bandas en",barrionombre,"es",barrio.cantidad,file=filetxt)
        print("Nombres:",file=filetxt)
        for banda in barrio.bandas:
            print(banda.solista,file=filetxt)
    print("\n¡El archivo txt fue creado con éxito!\n")
    return

def pedir_fecha():
    seguir = True
    while seguir:
        try:
            yy = int(input("Ingrese año en formato yy: "))
            if len(str(yy)) != 2:
                raise Exception("\n"+str(yy)+" no está en formato yy\n")
            else:
                mm = int(input("Ingrese mes en formato mm: "))
                if mm not in range(1,13):
                    raise Exception("\n"+str(mm)+" no corresponde a un número de mes\n")
                else:
                    dd = int(input("Ingrese día en formato dd: "))
                    if dd not in range(1,32):
                        raise Exception("\n"+str(dd)+" no corresponde a un día del mes\n")
                    else:
                        seguir = False
        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.')
        except Exception as e:
            print(e)
    fecha = datetime(yy,mm,dd)
    return fecha

def promedio_opcion2(barrio,fechalimite):
    conta = 0
    for banda in barrio.bandas:
        if banda.fecha <= fechalimite:
            conta += 1
    promedio = conta/barrio.cantidad #siempre es distinta de 0 --> no hay barrios sin bandas
    return promedio

def opcion2():
    print("\nIngrese fecha límite para calcular el promedio")
    fechalimite = pedir_fecha()
    with open("Promedio por barrio.txt","w") as filetxt:
        print("Promedio de bandas inscriptas por barrio:\n",file=filetxt)
        for barrio in Barrio.barrios.values():
            promedio = promedio_opcion2(barrio,fechalimite)
            print("El promedio de bandas inscriptas en el barrio",barrio.nombre,"hasta la fecha introducida es",str(promedio),file=filetxt)
    print("\n¡El archivo txt fue creado con éxito!\n")
    return

def asignar_personalidad(genero):
    generos = {"ROCK":"Autoestima baja, creativos, no muy trabajadores, introvertidos y amables","INSTRUMENTAL":"No hay información","INDIE":"Baja autoestima, creativos, poco amables y poco trabajadores","SOLISTA":"No hay información","PUNK":"No hay información","POP":"No hay información","METAL / HEAVY":"Autoestima baja, creativos, no muy trabajadores, introvertidos y amables","SKA / REGGAE":"Vagos, creativos, amables, extrovertidos y alta autoestima","FOLKLORE":"No hay información","JAZZ":"Alta autoestima, creativos, amables y extrovertidos","TROPICAL / LATINO":"No hay información","BLUES":"Alta autoestima, creativos, amables y extrovertidos","HIP HOP / RAP":"Alta autoestima, creativos, amables y extrovertidos","MELODICO":"No hay información","NEW AGE":"No hay información","TANGO":"No hay información","ELECTRO / DANCE":"Creativos, extrovertidos, no demasiado amables","FUNK":"No hay información","PERCUSION":"No hay información"}
    return generos[genero]

def opcion3():
    print("\nPersonalidad según género más tocado por barrio\n")
    for barrio in Barrio.barrios.values():
        print("Barrio:",barrio.nombre)
        print("Genero más tocado:", barrio.maximo)
        personalidad = asignar_personalidad(barrio.maximo)
        print("Personalidad:",personalidad)
        print()
    return

def opcion4():
    try:
        solista = input("\nIngrese nombre del solista: ")
        if solista not in Banda.bandas.keys():
            raise Exception("No existe un solista con ese nombre")
        else:
            print(Banda.bandas[solista])
    except Exception as e:
        print(e)
    return

def mostrarlistaordenada(barriosordenados):
    for barrio in barriosordenados:
        print("Barrio:",barrio.nombre,"-","Cantidad:",str(barrio.cantidad))
        print()
    return

def opcion5():
    barrios = list(Barrio.barrios.values())
    for i in range(len(barrios)-1):
        for j in range(i+1,len(barrios)):
            if barrios[i].cantidad < barrios[j].cantidad:
                aux = barrios[i]
                barrios[i] = barrios[j]
                barrios[j] = aux
    print("\nBarrios ordenados por cantidad de bandas de forma decreciente:\n")
    mostrarlistaordenada(barrios)
    return

def opcion6():
    barrios = list(Barrio.barrios.values())
    for i in range(len(barrios)-1):
        for j in range(i+1,len(barrios)):
            if barrios[i].nombre > barrios[j].nombre:
                aux = barrios[i]
                barrios[i] = barrios[j]
                barrios[j] = aux
    print("\nBarrios y cantidad de bandas ordenados alfabéticamente:\n")
    mostrarlistaordenada(barrios)
    return

def opcion7():
    dicxgenero = Banda.por_genero
    print("\nCantidad de bandas, discos e integrantes por género:\n")
    for genero in dicxgenero.keys():
        print("Género",genero)
        print("   - Cantidad de bandas:",str(dicxgenero[genero][0]))
        print("   - Cantidad de discos:",str(dicxgenero[genero][1]))
        print("   - Cantidad de integrantes:",str(dicxgenero[genero][2]))
        print()
    return

def opcion8():
    dicxgenero = Banda.por_genero
    with open("Promedio de integrantes por banda por genero.txt","w") as filetxt:
        print("Promedio de integrantes por banda por género:\n",file=filetxt)
        for genero in dicxgenero.keys():
            print("Género",genero,file=filetxt)
            print("   - Promedio de integrantes por banda:",str(dicxgenero[genero][3]),file=filetxt)
            print(" ",file=filetxt)
    print("\n¡El archivo txt fue creado con éxito!\n")
    return

def opcion9():
    bandas = list(Banda.bandas.values())
    for i in range(len(bandas)-1):
        for j in range(i+1,len(bandas)):
            if bandas[i].redes < bandas[j].redes:
                aux = bandas[i]
                bandas[i] = bandas[j]
                bandas[j] = aux
    bandas = bandas[0:10]
    nombres = []
    redes = []
    for banda in bandas:
        nombres.append(banda.solista)
        redes.append(banda.redes)

    plt.title(label="Bandas con más presencia en redes",loc='center',color='black',family='Courier New',fontsize=20)
    plt.xlabel("Bandas",family='Courier New',fontsize=15)
    plt.ylabel("Cantidad de redes sociales",family='Courier New',fontsize=15)
    plt.bar(nombres,redes,width=0.5,color="lightskyblue")
    plt.show()
    return

def opcion10():
    with open("Genero mas tocado por barrio.txt","w") as filetxt:
        barrios = Barrio.barrios.values()
        print("Género más tocado por barrio:\n",file=filetxt)
        for barrio in barrios:
            print("Barrio:",barrio.nombre,"-","Género más tocado:",barrio.maximo,file=filetxt)
    print("\n¡El archivo txt fue creado con éxito!\n")
    return

def pediraño():
    años = [14,15,16,17,18]
    seguir = True
    while seguir:
        try:
            print("\n¿Qué año desea seleccionar?\n1. 2014\n2. 2015\n3. 2016\n4. 2017\n5. 2018")
            rta = int(input("\nSeleccione una opción: "))
            if rta not in [1,2,3,4,5]:
                raise Exception("\nOpción no válida\n")
            else:
                seguir = False
        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.')
        except Exception as e:
            print(e)
    año = años[rta-1]
    return año

def generomaximo(lista):
    generos = {"ROCK":0,"INSTRUMENTAL":0,"INDIE":0,"SOLISTA":0,"PUNK":0,"POP":0,"METAL / HEAVY":0,"SKA / REGGAE":0,"FOLKLORE":0,"JAZZ":0,"TROPICAL / LATINO":0,"BLUES":0,"HIP HOP / RAP":0,"MELODICO":0,"NEW AGE":0,"TANGO":0,"ELECTRO / DANCE":0,"FUNK":0,"PERCUSION":0,"Maximo":0}
    maximo = None
    for banda in lista:
        generos[banda.genero] += 1
        if generos[banda.genero] > generos["Maximo"]:
            generos["Maximo"] = generos[banda.genero]
            maximo = banda.genero
    return maximo
    
def opcion11():
    año = pediraño()
    bandasdelaño = list(filter(lambda banda: banda.fecha.year == año,Banda.bandas.values()))
    cantidadxmes = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    generos = {"ROCK":0,"INSTRUMENTAL":0,"INDIE":0,"SOLISTA":0,"PUNK":0,"POP":0,"METAL / HEAVY":0,"SKA / REGGAE":0,"FOLKLORE":0,"JAZZ":0,"TROPICAL / LATINO":0,"BLUES":0,"HIP HOP / RAP":0,"MELODICO":0,"NEW AGE":0,"TANGO":0,"ELECTRO / DANCE":0,"FUNK":0,"PERCUSION":0,"Maximo":0}
    maximo = None
    for banda in bandasdelaño:
        mes = banda.fecha.month
        cantidadxmes[mes] += 1
        generos[banda.genero] += 1
        if generos[banda.genero] > generos["Maximo"]:
            generos["Maximo"] = generos[banda.genero]
            maximo = banda.genero
    print("\n¡Gráfico creado con éxito!\n")
    print("\nEl género más escuchado fue:",maximo,"con un total de",generos["Maximo"],"bandas.\n")
    plt.title(label="Cantidad de bandas inscriptas por mes en el año 20"+str(año),loc='center',color='black',family='Courier New',fontsize=20)
    plt.xlabel("Meses del año",family="Courier New",fontsize=15)
    plt.ylabel("Cantidad de bandas",family='Courier New',fontsize=15)
    plt.bar(["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],cantidadxmes.values(),width=0.5,color="thistle")
    plt.show()
    return

def filtrarBandas():
    seguir = True
    while seguir:
        try:
            print("\nIngrese fecha inferior")
            fecha1 = pedir_fecha()
            print("\nIngrese fecha superior")
            fecha2 = pedir_fecha()
            if fecha2 <= fecha1:
                raise Exception("La fecha superior no puede ser más antigua que la inferior")
            else:
                seguir = False
        except Exception as e:
            print(e)
    bandas = list(filter(lambda banda: banda.fecha >= fecha1 and banda.fecha <= fecha2,Banda.bandas.values()))
    return bandas

def opcion12():
    bandas = filtrarBandas()
    genero_maximo = generomaximo(bandas)
    print("\nEl género más tocado entre las bandas inscriptas en las fechas ingresadas es",genero_maximo)
    return

def opcion13():
    print("\nEstilos por cada género:\n")
    for genero,estilos in Banda.por_genero2.items(): #genero str y estilos set
        if genero != "Maximo":
            print("Género",genero)
            if len(estilos)!= 0:
                for estilo in estilos:
                    print("   -",estilo)
                    print()
            else:
                print("   El género no posee estilos registrados")
                print()
    print("El género con más estilos es",Banda.genero_maximo)
    return

def opcion14():
    print("\nIngrese una fecha límite")
    fecha = pedir_fecha()
    bandas = list(filter(lambda banda: banda.fecha <= fecha,Banda.bandas.values()))
    with open("Bandas con discos.txt","w") as filetxt:
        print("Las bandas que grabaron discos hasta esa fecha son:\n",file=filetxt)
        for banda in bandas:
            if len(banda.discos) != 0:
                print(banda.solista,file=filetxt)
    print("\n¡El archivo txt fue creado con éxito!\n")
    return

        
















