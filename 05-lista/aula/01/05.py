from random import randint

nomes = []
while True:
    nome = input("Nome  >> ")
    if nome == '':
        
        break
    nomes.append(nome)

print('Nomes lidos:')
print(nomes)
print("\n===================================\n")

# trocando valores aleatórios
for i in range(6):
    while True:
        i = randint(0, len(nomes)-1)
        j = randint(0, len(nomes)-1)
        if i != j:
            break
    aux = nomes[i]
    nomes[i] = nomes[j]
    nomes[j] = aux

print("Lista aleatoriamente alterada:")

print(nomes)
