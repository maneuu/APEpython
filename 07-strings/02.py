texto_entrada = input("Digite o texto: ")

for caractere in texto_entrada:
    ascii_valor = ord(caractere)
    binario = bin(ascii_valor)
    hexadecimal = hex(ascii_valor)
    octal = oct(ascii_valor)

    print(f"Símbolo: {caractere}, ASCII: {ascii_valor}, BIN: {binario}, HEX: {hexadecimal}, OCTA: {octal}")
    print("\n==============================\n")
