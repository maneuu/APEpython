# Considere uma sequência numérica em que o primeiro termo é o número 4. A cada
# termo, a partir do segundo, multiplica-se o anterior por 5 e soma-se 1. Escreva um
# programa que gere os 20° termos dessa sequência.

anterior = 4
print(anterior)
for i in range(19):
  anterior = anterior*5+1
  print(anterior)
