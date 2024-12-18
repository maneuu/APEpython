# valor1 = float(input('1º valor: '))
# valor2 = float(input('2º valor: '))
# valor3 = float(input('3º valor: '))
# valor4 = float(input('4º valor: '))
# valor5 = float(input('5º valor: '))
# valor6 = float(input('6º valor: '))

# media = (valor1 + valor2 + valor3 + valor4 + valor5 + valor6)/6
# print(f'Média = {media:.2f}')


soma = 0

for i in range(6):
  n = int(input('Informe o valor: '))
  soma += n
media = soma/6
print(f'Média = {media:.2f}')