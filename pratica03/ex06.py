# Escreva um programa que gere um triângulo de asteriscos, com o tamanho de linhas informado pelo usuário. Por exemplo, para a quantidade de de linhas igual a 6, a saída deverá ser:
# *
# **
# ***
# ****
# *****
# ******

# Observação: a pirâmide só deverá ser gerada se a quantidade de linhas for maior/igual a 2. Caso contrário, informe que não será possível gerar o triângulo.

piramide = int(input("Informe o tamanho da piramide(maior que 1):\n"))
if piramide >=2:
  for i in range(piramide+1):
    print("*" * i)