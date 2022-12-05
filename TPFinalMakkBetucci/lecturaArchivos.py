from routers import *
from municipios import *
from conexiones import *
import csv
from geopy.geocoders import Nominatim

#Lectura del csv municipios
with open('TPFinalMakkBetucci/municipios.csv') as csvFile:
    reader=csv.DictReader(csvFile)
    i=0
    for linea in reader:
        try:
            i+=1
            # if linea['municipio_id'] not in Municipio.diccionarioMunicipios.keys():
                #Se crea el objeto Provincia
            lineaProvincia = Provincia(linea['provincia_id'], linea['provincia'])
                #Se crea el objeto Departamento
            lineaDepartamento = Departamento(linea['provincia_id'], linea['provincia'],linea['id_departamento'],linea['departamento'])
                # print('Municipio {} ya fue cargado previamente'.format(linea['municipio_id']))
        except:
            print('Linea {} no pudo ser cargada correctamente'.format(i))

#Lectura del csv routers
with open('TPFinalMakkBetucci/routers.csv') as csvFile:
    geolocator = Nominatim(user_agent="geoapiExercises")
    reader=csv.DictReader(csvFile)
    i=0
    for linea in reader:
        try:
            i+=1
            latitude = linea['latitud']
            longitude = linea['longitud']

            latitude = latitude[:2] + '.' + latitude[2:]
            longitude = longitude[:2] + '.' + longitude[2:]

            location = geolocator.reverse(latitude+","+longitude)

            address = location.raw['address']
            municipio = address.get('county', '')   
            departamento = address.get('state_district', '')
            provincia = address.get('state', '')   
            
            #Se crea el objeto Municipio
            if linea['municipio_id'] not in Municipio.diccionarioMunicipios.keys():
                lineaMunicipio = Municipio(linea['provincia_id'], provincia,linea['id_departamento'],departamento,
                    linea['municipio_id'], municipio)
            #Se crea el objeto Router
            if linea['id'] not in Router.diccionarioRouter.keys():
                linea = Router(linea['id'], linea['identificador'],linea['ubicacion'],linea['latitud'],linea['longitud'],
                    linea['longitud'], linea['municipio_id'], linea['provincia_id'], linea['id_departamento'])
            else:
                print('Router {} ya fue cargado previamente'.format(linea['id']))
        except:
            print('Linea {} no pudo ser cargada correctamente'.format(i))

#Lectura del csv conexiones y carga de conexiones al diccionario de conexiones y a los routers
with open('TPFinalMakkBetucci/conexiones.csv') as csvFile:
    reader=csv.DictReader(csvFile)
    i=0
    for linea in reader:
        try:
            i+=1        
            if linea['Direccion IP'] not in Conexion.conexionIDRegistrados.keys():
                conexion = Conexion(linea['Direccion IP'],linea['MAC Address'],linea['Fecha'],linea['Hora'],linea['Activa'])
            else:
                print('Conexion {} ya fue cargada previamente'.format(linea['Direccion IP']))
        except:
            print('Linea {} no pudo ser cargada correctamente'.format(i))