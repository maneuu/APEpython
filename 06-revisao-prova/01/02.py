matriz = []

from random import randint

linhas = 5
colunas = 10

matriz = [[randint(1,10) for j in range(colunas)] for i in range(linhas)]
valor_k = int(input())

for i in matriz:
    print(i)

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == valor_k:
            print("=" * 50)
            print(f"Linha = {i}")
            print(f"Coluna = {j}")