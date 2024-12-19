nomes = []
while True:
    nome = input("Nome  >> ")
    if nome == '':
        
        break
    nomes.append(nome)

print('Nomes lidos:')
print(nomes)
print("\n===================================\n")

aux = nomes[0]

nomes[0] = nomes[-1]

nomes[-1] = aux 

print("Nomes com o primeiro e o último trocados:")  
print(nomes)