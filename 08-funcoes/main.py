import lib_vogais as lv

'''
    Programa para exibir um menu iterativo com as opções a seguir:
    
    1 - Verificar se um texto é formado apenas por vogais.
    2 - Contar a quantidade de vogais em um texto.
    3 - Exibir o texto sem as vogais.
    4 - Exibir o texto substituindo as vogais por * (asterísco).
    5 - Exibir as vogais presentes no texto.
    6 - Exibir a frequência de cada vogal no texto.
    7 - Exibir a(s) vogal(is) que mais aparece(m) no texto.
    8 - Sair.
'''

while True:
    print("""
    1 - Verificar se um texto é formado apenas por vogais.
    2 - Contar a quantidade de vogais em um texto.
    3 - Exibir o texto sem as vogais.
    4 - Exibir o texto substituindo as vogais por * (asterísco).
    5 - Exibir as vogais presentes no texto.
    6 - Exibir a frequência de cada vogal no texto.
    7 - Exibir a(s) vogal(is) que mais aparece(m) no texto.
    8 - Sair.
          """)
    valor = int(input())
    if valor == 1:
        teste1 = input("Teste 1 (função eh_texto_vogal): ")
        print(lv.eh_texto_vogal(teste1))
    elif valor == 2:
        teste2 = input("Teste 2 (função quantidade_vogais): ")
        print(lv.quantidade_vogais(teste2))
    elif valor == 3:
        teste3 = input("Teste 3 (função remove_vogais): ")
        print(lv.remove_vogais(teste3))
    elif valor == 4:
        teste4 = input("Teste 4 (função substitui_vogais): ")
        print(lv.substitui_vogais(teste4))
    elif valor == 5:
        teste5 = input("Teste 5 (função identifica_vogais): ")
        print(lv.identifica_vogais(teste5))
    elif valor == 6:
        teste6 = input("Teste 6 (função frequencia_vogais): ")
        print(lv.frequencia_vogais(teste6))
    elif valor == 7:
        teste7 = input("Teste 7 (função vogal_mais_frequente): ")
        print(lv.vogal_mais_frequente(teste7))
    elif valor == 8:
        print("Programa finalizado")
        break
    else:
        print("Digite um valor valido")