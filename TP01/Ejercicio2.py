'Hacer una función que reciba una lista de campos, una lista con datos y dos valores inicio y fin.'
'La función deberá armar fichas que muestren el nombre del campo con los datos a continuación,'
'para los elementos de la lista de datos comprendidos entre inicio y fin.'
'Para comprobar que la función funciona correctamente debe asegurarse que, en la lista de datos,'
'los datosestán bien formados. Esto significa que por cada elemento hay tantos datos como campos hay en la lista decampos. '
'La función tiene que validar que inicio y fin sean valores correctos. '
'Es decir, inicio debe estar antes que finy ambos ser valores de índices dentro de la lista'

listaCampos = ["LEGAJO", "MAIL", "APELLIDO", "NOMBRE"]

listaDatos = [
    ["10001", "ndelgado@itba.edu.ar", "Delgado", "Ninfa"],
    ["10123", "pperez@itba.edu.ar", "Perez", "Patricia"],
    ["15111", "aalvar@itba.edu.ar", "Alvarez", "Adriana"],
    ["18145", "pgarcia@itba.edu.ar", "Garcia", "Pedro"],
    ["15435", "gmagal@itba.edu.ar", "Magallanes", "Gustavo"]
]

def mostrarFichas(desde, hasta):
    if desde < 0 or desde > len(listaDatos) or hasta < 0 or hasta > len(listaDatos) or desde > hasta:
        print("Nada que ver")
        exit()
    else:
        while desde <= hasta:
            n = 0
            campo = ""
            while n < len(listaCampos[0]):
                campo = str(listaCampos[n]) + ": " + str(listaDatos[desde][n]) + " " + campo
            print(campo)
            desde += 1

try:
    mostrarFichas(int(input("¿Desde qué ficha?: ")), int(input("¿Hasta qué ficha?: ")))
except ValueError:
    print("Ingresar un valor válido por favor")
    exit()