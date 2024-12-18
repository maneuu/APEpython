# Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele  próprio. Faça um programa que leia um número e determine se ele é ou não  primo. 
check = 1
num = int(input("Valor: "))
for i in range(2,num):
  check = num % i
  if check == 0:
    break

if check == 0:
  print(f"O número {num} não é número primo.")
else: 
  print(f"O número {num} é número primo.")
