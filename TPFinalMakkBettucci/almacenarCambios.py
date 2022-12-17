from ventanasSecundarias.opcion1 import *
from municipios import *
from routers import *
import csv

pathMuni = "FinalMakkBettucci/municipios.csv"
def actualizarArchivoMuni(pathMuni):
    with open(pathMuni, "w") as archivo:
        writer = csv.writer(archivo, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['municipio_id','provincia_id','id_departamento','municipio','provincia','departamento'])
        for provId in Provincia.diccionarioProv:
            prov = Provincia.diccionarioProv[provId]
            for dptoId in prov.diccionarioDptos:
                dpto = prov.diccionarioDptos[dptoId]
                for municipioId in dpto.diccionarioMunicipios:
                    municipio = dpto.diccionarioMunicipios[municipioId]
                    writer.writerow([municipio.municipioID, prov.provinciaID, dpto.departamentoID, municipio.municipio, prov.provincia, dpto.departamento])
    print("Archivo de municipios actualizado")
    
pathRouter = "FinalMakkBettucci/routers.csv"
def actualizarArchivoRouters(pathRouter):
    with open(pathRouter, "w") as archivo:
        writer = csv.writer(archivo, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['id','identificador','ubicacion','latitud','longitud','municipio_id','provincia_id','id_departamento'])
        for routerId in Router.diccionarioRouter:
            router = Router.diccionarioRouter[routerId]
            writer.writerow([router.id, router.identificador, router.ubicacion, router.latitud, router.longitud, router.municipioID, router.provinciaID, router.departamentoID])
    print("Archivo de routers actualizado")

pathConexiones = "FinalMakkBettucci/conexiones.csv"
def actualizarArchivoConexiones(pathConexiones):
    with open(pathConexiones, "w") as archivo:
        writer = csv.writer(archivo, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Router ID','MAC Address','Fecha','Horario','Activa','Direccion IP'])
        
        nodoActual = Conexion.conexionesHistoricas.head
        
        while nodoActual != None:
            conexion = nodoActual.valor
            fecha, hora = conexion.fechaYHora.strftime("%d/%m/%Y %H:%M:%S").split(" ")
            writer.writerow([conexion.routerID, conexion.direccionMAC, fecha, hora, conexion.activa, conexion.direccionIP])
              
            nodoActual = nodoActual.prox

        # for conexion in Conexion.conexionesHistoricas:
        #     router = Conexion.conexionesHistoricas[conexion]
        #     for conexionId in router.conexiones:
        #         conexion = router.conexiones[conexionId]
        #         fecha, hora = conexion.fechaYHora.strftime("%d/%m/%Y %H:%M:%S").split(" ")
        #         writer.writerow([conexion.routerID, conexion.direccionMAC, fecha, hora, conexion.activa, conexion.direccionIP])
    print("Archivo de conexiones actualizado")