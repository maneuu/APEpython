import lib_vogais as lv

'''
    Testes para as funções criadas na biblioteca "lib_vogais".
'''
print("=" * 50)

# Testes para a função eh_vogal

# Caso 1: Testa a vogal 'a'
print(lv.eh_vogal("a"))  # Esperado: True

# Caso 2: Testa a vogal 'e'
print(lv.eh_vogal("e"))  # Esperado: True

# Caso 3: Testa uma letra que não é vogal ('b')
print(lv.eh_vogal("b"))  # Esperado: False

# Caso 4: Testa a vogal maiúscula 'I'
print(lv.eh_vogal("I"))  # Esperado: True

# Caso 5: Testa um caractere especial
print(lv.eh_vogal("#"))  # Esperado: False

# ====================================================
print("=" * 50)

# Testes para a função eh_texto_vogal 

# Caso 1: Texto com apenas vogais minúsculas
print(lv.eh_texto_vogal("aeiou"))  # Esperado: True

# Caso 2: Texto com apenas vogais maiúsculas
print(lv.eh_texto_vogal("AEIOU"))  # Esperado: True

# Caso 3: Texto com vogais e consoantes
print(lv.eh_texto_vogal("aeiob"))  # Esperado: False

# Caso 4: Texto vazio
print(lv.eh_texto_vogal(""))  # Esperado: False

# Caso 5: Texto com símbolos e números
print(lv.eh_texto_vogal("a2e!"))  # Esperado: False

# ========================================================
print("=" * 50)

# Testes para a função quantidade_vogais

# Caso 1: Texto com 5 vogais
print(lv.quantidade_vogais("aeiou"))  # Esperado: 5

# Caso 2: Texto com letras e números
print(lv.quantidade_vogais("aei3o1u"))  # Esperado: 5

# Caso 3: Texto com apenas consoantes
print(lv.quantidade_vogais("bcdfg"))  # Esperado: 0

# Caso 4: Texto com letras maiúsculas
print(lv.quantidade_vogais("AEIOU"))  # Esperado: 5

# Caso 5: Texto vazio
print(lv.quantidade_vogais(""))  # Esperado: 0

# ==============================================================
print("=" * 50)

# Testes para a função remove_vogais

# Caso 1: Texto com vogais a serem removidas
print(lv.remove_vogais("aeiou"))  # Esperado: ""

# Caso 2: Texto com letras e números
print(lv.remove_vogais("aei3o1u"))  # Esperado: "31"

# Caso 3: Texto com apenas consoantes
print(lv.remove_vogais("bcdfg"))  # Esperado: "bcdfg"

# Caso 4: Texto com espaços e pontuação
print(lv.remove_vogais("hello, world!"))  # Esperado: "hll, wrld!"

# Caso 5: Texto vazio
print(lv.remove_vogais(""))  # Esperado: ""

# =============================================
print("=" * 50)

# Testes para a função identifica_vogais

# Caso 1: Texto com todas as vogais
print(lv.identifica_vogais("aeiou"))  # Esperado: ['a', 'e', 'i', 'o', 'u']

# Caso 2: Texto com vogais repetidas
print(lv.identifica_vogais("aaaeeeiiiooo"))  # Esperado: ['a', 'e', 'i', 'o']

# Caso 3: Texto com apenas consoantes
print(lv.identifica_vogais("bcdfg"))  # Esperado: []

# Caso 4: Texto misturado com consoantes e vogais
print(lv.identifica_vogais("hello"))  # Esperado: ['e', 'o']

# Caso 5: Texto vazio
print(lv.identifica_vogais(""))  # Esperado: []


#  ====================================================
print("=" * 50)

# Testes para a função frequencia_vogais

# Caso 1: Texto com todas as vogais
print(lv.frequencia_vogais("aeiou"))  # Esperado: [1, 1, 1, 1, 1]

# Caso 2: Texto com vogais repetidas
print(lv.frequencia_vogais("aeiiooo"))  # Esperado: [1, 1, 2, 3, 0]

# Caso 3: Texto com apenas consoantes
print(lv.frequencia_vogais("bcdfg"))  # Esperado: [0, 0, 0, 0, 0]

# Caso 4: Texto com misturas de maiúsculas e minúsculas
print(lv.frequencia_vogais("aEiOu"))  # Esperado: [1, 1, 1, 1, 1]

# Caso 5: Texto vazio
print(lv.frequencia_vogais(""))  # Esperado: [0, 0, 0, 0, 0]

#  =========================================================
print("=" * 50)

# Testes para a função substitui_vogais

# Caso 1: Texto com todas as vogais
print(lv.substitui_vogais("aeiou"))  # Esperado: ""

# Caso 2: Texto com letras e números
print(lv.substitui_vogais("aei3o1u"))  # Esperado: "31"

# Caso 3: Texto com apenas consoantes
print(lv.substitui_vogais("bcdfg"))  # Esperado: "bcdfg"

# Caso 4: Texto com espaços e pontuação
print(lv.substitui_vogais("hello, world!"))  # Esperado: "hll, wrld!"

# Caso 5: Texto vazio
print(lv.substitui_vogais(""))  # Esperado: ""

# ====================================================================
print("=" * 50)

# Testes para a função vogal_mais_frequente

# Caso 1: Texto com uma vogal mais frequente
print(lv.vogal_mais_frequente("aeioo"))  # Esperado: ['o']

# Caso 2: Texto com duas vogais igualmente frequentes
print(lv.vogal_mais_frequente("aeiooou"))  # Esperado: ['o', 'u']

# Caso 3: Texto com apenas consoantes
print(lv.vogal_mais_frequente("bcdfg"))  # Esperado: []

# Caso 4: Texto com misturas de maiúsculas e minúsculas
print(lv.vogal_mais_frequente("aeiouAEIOU"))  # Esperado: ['a', 'e', 'i', 'o', 'u']

# Caso 5: Texto vazio
print(lv.vogal_mais_frequente(""))  # Esperado: []


# ===============================================================
print("=" * 50)
# Testes para a função sortear_vogal

# Caso 1: Sorteio de uma vogal (não há como prever qual será)
print(lv.sortear_vogal())  # Esperado: Qualquer vogal ('a', 'e', 'i', 'o', 'u')

# Caso 2: Sorteio de uma vogal novamente
print(lv.sortear_vogal())  # Esperado: Qualquer vogal

# Caso 3: Sorteio de uma vogal mais uma vez
print(lv.sortear_vogal())  # Esperado: Qualquer vogal

# Caso 4: Sorteio de uma vogal
print(lv.sortear_vogal())  # Esperado: Qualquer vogal

# Caso 5: Sorteio de uma vogal
print(lv.sortear_vogal())  # Esperado: Qualquer vogal
