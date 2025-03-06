# Gerar uma lista de tamanho n com valores aleatórios.
from random import randint
def gerar_lista(quantidade: int, menor_valor: int, maior_maior: int) -> list:
    lista = []
    for _ in range(quantidade):
        lista.append(randint(menor_valor,maior_maior))
    return lista

# Exibir os elementos da lista, um por linha.
def exibir_lista(lista: list):
    for item in lista:
        print(item)

# Calcular a média dos valores da lista.
def calcular_media(lista: list) -> float:
    qtd_elementos = len(lista)
    media = sum(lista) / qtd_elementos
    return media

# Elementos com valores acima da média.
def elementos_acima_da_media(lista: list) -> list:
    valores_acima = []
    media = sum(lista) / len(lista)
    for item in lista:
        if item > media:
            valores_acima.append(item)
    return valores_acima

        

# Elementos com valores abaixo da média.
def elementos_abaixo_da_media(lista: list) -> list:
    valores_baixo = []
    media = sum(lista) / len(lista)
    for item in lista:
        if item < media:
            valores_baixo.append(item)
    return valores_baixo


# Elementos com valores entre (inclusive) dois valores informados.
def elementos_entre_dois_valores(lista: list, valor1: int, valor2: int) -> list:
    valores = []
    for item in lista:
        if item > valor1 and item < valor2:
            valores.append(item)
    return valores

# Elementos com valores fora de um intervalo informado.
def elementos_fora_de_um_intervalo(lista: list, valor1: int, valor2: int) -> list:
    valores = []
    for item in lista:
        if item < valor1 or item > valor2:
            valores.append(item)
    return valores

# Elementos distintos da lista.
def elementos_distintos(lista: list) -> list:
    items_distintos = []
    for item in lista:
        if item not in items_distintos:
            items_distintos.append(item)

    return items_distintos

# Elemento mais frequente. Pode haver repetição.
def elemento_mais_frequente(lista: list) -> list:
    frequencia = 0
    for item in lista:
        if lista.count(item) > frequencia:
            frequencia = lista.count(item)
    valores_frequentes = []
    for item in lista:
        if lista.count(item) == frequencia:
            valores_frequentes.append(item)
    return valores_frequentes


# Calcular a quantidade de elementos com valores acima da média.
def quantidade_elementos_acima_da_media(lista: list) -> int:
    valores_acima = []
    media = sum(lista) / len(lista)
    for item in lista:
        if item > media:
            valores_acima.append(item)
    return len(valores_acima)

# Calcular a quantidade de elementos com valores abaixo da média.
def quantidade_elementos_abaixo_da_media(lista: list) -> int:
    valores_baixo = []
    media = sum(lista) / len(lista)
    for item in lista:
        if item < media:
            valores_baixo.append(item)
    return len(valores_baixo)

# Calcular a quantidade de elementos com valores entre (inclusive) dois valores informados.
def quantidade_elementos_entre_dois_valores(lista: list, menor_valor: int, maior_valor: int) -> int:
    valores = []
    for item in lista:
        if item > menor_valor and item < maior_valor:
            valores.append(item)
    return len(valores)

# Calcular a quantidade de elementos com valores fora de um intervalo informado.
def quantidade_elementos_fora_de_um_intervalo(lista: list, menor_valor: int, maior_valor: int) -> int:
    valores = []
    for item in lista:
        if item < menor_valor or item > maior_valor:
            valores.append(item)
    return len(valores)

# Calcular a quantidade de elementos distintos da lista
def quantidade_elementos_distintos(lista: list) -> int:
    items_distintos = []
    for item in lista:
        if item not in items_distintos:
            items_distintos.append(item)
    return len(items_distintos)