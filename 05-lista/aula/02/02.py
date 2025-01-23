lista = []

from random import randint
for _ in range(100):
    lista.append(randint(1,60))
    

for item in lista:
    count = 0

    for i in lista:
        if item == i:
            count += 1
    if count == 1:
        print(item)