# Faça um programa que leia um número inteiro N, calcule e mostre o maior  quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o  resultado é 36.
calculo = 0 
num = int(input("Valor: ")) 
for i in range(1,num + 1):
  calculo = (i ** 2)
  if calculo > num:
    break
  valor_final = calculo
print(f"O maior quadrado perfeito menor ou igual ao valor {num} é {valor_final}.")