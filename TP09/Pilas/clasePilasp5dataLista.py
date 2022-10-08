
from queue import Queue

# Inicializar la pila
stack=Queue(maxsize=0)
lista=[]

stack.put_nowait('8')
stack.put_nowait('28')
stack.put_nowait('14')

print("La cantidad de datos que hay son ", stack.qsize())
print("La cantidad de datos que hay son ", len(lista))

# Eliminar elementos de la pila
lista.append(stack.get())
print("La cantidad de datos que hay son ", stack.qsize())
print("La cantidad de datos que hay son ", len(lista))

lista.append(stack.get())
print("La cantidad de datos que hay son ", stack.qsize())
print("La cantidad de datos que hay son ", len(lista))

lista.append(stack.get())
print("La cantidad de datos que hay son ", stack.qsize())
print("La cantidad de datos que hay son ", len(lista))

print(stack)
print(lista)