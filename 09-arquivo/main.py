def ip(registro: str) -> str:
    """Extrai o IP de um registro de log."""
    return registro.split(' ')[0]

def dia(registro: str) -> str:
    """Extrai a data de um registro de log."""
    inicio = registro.find('[') + 1
    fim = registro.find(':', inicio)
    return registro[inicio:fim]

def ips(registros: list) -> list:
    """Retorna a lista de IPs únicos."""
    return list(set(ip(registro) for registro in registros))

def contar_acessos_por_dia(registros: list) -> dict:
    """Conta quantos acessos ocorreram em cada dia."""
    contagem_por_dia = {}
    for registro in registros:
        data = dia(registro)
        contagem_por_dia[data] = contagem_por_dia.get(data, 0) + 1
    return contagem_por_dia

def dia_maior_ataque(registros: list) -> tuple:
    """Retorna o dia com mais ataques no log e a quantidade de ataques."""
    contagem = contar_acessos_por_dia(registros)
    dia_mais = max(contagem, key=contagem.get)
    return dia_mais, contagem[dia_mais]

def dia_menor_ataque(registros: list) -> tuple:
    """Retorna o dia com menos ataques no log e a quantidade de ataques."""
    contagem = contar_acessos_por_dia(registros)
    dia_menos = min(contagem, key=contagem.get)
    return dia_menos, contagem[dia_menos]

# Lendo o arquivo e processando os dados
with open('09-arquivo/access.log', 'r') as arquivo:
    registros = arquivo.read().splitlines()

# Obtendo os resultados
quantidade_ips = len(ips(registros))
dia_mais_ataques, ataques_mais = dia_maior_ataque(registros)
dia_menos_ataques, ataques_menos = dia_menor_ataque(registros)

# Exibindo os resultados
print(f'Quantidade de IPs diferentes: {quantidade_ips}')
print(f'Dia com mais ataques: {dia_mais_ataques} ({ataques_mais} ataques)')
print(f'Dia com menos ataques: {dia_menos_ataques} ({ataques_menos} ataques)')
