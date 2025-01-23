nomes = []
while True:
    nome = input("Nome  >> ")
    if nome == '':
        
        break
    nomes.append(nome)

print('Nomes lidos:')
print(nomes)

print("\n===================================\n")

ultimo = nomes.pop()
primeiro = nomes.pop(0)

nomes.insert(0, ultimo)
nomes.append(primeiro)

print("Nomes com o primeiro e o último trocados:")
print(nomes)