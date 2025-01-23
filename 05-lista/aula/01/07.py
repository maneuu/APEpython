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

for nome in range(len(nomes)-1):
    print(f"- {nomes[nome]} e {nomes[nome+1]}")