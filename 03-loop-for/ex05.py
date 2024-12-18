# Faça um programa que gere a tabuada de 1 a 10. Mostre a tabuada na forma:
# 1 x 1 = 1
# 1 x 2 = 2

num = int(input("Valor: "))
for i in range(1,11):
  resultado = num * i
  print(f"{num} x {i} = {resultado}")