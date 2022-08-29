
import numpy as np 

# Crear vector
vector=np.array(1,2,3,5)
print(vector)

# Crear matrices
matriz=np.array([(1,2,3), (4,5,6)])
print(matriz)

for fila in matriz:
    print(fila)

# Empty
matrizAleatoria=np.empty([2,2])
print(matrizAleatoria)

matrizAleatoria=np.empty([2,2], dtype=int)
print(matrizAleatoria)

vectorleatorio=np.empty(5)
print(vectorleatorio)

# Generar matriz de ceros
matricesCeros = np.zeros([2,3], dtype=int)
print(matricesCeros)

vectorUnos=np.ones(4)
print(vectorUnos)

# Arrange
matriz1 = np.arrange(0,4,2)
print(matriz1)

# Reshape (dimensiones)
matriz1 = np.arrange(4).reshape(2,2)
print(matriz1)

# Sort
matriz1=np.arange(0,4)
print(matriz1)
matriz1.sort()
