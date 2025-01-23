import random 

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
while True:
    i = random.randint(0, len(nomes)-1)
    j = random.randint(0, len(nomes)-1)
    if i != j:
        break
aux = nomes[i]
nomes[i] = nomes[j]
nomes[j] = aux
print(f"Os nomes {nomes[i]} e {nomes[j]} foram trocados de lugar")
print(nomes)
