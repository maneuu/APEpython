'''Write a Python program to flatten a shallow list

Sample Output

[[20,30,70],[30,90,10], [30,20], [70,90,10,80]]

[20, 30, 70, 30, 90, 10, 30, 20, 70, 90, 10, 80]
'''
lista = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
print(f'Lista original: {lista}')
lista2 = []
for i in lista:
    for j in i:
        lista2.append(j)
print(f'Lista transformada: {lista2}')