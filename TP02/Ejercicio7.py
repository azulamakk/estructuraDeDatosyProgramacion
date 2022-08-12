#Realizar una función que, dada una lista palabras y dos palabras, 
# encuentre la distancia mínima entre laspalabras dadas dentro de la lista.

def calculadorDistanciaPalabras(Palabras, primeraPalabra, segundaPalabra):
    
    posicionPrimeraPalabra = Palabras.index(primeraPalabra)
    posicionSegundaPalabra = Palabras.index(segundaPalabra)
    distancia=posicionSegundaPalabra-posicionPrimeraPalabra
    print("La distancia minima entre "+ primeraPalabra + " y " +segundaPalabra+" es: "+str(distancia))

Palabras=["La","materia","Estructuras","de","Datos","es","genial"]

primeraPalabra="La"
segundaPalabra="es"

calculadorDistanciaPalabras(Palabras, primeraPalabra, segundaPalabra)
