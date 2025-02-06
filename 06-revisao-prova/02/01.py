linhas = 5
colunas = 5

from random import randint

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

print("="*30)
for i in matriz:
    print(i)
print("="*30)