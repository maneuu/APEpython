'''
    Nome: lib_vogais
    Descrição: Biblioteca para manipulação de vogais em textos.
    Autores: Valéria Cavalcanti, <seu_nome>
    Data: 27/02/2025
    Versão: 1.0
'''

# Verifica se um determinado símbolo é vogal.
def eh_vogal(simbolo: str) -> bool:
    vogais = ["a", "e", "i", "o", "u"]
    if simbolo in vogais:
        return True
    else:
        return False

# Verifica se um texto é formado apenas por vogais.
def eh_texto_vogal(texto: str) -> bool:
    vogais = ["a", "e", "i", "o", "u"]
    apenas_vogais = True
    for simbolo in texto:
        if simbolo.lower() not in vogais:
            apenas_vogais = False
    
    return apenas_vogais
        

# Retorna a quantidade de vogais em um texto.
def quantidade_vogais(texto: str) -> int:
    vogais = ["a", "e", "i", "o", "u"]
    qtd_vogais = 0
    for simbolo in texto:
        if simbolo.lower() in vogais:
            qtd_vogais += 1
    
    return qtd_vogais


# Remove as vogais de um texto.
def remove_vogais(texto:str) -> str:
    texto_modificado = ""
    vogais = ["a", "e", "i", "o", "u"]

    for simbolo in texto:
        if simbolo.lower() not in vogais:
            texto_modificado += simbolo
    return texto_modificado

# Identifica as vogais que estão presentes em um texto.
def identifica_vogais(texto: str) -> list:
    vogais = ["a", "e", "i", "o", "u"]
    vogais_do_texto = []
    for simbolo in texto:
        if simbolo.lower() in vogais and simbolo.lower() not in vogais_do_texto:
            vogais_do_texto.append(simbolo.lower())
    
    return vogais_do_texto
        

# Frequêcia de vogais em um texto.
def frequencia_vogais(texto: str) -> list:
    vogais = ["a", "e", "i", "o", "u"]
    frequencia = [0,0,0,0,0] # a e i o u
    for simbolo in texto:
        if simbolo.lower() in vogais:
            index = vogais.index(simbolo.lower())  
            frequencia[index] += 1
    return frequencia



# Substitui as vogais de um texto por * (asterísco).
def substitui_vogais(texto: str) -> str:
    texto_modificado = ""
    vogais = ["a", "e", "i", "o", "u"]
    for simbolo in texto:
        if simbolo.lower() in vogais:
            texto_modificado += "*"
        else:
            texto_modificado += simbolo
    return texto_modificado

# Identifica a vogal que mais aparece em um texto. Pode haver mais de uma vogal com a mesma frequência.
def vogal_mais_frequente(texto: str) -> list:
    vogais = ["a", "e", "i", "o", "u"]
    frequencia = [0,0,0,0,0] # a e i o u
    for simbolo in texto:
        if simbolo.lower() in vogais:
            index = vogais.index(simbolo.lower())  
            frequencia[index] += 1
    
    maior_frequencia = max(frequencia)
    maiores_frequencia = []
    for i in range(len(frequencia)):
        if frequencia[i] == maior_frequencia:
            maiores_frequencia.append(vogais[i])
    return maiores_frequencia

    
# Sortear uma vogal.
def sortear_vogal() -> str:
    from random import randint
    vogais = ["a", "e", "i", "o", "u"]
    valor_aleatorio = randint(0,4)
    vogal_sorteada = vogais[valor_aleatorio]
    return vogal_sorteada


