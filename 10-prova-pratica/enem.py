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
        inicio = linha.find('Campus')
        fim = linha.find('"', inicio)
        campus.add(linha[inicio:fim])
    return list(campus)


# Relação dos Cursos de um determinado Campus.
def cursos(registros: list, nome_campus: str) -> list:
    lista_cursos = set()
    for linha in registros:
        if nome_campus:
            lista_separada = linha.split(";")
            nome_curso = lista_separada[6]
            lista_cursos.add(nome_curso)
    return list(lista_cursos)



# Maior nota da instituição
def maior_nota_instituicao(registros: list) -> float:
    notas = []
    for linha in registros:
        lista_separada = linha.split(";")
        nota = lista_separada[16].replace(",", ".")
        nota = float(nota.strip("'\""))
        notas.append(nota)
    return max(notas)

# Maior nota do Campus
def maior_nota_campus(registros: list, nome_campus: str) -> float:
    notas = []
    for linha in registros:
        if nome_campus in linha:
            lista_separada = linha.split(";")
            nota = lista_separada[16].replace(",", ".")
            nota = float(nota.strip("'\""))
            notas.append(nota)
    return max(notas)

# Maior nota de um Curso
def maior_nota_curso(registros: list, codigo_curso: int) -> float:
    pass

# Maior nota de corte da instituição
def maior_nota_corte_instituicao(registros: list) -> float:
    notas = []
    for linha in registros:
        lista_separada = linha.split(";")
        nota = lista_separada[17].replace(",", ".")
        nota = float(nota.strip("'\""))
        notas.append(nota)

    return max(notas)

# Maior nota do Campus
def maior_nota_corte_campus(registros: list, nome_campus: str) -> float:
    notas = []
    for linha in registros:
        if nome_campus in linha:
            lista_separada = linha.split(";")
            nota = lista_separada[17].replace(",", ".")
            nota = float(nota.strip("'\""))
            notas.append(nota)
    return max(notas)

# registro = registros("dados_mec.csv")
# print(maior_nota_corte_campus(registro, "Campus Planaltina"))



def maior_nota_corte_curso(registros: list, codigo_curso: int) -> float:
    for linha in registros:
        if codigo_curso in linha:
            pass

# Retorna o código de um determinado curso de um determinado campus
def codigo_curso(registros: list, nome_campus: str, nome_curso: str) -> int:
    codigo = None
    for linha in registros:
        if nome_campus in linha and nome_curso in linha:
            lista_separada = linha.split(";")
            codigo = int(lista_separada[5].strip("'\""))
    return codigo
            
