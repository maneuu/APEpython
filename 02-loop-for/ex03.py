multiplo = int(input("Valor do mútiplo: "))
inicio = int(input('Começa no número : '))
final = int(input('Termina no número : '))
for i in range(inicio, final+1):
  if i % multiplo == 0:
    print(f'{i}', end=' ')  
