ordem = int(input("Ordem da matriz: "))

matriz = []
for i in range(ordem):
    linha = [int(input(f"Valor ({i+1})({j+1}): ")) for j in range(ordem)]
    matriz.append(linha)

simetrico = True
for i in range(ordem):
    for j in range(ordem):
        if matriz[i][j] != matriz[j][i]: 
            simetrico = False

    if not simetrico: 
        break


print("Matriz simetrica" if simetrico else "Matriz não simetrica")
