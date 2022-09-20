from matplotlib import pyplot as plt

lenguajes=['C', 'C++', 'Java', 'Python']
usuarios=[50,30,70,120]

plt.pie(usuarios, labels=lenguajes, autopct='%.2f%%')
plt.title(label='Preferencia actual lenguajes Programacion',
    loc='center',
    color='black')

plt.show()