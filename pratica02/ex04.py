valor03 = int(input("Valor do mútiplo: "))
valor01 = int(input('Começa no número : '))
valor02 = int(input('Termina no número : '))

n_numeros = 0

for i in range(valor01, valor02+1):
  if i % valor03 == 0:
    n_numeros += 1
print(n_numeros)