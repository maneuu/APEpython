valor = int(input())
lista_a = []
from random import randint
for _ in range(valor):
    lista_a.append(randint(1, 10))
lista_b = []
for i in range(valor):
    if lista_a[i] % 2 == 0:
        lista_b.append(0)
    else:
        lista_b.append(1)
        
print(lista_a)
print(lista_b)