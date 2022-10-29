#ABRIR UN ARCHIVO EXISTENTE EN MI MAQUINA

from io import UnsupportedOperation


def existe(patharchivo):
    try:
        archivo=open(patharchivo,'r')
        archivo.write("Hola como estas")
        return archivo
    except FileNotFoundError:
        return None
    except UnsupportedOperation:
        print("El archivo esta tratando de realizar una tarea no permitida")
    

if __name__=="__main__":
    patharchivo="C:/Users/NINFA ESPERANZA/OneDrive/Documentos/codigofacilito/pedidos.txt"
    manejararchivo=existe(patharchivo)
    if manejararchivo!= None:
        print("Archivo Existe")
        for linea in manejararchivo:
            print(linea)
    else:
        print("El archivo no existe")