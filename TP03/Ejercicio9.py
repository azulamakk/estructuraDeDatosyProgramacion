lista=[1,2,-3, 4, 6, -10]
negativos=filter(lambda dato:dato if dato<0 else '', lista)
print(list(negativos))