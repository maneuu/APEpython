palavras_digitadas = []
palavras_unicas = []

while True: 
    palavra = input("Digite uma palavra (ou 'fim' para encerrar): ")
    if palavra.lower() == "fim":
        break
    palavras_digitadas.append(palavra)
    if palavra not in palavras_unicas:
        palavras_unicas.append(palavra)

for palavra in palavras_unicas:
    print(f"\t>> Palavra: {palavra}, Quantidade de ocorrências: {palavras_digitadas.count(palavra)}\n")
