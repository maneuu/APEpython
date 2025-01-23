lista = []
from random import randint
while True:
    numero = randint(1,60)
    if numero not in lista:
        lista.append(numero)
    if len(lista) == 6: break


for i in lista:
    print(i)