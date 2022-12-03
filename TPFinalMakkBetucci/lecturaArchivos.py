from routers import *
from municipios import *
from conexiones import *
import csv

listaMunicipios = []
listaDepartamentos = []

with open('TPFinalMakkBetucci/municipios.csv') as csvFile:
    reader=csv.DictReader(csvFile)
    i=0
    for linea in reader:
        try:
            i+=1
            if linea['municipio_id'] not in Municipio.municipioIDRegistrados:
                Municipio.municipioIDRegistrados.add(linea['municipio_id'])
                linea = Municipio(linea['provincia_id'], linea['provincia'],linea['id_departamento'],linea['departamento'],
                    linea['municipio_id'],linea['municipio'])
                listaMunicipios.append(linea)
            else:
                print('Municipio {} ya fue cargado previamente'.format(linea['municipio_id']))
            
            if linea['id_departamento'] not in Depantamento.departamentoIDRegistrados:
                Depantamento.departamentoIDRegistrados.add(linea['departamento_id'])
            
            if linea['provincia_id'] not in Provincia.provinciaIDRegistrados:
                Provincia.provinciaIDRegistrados.add(linea['provincia_id'])
        except:
            print('Linea {} no pudo ser cargada correctamente'.format(i))

listaRouters = []
with open('TPFinalMakkBetucci/routers.csv') as csvFile:
    reader=csv.DictReader(csvFile)
    i=0
    for linea in reader:
        try:
            i+=1        
            if linea['id'] not in Router.routerIDRegistrados:
                Router.routerIDRegistrados.add(linea['id'])
                linea = Router(linea['id'], linea['identificador'],linea['ubicacion'],linea['latitud'],linea['longitud'],
                    linea['longitud'], linea['municipio_id'], linea['provincia_id'], linea['id_departamento'])
                listaRouters.append(linea)
            else:
                print('Router {} ya fue cargado previamente'.format(linea['id']))
        except:
            print('Linea {} no pudo ser cargada correctamente'.format(i))


def leerArchivoRouters():
    return
    # archivo = open("routers.csv", "r")
    # listaRouters = []
    # for linea in archivo:
    #     linea = linea.strip()
    #     linea = linea.split(",")
    #     listaRouters.append(linea)
    # archivo.close()
    # return listaRouters