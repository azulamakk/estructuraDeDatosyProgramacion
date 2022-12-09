from routers import *
from municipios import *
from conexiones import *
import csv
from geopy.geocoders import Nominatim
import json



#Lectura del csv municipios
def cargarProvinciasyDptos(pathMunicipios):
    prefijos_json = {}
    with open('TPFinalMakkBetucci/prefijos.json') as json_file:
        prefijos_json = json.load(json_file)
    with open(pathMunicipios, encoding= 'unicode_escape') as csvFile:
        reader=csv.DictReader(csvFile)
        i=0
        for linea in reader:
            try:
                i+=1

                #Se crea el objeto Provincia
                Provincia(linea['provincia_id'], linea['provincia'])

                #Se crea el objeto Departamento
                Departamento(linea['provincia_id'], linea['provincia'],linea['id_departamento'], linea['departamento'])

                #Se crea el objeto Municipio
                prefijo = prefijos_json[linea['provincia_id']]
                if linea['municipio_id'] != '' and linea['municipio_id'][:3] == prefijo:
                    Municipio(linea['provincia_id'], linea['provincia'], linea['id_departamento'], linea['departamento'], linea['municipio_id'], linea['municipio'])
            except:
                print('Linea {} no pudo ser cargada correctamente'.format(i))


listaMunicipios = []
cargarProvinciasyDptos('TPFinalMakkBetucci/municipios.csv')



def leerArchivoRouter(pathRouters):
    #Lectura del csv routers
    with open(pathRouters, encoding='unicode_escape') as csvFile:
        geolocator = Nominatim(user_agent="geoapiExercises")
        reader=csv.DictReader(csvFile, delimiter=';')
        i=0
        for linea in reader:
            try:
                i+=1

                if linea['provincia_id'] not in Provincia.diccionarioProv:
                    raise Exception("Provincia no registrada")
                
                prov = Provincia.diccionarioProv[linea['provincia_id']]
                if linea['id_departamento'] not in prov.diccionarioDptos:
                    raise Exception("Departamento no registrado")
                
                depto = prov.diccionarioDptos[linea['id_departamento']]

                if linea['municipio_id'] not in depto.diccionarioMunicipios:
                    latitude = int(linea['latitud'].replace('.',''))
                    longitude = int(linea['longitud'].replace('.', ''))
                    if latitude == 0 and longitude == 0:
                        # raise Exception("Coordenadas invalidas")
                        municipio = ''
                    else:
                        latitude = str(latitude / 1_000_000)
                        longitude = str(longitude / 1_000_000)

                        # location = geolocator.reverse(latitude+","+longitude)

                        # address = location.raw['address']
                        # municipio = address.get('county', '')  
                        municipio = ''
                    #Se crea el objeto Municipio

                    Municipio(linea['provincia_id'], prov.provincia, linea['id_departamento'], depto.departamento,
                        linea['municipio_id'], municipio)

                    # listaMunicipios.append(linea)
                if linea['id'] not in Router.diccionarioRouter.keys():
                    Router(linea['id'], linea['identificador'],linea['ubicacion'],linea['latitud'],linea['longitud'],
                        linea['municipio_id'], linea['provincia_id'], linea['id_departamento'])
                else:
                    print('Router {} ya fue cargado previamente'.format(linea['id']))
            except Exception as e:
                print(e)
                print('Linea {} no pudo ser cargada correctamente'.format(i))

# leerArchivoRouter('TPFinalMakkBetucci/routers.csv')
def leerArchivoConexiones(pathConexiones):
    #Lectura del csv conexiones y carga de conexiones al diccionario de conexiones y a los routers
    with open(pathConexiones, encoding='utf-8-sig') as csvFile:
        reader=csv.DictReader(csvFile, delimiter=';')
        i=0
        for linea in reader:
            try:
                i+=1        
                conexion = Conexion(linea['Direccion IP'],linea['MAC Address'],linea['Fecha'],linea['Horario'],linea['Activa'],linea['Direccion IP'])
                if linea['Direccion IP'] in Router.diccionarioRouter and linea['Activa'] == '1':
                    router = Router.diccionarioRouter[linea['Direccion IP']]
                    if conexion.direccionMAC not in router.conexiones:
                        router.conexiones[conexion.direccionMAC] = conexion
                    else:
                        print('Conexion {} ya fue cargada previamente'.format(conexion.direccionMAC))
            except Exception as e:
                print(e)
                print('Linea {} no pudo ser cargada correctamente'.format(i))

leerArchivoRouter('TPFinalMakkBetucci/routers.csv')
leerArchivoConexiones('TPFinalMakkBetucci/conexiones.csv')

print(Conexion.conexionesHistoricas)