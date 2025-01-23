from random import randint

lista = []
for _ in range(10):
    lista.append(randint(1,5))
print("Lista:", lista)

repete = []
frequencia = []

# Conta as repetições
for i in lista:
    count = 0
    for j in lista:
        if i == j:
            count += 1
    if count > 1 and i not in repete:
        repete.append(i)
        frequencia.append(count)
print("Numeros repetidos:", repete)
print("Frequencia dos números repetidos:",frequencia)
# Encontra a maior frequência
maior = -1
for num in frequencia:
    if num > maior:
        maior = num

# Coleta os números com maior frequência
resultado = []
for i in range(len(frequencia)):
    if frequencia[i] == maior:
        resultado.append(repete[i])

print("Número(s) que mais se repete(m):", resultado)