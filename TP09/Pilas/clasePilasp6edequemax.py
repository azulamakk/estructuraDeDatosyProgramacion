from collections import deque

stack=deque(maxlen=None)
stack1=deque()

# Agregar elemento a la pila

stack.append(3)
print(stack)

stack.append(33)
print(stack)

stack.append(333)
print(stack)

stack.append(444)
print(stack)

stack1.append(stack.pop())
print(stack)
print(stack1)

stack1.append(stack.pop())
print(stack)
print(stack1)

stack1.append(stack.pop())
print(stack)
print(stack1)

print('Lista original ', len(stack))
print('Lista copia de la original ', len(stack1))