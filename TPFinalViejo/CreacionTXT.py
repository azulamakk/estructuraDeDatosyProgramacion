import csv

with open("Proyecto Final/bandas-inscriptas.csv") as file_csv:
    reader = csv.reader(file_csv,delimiter = ";")
    with open("Proyecto Final/bandas-inscriptas.txt","w") as file_txt:
        for row in reader:
            texto = ""
            for elemento in row:
                if len(elemento) != 0:
                    if elemento[-1] == " ":
                        elemento = elemento[0:len(elemento)-1]
                texto += elemento+";"
            print(texto,file=file_txt)