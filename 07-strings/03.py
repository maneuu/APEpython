entrada_texto = input("Digite o texto: ")

quantidade_maiusculas = 0
quantidade_minusculas = 0
quantidade_numeros = 0

for caractere in entrada_texto:
    if caractere.isupper():
        quantidade_maiusculas += 1
    elif caractere.islower():
        quantidade_minusculas += 1
    elif caractere.isdigit():
        quantidade_numeros += 1

print(f"Quantidade de letras maiúsculas no texto: {quantidade_maiusculas}")
print(f"Quantidade de letras minúsculas no texto: {quantidade_minusculas}")
print(f"Quantidade de números no texto: {quantidade_numeros}")
