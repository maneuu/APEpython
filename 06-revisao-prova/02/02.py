linhas = 3
colunas = 3

from random import randint

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input("Valor: ")))
    matriz.append(linha)

print("="*30)
for i in matriz:
    print(i)
print("="*30)

quadro_magico = True
for i in range(linhas):
    soma_linha = sum(matriz[i])
    for j in range(colunas):
        soma_colunas = 0
        for x in range(linhas):
            soma_colunas += matriz[x][j]
        soma_diagonal1 = 0
        for x in range(linhas):
            soma_diagonal1 = matriz[x][x]
        soma_diagonal2 = 0
        a = -1
        for x in range(linhas):
            soma_diagonal2 += matriz[x][a]
            a -= 1
        if not(soma_colunas == soma_linha and soma_linha == soma_diagonal1 and soma_linha == soma_diagonal2):
            quadro_magico == False

if quadro_magico:
    print("Matriz quadro mágico")
else:
    print("Matriz não é quadro mágico")
        