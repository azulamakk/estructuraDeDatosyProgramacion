# Manipular las pilas usando la libreria queue
# importar libreria

from queue import Queue

# Inicializar la pila
stack =Queue(maxsize=0) #No tiene techo

stack.put_nowait('8')
stack.put_nowait('28')
stack.put_nowait('14')

# Visualizar si la pila esta llena
print(stack.full())
stack.put_nowait('8')
stack.put_nowait('28')
stack.put_nowait('14')

print(stack.full())
print("La cantidad de datos que hay son ", stack.qsize())

stack.get()
# Visualizar cantidad de datos de la pila
print("La cantidad de datos que hay son ", stack.qsize())

stack.get()
# Visualizar cantidad de datos de la pila
print("La cantidad de datos que hay son ", stack.qsize())

stack.get()
# Visualizar cantidad de datos de la pila
print("La cantidad de datos que hay son ", stack.qsize())

# Visualizar si la pila esta llena
print(stack.full())

# stack.get_nowait()