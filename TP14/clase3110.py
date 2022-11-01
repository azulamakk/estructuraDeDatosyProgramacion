lista1=['Un', 'dia', 'lindo']

file1=open('myfile.txt', 'w')
file1.writelines(lista1)
file1.close()

file1=open('myfile.txt', 'r')
texto =file1.readline()
for linea in file1.readlines():
    print(linea, end=' ')