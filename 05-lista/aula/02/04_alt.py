from random import randint

# 1. Criar lista com 100 números aleatórios
numeros = []
for _ in range(100):
    numeros.append(randint(1, 20))

# 2. Contar quantas vezes cada número aparece
contagem = [0] * 20  # Uma posição para cada número de 1 a 20

for num in numeros:
    # A posição 0 guarda quantas vezes o número 1 apareceu
    # A posição 1 guarda quantas vezes o número 2 apareceu, etc
    contagem[num - 1] += 1

# 3. Descobrir qual foi a maior contagem
maior_contagem = 0
for qtd in contagem:
    if qtd > maior_contagem:
        maior_contagem = qtd

# 4. Descobrir quais números tiveram a maior contagem
resultado = []
for posicao in range(len(contagem)):
    if contagem[posicao] == maior_contagem:
        # A posição 0 corresponde ao número 1, posição 1 ao número 2, etc
        numero = posicao + 1
        resultado.append(numero)

# 5. Mostrar o resultado
print("Número(s) que mais apareceu(ram):", resultado)