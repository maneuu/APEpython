from random import randint

nomes = []
email = []
while True:
    nome = input("Nome  >> ")
    if nome == '':
        break
    email_input = input("Email >> ")

    nomes.append(nome)
    email.append(email_input)

print('Nomes lidos:')
print(nomes)
print("\nEmails lidos:")
print(email)

for i in range(len(nomes)-1):
    print(f"{nomes[i]} - {email[i]}")