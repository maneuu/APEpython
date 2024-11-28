# Faça um programa que mostre todos os números primos de 1 a N (obs: N será lido).
num_input = int(input("Digite um valor: "))

for num in range(2, num_input + 1):
    num_primo = True  # Presume que o número é primo

    for i in range(2, num): # Um número primo é aquele que é dividido apenas por um e por ele mesmo
        if num % i == 0: # Se o número passa na condição o número não é primo
            num_primo = False
            print(f"O número {num} não é primo")  
            break 

    if num_primo:
        print(f"O número {num} é primo")  # Número é primo
