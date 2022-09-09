#Utilice funciones built-in del caso, dada una lista de nombres haga una lista donde 
# almacena la cantidad deletras ‘a’ o ‘A’ que hay en cada nombre de la lista 

lista=["Ana", "Tomas"]

print(list(map(lambda dato: dato.lower().count("a"), lista)))