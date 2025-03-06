import manipula_lista as ml

# Teste 1: Gerar lista com 5 elementos entre 1 e 10
def testar_gerar_lista():
    print("Teste 1: Gerar lista")
    lista = ml.gerar_lista(5, 1, 10)
    print(lista)
    print("\n")

# Teste 2: Exibir lista
def testar_exibir_lista():
    print("Teste 2: Exibir lista")
    lista = [10, 20, 30, 40, 50]
    ml.exibir_lista(lista)
    print("\n")

# Teste 3: Calcular média
def testar_calcular_media():
    print("Teste 3: Calcular média")
    lista = [10, 20, 30, 40, 50]
    media = ml.calcular_media(lista)
    print(f"Média: {media}\n")

# Teste 4: Elementos acima da média
def testar_elementos_acima_da_media():
    print("Teste 4: Elementos acima da média")
    lista = [10, 20, 30, 40, 50]
    elementos_acima = ml.elementos_acima_da_media(lista)
    print(f"Elementos acima da média: {elementos_acima}\n")

# Teste 5: Elementos abaixo da média
def testar_elementos_abaixo_da_media():
    print("Teste 5: Elementos abaixo da média")
    lista = [10, 20, 30, 40, 50]
    elementos_abaixo = ml.elementos_abaixo_da_media(lista)
    print(f"Elementos abaixo da média: {elementos_abaixo}\n")

# Teste 6: Elementos entre dois valores
def testar_elementos_entre_dois_valores():
    print("Teste 6: Elementos entre dois valores")
    lista = [10, 20, 30, 40, 50]
    elementos_entre = ml.elementos_entre_dois_valores(lista, 15, 45)
    print(f"Elementos entre 15 e 45: {elementos_entre}\n")

# Teste 7: Elementos fora de um intervalo
def testar_elementos_fora_de_um_intervalo():
    print("Teste 7: Elementos fora de um intervalo")
    lista = [10, 20, 30, 40, 50]
    elementos_fora = ml.elementos_fora_de_um_intervalo(lista, 15, 45)
    print(f"Elementos fora de 15 e 45: {elementos_fora}\n")

# Teste 8: Elementos distintos
def testar_elementos_distintos():
    print("Teste 8: Elementos distintos")
    lista = [10, 20, 10, 30, 20, 40, 50]
    elementos_distintos = ml.elementos_distintos(lista)
    print(f"Elementos distintos: {elementos_distintos}\n")

# Teste 9: Elemento mais frequente
def testar_elemento_mais_frequente():
    print("Teste 9: Elemento mais frequente")
    lista = [10, 20, 10, 30, 10, 40, 50]
    elemento_frequente = ml.elemento_mais_frequente(lista)
    print(f"Elemento mais frequente: {elemento_frequente}\n")

# Teste 10: Quantidade de elementos acima da média
def testar_quantidade_elementos_acima_da_media():
    print("Teste 10: Quantidade de elementos acima da média")
    lista = [10, 20, 30, 40, 50]
    qtd_acima = ml.quantidade_elementos_acima_da_media(lista)
    print(f"Quantidade de elementos acima da média: {qtd_acima}\n")

# Teste 11: Quantidade de elementos abaixo da média
def testar_quantidade_elementos_abaixo_da_media():
    print("Teste 11: Quantidade de elementos abaixo da média")
    lista = [10, 20, 30, 40, 50]
    qtd_abaixo = ml.quantidade_elementos_abaixo_da_media(lista)
    print(f"Quantidade de elementos abaixo da média: {qtd_abaixo}\n")

# Teste 12: Quantidade de elementos entre dois valores
def testar_quantidade_elementos_entre_dois_valores():
    print("Teste 12: Quantidade de elementos entre dois valores")
    lista = [10, 20, 30, 40, 50]
    qtd_entre = ml.quantidade_elementos_entre_dois_valores(lista, 15, 45)
    print(f"Quantidade de elementos entre 15 e 45: {qtd_entre}\n")

# Teste 13: Quantidade de elementos fora de um intervalo
def testar_quantidade_elementos_fora_de_um_intervalo():
    print("Teste 13: Quantidade de elementos fora de um intervalo")
    lista = [10, 20, 30, 40, 50]
    qtd_fora = ml.quantidade_elementos_fora_de_um_intervalo(lista, 15, 45)
    print(f"Quantidade de elementos fora de 15 e 45: {qtd_fora}\n")

# Teste 14: Quantidade de elementos distintos
def testar_quantidade_elementos_distintos():
    print("Teste 14: Quantidade de elementos distintos")
    lista = [10, 20, 10, 30, 20, 40, 50]
    qtd_distintos = ml.quantidade_elementos_distintos(lista)
    print(f"Quantidade de elementos distintos: {qtd_distintos}\n")


# Executando todos os testes
if __name__ == "__main__":
    testar_gerar_lista()
    testar_exibir_lista()
    testar_calcular_media()
    testar_elementos_acima_da_media()
    testar_elementos_abaixo_da_media()
    testar_elementos_entre_dois_valores()
    testar_elementos_fora_de_um_intervalo()
    testar_elementos_distintos()
    testar_elemento_mais_frequente()
    testar_quantidade_elementos_acima_da_media()
    testar_quantidade_elementos_abaixo_da_media()
    testar_quantidade_elementos_entre_dois_valores()
    testar_quantidade_elementos_fora_de_um_intervalo()
    testar_quantidade_elementos_distintos()
