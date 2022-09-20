import matplotlib.pyplot as plt

a=[1,2,3,4]
b=[11,22,33,44]
c=[2,4,6,8]
d=[24,20,18,21]


plt.title("Grafica Linea")
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.plot(a, b, color='green', linewidth=3, label='Porcentajes')
plt.plot(c, d, color='red', linewidth=3, label='Porcentajes')


plt.show()