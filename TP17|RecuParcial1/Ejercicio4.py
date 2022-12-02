
A = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]

# Primero chequeamos que sea cuadrada
def esCuadrada(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    if filas != columnas:
        print('No es cuadrada')
        return False
    else:
        print('Es cuadrada')
        return True

def esTriangularSuperior(matriz):
    trianularSuperior=True
    for i in range(1, len(matriz)):
        for j in range(0, i):
            if(matriz[i][j] != 0):
                trianularSuperior=False
    if trianularSuperior == True:
        print('Es triangular superior')
    else: 
        print('No es triangular superior')
    return trianularSuperior
if esCuadrada(A):
    esTriangularSuperior(A)
else:
    exit()

