cadena = "zyxbcde"

cad = cadena[:len(cadena)//2+1]
ena = cadena[len(cadena)//2:]

cad_sorted = sorted(cad)
cad_sorted.reverse()
cad_sorted = "".join(cad_sorted)
ena_sorted = "".join(sorted(ena))

if cad_sorted == cad and ena_sorted == ena:
    print("Es bitonica")
else:
    print("No es bitonica")