ordem = int(input("Ordem da matriz: "))

# Lendo a matriz
matriz = []
for i in range(ordem):
    linha = [int(input(f"Valor ({i+1})({j+1}): ")) for j in range(ordem)]
    matriz.append(linha)

# Definindo a soma mágica como a soma da primeira linha
soma_magica = sum(matriz[0])

# Calculando a soma das diagonais
soma_diagonal1 = 0
soma_diagonal2 = 0
for i in range(ordem):
    soma_diagonal1 += matriz[i][i]
    soma_diagonal2 += matriz[i][ordem-1-i]

# Verificando as somas das linhas e colunas
linhas_validas = True
colunas_validas = True

for i in range(ordem):
    soma_linha = sum(matriz[i])
    soma_coluna = sum(matriz[j][i] for j in range(ordem))

    if soma_linha != soma_magica:
        linhas_validas = False
        break

    if soma_coluna != soma_magica:
        colunas_validas = False
        break

# O quadrado é mágico se todas as somas forem iguais
quadrado_magico = linhas_validas and colunas_validas and (soma_diagonal1 == soma_magica) and (soma_diagonal2 == soma_magica)

print("Matriz é um quadrado mágico" if quadrado_magico else "Matriz não é um quadrado mágico")

# Exibindo a matriz
print("=" * 30)
for linha in matriz:
    print(linha)
print("=" * 30)