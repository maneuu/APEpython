# Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a seguinte soma:  
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
result = 0
num = int(input("Valor: "))
for i in range(1,num + 1):
  result += 1/i
print(f"O resultado final é: {result:.2f}")