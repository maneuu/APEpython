ordem = int(input("Ordem: "))


matriz = []
matriz_identidade = True

for i in range(ordem):
    linha = []

    for j in range(ordem):
        N = int(input(f"Valor ({i+1}) ({j+1}):"))
        linha.append(N)
        if (i == j and N != 1) or (i != j and N != 0):
            matriz_identidade = False
        
    matriz.append(linha)


print("E uma matriz identidade\n" if matriz_identidade else "Não é uma matriz identidade\n")


print("="*20)
for i in matriz:
    print(i)
print("="*20)