# Registros encontrados no arquivo
def registros(file: str) -> list:
    arq = open(file, 'r', encoding='utf-8')
    lista = arq.read().splitlines()
    arq.close()
    # A primeira linha contém o cabeçalho de cada campo.
    # Retornar a partir da segunda linha
    return lista[1:]

# Quantidade de registros
def quantidade_registros(registros: list) -> int:
    return len(registros)

# Relação dos Campi da Instituição.
def campi(registros: list) -> list:
    campus = set()
    for linha in registros:
        # inicio = linha.find('Campus')
        # fim = linha.find('"', inicio)
        # campus.add(linha[inicio:fim])
        linha_separada = linha.split(";")
        campus.add(linha_separada[4].strip("'\""))
    return list(campus)


# Relação dos Cursos de um determinado Campus.
def cursos(registros: list, nome_campus: str) -> list:
    lista_cursos = set()
    for linha in registros:
        if nome_campus:
            linha_separada = linha.split(";")
            nome_curso = linha_separada[6].strip("'\"")
            lista_cursos.add(nome_curso)
    return list(lista_cursos)



# Maior nota da instituição
def maior_nota_instituicao(registros: list) -> float:
    notas = []
    for linha in registros:
        linha_separada = linha.split(";")
        nota = linha_separada[16].replace(",", ".")
        nota = float(nota.strip('"'))
        notas.append(nota)
    return max(notas)

# Maior nota do Campus
def maior_nota_campus(registros: list, nome_campus: str) -> float:
    notas = []
    for linha in registros:
        if nome_campus in linha:
            linha_separada = linha.split(";")
            nota = linha_separada[16].replace(",", ".")
            nota = float(nota.strip('"'))
            notas.append(nota)
    return max(notas)

# Maior nota de um Curso
def maior_nota_curso(registros: list, codigo_curso: int) -> float:
    notas = []
    for linha in registros:
        if str(codigo_curso) in linha:
            linha_separada = linha.split(";")
            nota = linha_separada[16].replace(",", ".")
            nota = float(nota.strip("'\""))
            notas.append(nota)
    return max(notas)

# Maior nota de corte da instituição
def maior_nota_corte_instituicao(registros: list) -> float:
    notas = []
    for linha in registros:
        linha_separada = linha.split(";")
        nota = linha_separada[17].replace(",", ".")
        nota = float(nota.strip('"'))
        notas.append(nota)

    return max(notas)

# Maior nota do Campus
def maior_nota_corte_campus(registros: list, nome_campus: str) -> float:
    notas = []
    for linha in registros:
        if nome_campus in linha:
            linha_separada = linha.split(";")
            nota = linha_separada[17].replace(",", ".")
            nota = float(nota.strip("'\""))
            notas.append(nota)
    return max(notas)


def maior_nota_corte_curso(registros: list, codigo_curso: int) -> float:
    notas = []
    for linha in registros:
        if str(codigo_curso) in linha:
            linha_separada = linha.split(";")
            nota = linha_separada[17].replace(",", ".")
            nota = float(nota.strip("'\""))
            notas.append(nota)
    return max(notas)


# Retorna o código de um determinado curso de um determinado campus
def codigo_curso(registros: list, nome_campus: str, nome_curso: str) -> int:
    for linha in registros:
        if nome_campus in linha and nome_curso in linha:
            linha_separada = linha.split(";")
            codigo = int(linha_separada[5].strip("'\""))
            return codigo
    return False
    

