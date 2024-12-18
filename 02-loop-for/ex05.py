#Um estudante encontrou um livro contendo as medidas (três lados) de 06 (seis)
# pirâmides do Egito. Escreva um programa para ler essas medidas. Seu programa deverá
# calcular e exibir quantas medidas são válidas para uma pirâmide, considerando a Condição
# de Existência de um Triângulo.
cont = 0
for i in range(6):
  print(f'\n{i + 1}º pirâmide')
  a = int(input('Valor 1: '))
  b = int(input('Valor 2: '))
  c = int(input('Valor 3: '))
  if a < b + c and b < a + c and c < a + b :
    cont += 1
print(f'\nQuantidade de pirâmides validas: {cont}')