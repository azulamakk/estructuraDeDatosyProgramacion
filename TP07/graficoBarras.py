from opcode import hasjabs
import matplotlib.pyplot as plt

habitantes=[671280, 447287, 94782, 8611122, 591630]
ciudades=['Bristol', 'Cardiff', 'Bath', 'Liverpool', 'Glasgow']

plt.title(label="Grafico habitantes por ciudad", fontsize=20, color='blue')
plt.xlabel('Ciudades')
plt.ylabel('Poblacion')

plt.bar(ciudades, habitantes, color='green', width=0.5)
plt.show()