# Escriba una función que dada una lista de tuplas elimine de la lista todas las tuplas vacías.

listaDeTuplas=[('xyz'), (), (1234, 'abcd'), (), (30)]
print(listaDeTuplas)
listaTuplasNoVacias=[]

def estaVacia(tupla):
    if tupla == ():
        return True
    else:
        return False

tuplaPrueba=()
print(estaVacia(tuplaPrueba))

for i in range(len(listaDeTuplas)):
    if estaVacia(listaDeTuplas[i])==False:
        listaTuplasNoVacias.append(listaDeTuplas[i])

listaDeTuplas=tuple(listaTuplasNoVacias)
print(listaDeTuplas)

