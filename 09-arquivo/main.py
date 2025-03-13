arquivo = open('09-arquivo/access.log', 'r')

conteudo = arquivo.read()

linhas = conteudo.splitlines()

ips = []
for ip in linhas:
    linha = ""
    for char in linha:
        if char == " ": break
        linha += char
    ips.append(linha)

print(ips[0])
print("a")

arquivo.close()