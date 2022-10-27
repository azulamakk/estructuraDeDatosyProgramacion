# Listas simple comportamiento de una pila
# LIFO --> Ultimo que entra es el primero que sale

lista=[]

# Agregar elementos listas / pila

lista.append(8)
lista.append(28)
lista.append(14)

print(lista)

# # Eliminar los elementos de la pila

# print(lista.pop())
# print(lista)

# print(lista.pop())
# print(lista)

# print(lista.pop())
# print(lista)

# print(lista.pop())
# print(lista)

# **********OTRO EJEMPLO**********
pilaaux=[]
pilaaux.append(lista.pop())
print(pilaaux)

pilaaux.append(lista.pop())
print(pilaaux)

pilaaux.append(lista.pop())
print(pilaaux)
print(lista)

pilaaux.reverse()
print(pilaaux)
lista=pilaaux
print(lista)