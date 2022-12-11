from ventanasSecundarias.opcion1 import *
from municipios import *
from routers import *
import csv

pathMuni = "FinalMakkBettucci/municipios.csv"
def actualizarArchivoMuni(pathMuni):
    with open(pathMuni, "w") as archivo:
        writer = csv.writer(archivo, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow('municipio_id','provincia_id','id_departamento','municipio','provincia','departamento')
        for prov in Provincia.diccionarioProv:
            for dpto in prov.diccionarioDptos:
                for municipio in dpto.diccionarioMunicipios:
                    writer.writerow(municipio.municipioID, prov.provinciaID, dpto.departamentoID, municipio.municipio, prov.provincia, dpto.departamento)

pathRouter = "FinalMakkBettucci/routers.csv"
def actualizarArchivoRouters(pathRouter):
    with open(pathRouter, "w") as archivo:
        writer = csv.writer(archivo, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow('id','identificador','ubicacion','latitud','longitud','municipio_id','provincia_id','id_departamento')
        for router in Router.diccionarioRouters:
            writer.writerow(router.id, router.identificador, router.ubicacion, router.latitud, router.longitud, router.municipioID, router.provinciaID, router.departamentoID)

pathConexiones = "FinalMakkBettucci/conexiones.csv"
def actualizarArchivoConexiones(pathConexiones):
    with open(pathConexiones, "w") as archivo:
        writer = csv.writer(archivo, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow('Router ID','MAC Address','Fecha','Horario','Activa','Direccion IP')
        for router in Router.diccionarioRouters:
            for conexion in router.conexiones:
                writer.writerow(conexion.direccionIP, conexion.direccionMAC, conexion.fecha, conexion.hora, conexion.activa, conexion.routerID)
