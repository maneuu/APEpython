soma_idade = 0
pessoas = 0
media_idade = 0

while True:
    idade = int(input("Idade: \n\t>>> "))
    if idade <= 0:
        break
    
    soma_idade += idade
    pessoas += 1
    media_idade = soma_idade / pessoas
    
print(f"{media_idade:.2f}")
