# Um grupo é formado por 40 (quarenta) pessoas. Escreva um programa para ler as
# idades das pessoas desse grupo. Ao final, calcular e exibir a idade da pessoa mais velha e a idade da pessoa mais nova.

idada_maior = 0
idade_menor = 200

for i in range(3):
  idade = int(input(f"{i+1}º Idade: "))
  if idade > idada_maior:
    idada_maior = idade
  if idade < idade_menor:
    idade_menor = idade
print(f"O mais velho tem {idada_maior} anos de idade, o mais novo tem {idade_menor} anos de idade.")