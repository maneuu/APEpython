texto = input("Digite o texto: ")
contador = 0
letras_python = "python"

for char in texto:
    if char.lower() in letras_python:
        contador += 1

print(f"A quantidade de vezes que aparecem letras de 'python' no texto é: {contador}")
