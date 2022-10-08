# Guardas la data de la pila en otra pila para no perder la informacion

from queue import Queue

# Inicializar la pila
stack=Queue(maxsize=0)
stack1=Queue(maxsize=0)

stack.put_nowait('8')
stack.put_nowait('28')
stack.put_nowait('14')

print("La cantidad de datos que hay son ", stack.qsize())
print("La cantidad de datos que hay son ", stack1.qsize())

# Eliminar elementos de la pila
stack1.put_nowait(stack.get())
print("La cantidad de datos que hay son ", stack.qsize())
print("La cantidad de datos que hay son ", stack1.qsize())

stack1.put_nowait(stack.get())
print("La cantidad de datos que hay son ", stack.qsize())
print("La cantidad de datos que hay son ", stack1.qsize())

print(stack)
print(stack1)
stack=stack1