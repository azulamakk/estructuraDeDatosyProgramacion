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

listaMunicpios = []
#Lectura del csv routers
with open('TPFinalMakkBetucci/routers.csv', encoding= 'unicode_escape') as csvFile:
    geolocator = Nominatim(user_agent="geoapiExercises")
    reader=csv.DictReader(csvFile)
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
                    raise Exception("Coordenadas invalidas")
                latitude = str(latitude / 1_000_000)
                longitude = str(longitude / 1_000_000)

                location = geolocator.reverse(latitude+","+longitude)

                address = location.raw['address']
                municipio = address.get('county', '')   
                departamento = address.get('state_district', '')
                provincia = address.get('state', '')

                #Se crea el objeto Municipio
                lineaMunicipio = Municipio(linea['provincia_id'], provincia, linea['id_departamento'], departamento,
                    linea['municipio_id'], municipio)
                listaMunicpios.append(lineaMunicipio)
            if linea['id'] not in Router.diccionarioRouter.keys():
                linea = Router(linea['id'], linea['identificador'],linea['ubicacion'],linea['latitud'],linea['longitud'],
                    linea['municipio_id'], linea['provincia_id'], linea['id_departamento'])
            else:
                print('Router {} ya fue cargado previamente'.format(linea['id']))
        except Exception as e:
            print(e)
            print('Linea {} no pudo ser cargada correctamente'.format(i))
for muni in listaMunicpios:
    print(muni)
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