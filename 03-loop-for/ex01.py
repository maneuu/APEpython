# Faça um programa que calcule e mostre o fatorial de um número N, fornecido  pelo usuário.
num = int(input("Valor:"))
result= 1
for i in range(1,num + 1):
  result *= i
  print(result)
print(result)
