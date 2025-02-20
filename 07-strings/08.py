texto = input("TEXTO: ")

# Divide o texto em palavras
palavra_texto = texto.split()

# Cria uma lista de palavras únicas
palavras_unicas = []
for item in palavra_texto:
    if item not in palavras_unicas:
        palavras_unicas.append(item)

# Variáveis para armazenar as palavras com maior frequência
maior_frequencia = 0
palavras_freq = []

# Contagem da frequência de cada palavra
for item in palavras_unicas:
    frequencia = palavra_texto.count(item)
    if frequencia > maior_frequencia:
        maior_frequencia = frequencia
    palavras_freq.append([item, frequencia])

# Exibe a frequência de todas as palavras
print("\nFrequência de todas as palavras:")
for item, frequencia in palavras_freq:
    print(f"{item}: {frequencia}")

# Exibe as palavras com maior frequência e seus índices
print("\nPalavra(s) com maior frequência:")
for item, frequencia in palavras_freq:
    if frequencia == maior_frequencia:
        indices = [i for i, palavra in enumerate(palavra_texto) if palavra == item]
        print(f"Palavra: '{item}', Frequência: {frequencia}, Índices: {indices}")
