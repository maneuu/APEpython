codigo_entrada = input("Digite o código alfanumérico: ")
codigo_modificado = ""

for caractere in codigo_entrada:
    if caractere.isdigit():
        codigo_modificado += "*"  # Substitui dígitos por '*'
    else:
        codigo_modificado += caractere  # Mantém os outros caracteres

print(f"Código modificado: {codigo_modificado}")
