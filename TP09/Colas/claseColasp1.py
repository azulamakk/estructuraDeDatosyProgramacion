# Importar la libreria collections
from collections import deque

# Crear el objeto Cola
deques=deque()

# Visualizar el objeto Cola - Cola esta vacia
print(deques)

# Agregar elemnentos a la cola
deques.append(8)
print(deques)

deques.append(81)
print(deques)

deques.append(881)
print(deques)

deques.append(1881)
print(deques)

# Atender los elementos de la cola
deques.popleft()
print(deques)