#Utilice funciones built-in del caso que, dada una lista de enteros arme dos listas distintas, una para lospares y una para los impares. 
# Luego, ambas listas deben unirse en una lista final que posea primero losnúmeros pares y luego los impares
import builtins

lista1=[1,2,3,4]
lista2=[2,3,4,5]

lista1.extend(lista2)

print(sorted(lista1))