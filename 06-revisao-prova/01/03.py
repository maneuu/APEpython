matriz = []

from random import randint

linhas = 4
colunas = 4

matriz = [[randint(1,10) for j in range(colunas)] for i in range(linhas)]
for i in matriz:
        print(i)
print("="*10)
vetor_diagonal_1 = []
vetor_diagonal_2 = []

j = 0
for i in range(linhas):
        vetor_diagonal_1.append(matriz[i][j])
        j += 1
j = -1
for i in range(linhas):
        vetor_diagonal_2.append(matriz[i][j])
        j -= 1
print(vetor_diagonal_1)
print(vetor_diagonal_2)