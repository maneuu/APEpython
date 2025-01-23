from random import randint

# Gera lista com números únicos de 1 a 6
lista = []
while True:
    numero = randint(1, 6)
    if numero not in lista:
        lista.append(numero)
    if len(lista) == 6:
        break

print("Lista original:", lista)

# Ordenação manual sem funções (apenas loops e append)
ordenada = []
copia = []  # Cria uma cópia manual da lista original
for num in lista:
    copia.append(num)

# Algoritmo de ordenação simplificado
while len(copia) > 0:
    # Encontra o menor número manualmente
    menor_valor = copia[0]
    posicao_menor = 0
    for i in range(len(copia)):
        if copia[i] < menor_valor:
            menor_valor = copia[i]
            posicao_menor = i
    
    # Remove o menor valor da cópia e adiciona à lista ordenada
    ordenada.append(menor_valor)
    nova_copia = []
    for i in range(len(copia)):
        if i != posicao_menor:
            nova_copia.append(copia[i])
    copia = nova_copia

print("Lista ordenada:", ordenada)