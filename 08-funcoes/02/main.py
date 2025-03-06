# Escreva um programa para ler a quantidade de estudantes de uma turma. 
# Gere uma lista contendo notas aleatórias para esses estudantes, com valores entre 0 e 100.

# Calcular e exibir:
# a) As notas dos estudantes.
# b) A média das notas da turma.
# c) A quantidade de estudantes com nota acima da média da turma.
# d) A quantidade de estudantes com nota abaixo da média da turma.
# e) A quantidade de estudantes aprovados (nota maior ou igual a 70).
# f) A quantidade de estudantes reprovados (nota menor que 70).
# g) A quantidade de estudantes que não possuem nota entre 70 e 80 (inclusive).
# h) Notas que foram encontradas na avaliação.
# i) Nota(s) mais frequente(s).

# Utilize as funções da biblioteca manipula_lista.py.

import manipula_lista as ml
from random import randint

# Função para gerar as notas aleatórias
def gerar_notas(quantidade: int) -> list:
    return ml.gerar_lista(quantidade, 0, 100)

# Função principal
def main():
    # Ler a quantidade de estudantes
    quantidade_estudantes = int(input("Digite a quantidade de estudantes: "))
    
    # Gerar as notas aleatórias
    notas = gerar_notas(quantidade_estudantes)
    
    # Exibindo as notas dos estudantes
    print("\n=========================")
    print("Notas dos estudantes:")
    ml.exibir_lista(notas)
    print("=========================\n")

    # b) Calcular e exibir a média das notas
    media = ml.calcular_media(notas)
    print(f"Média das notas da turma: {media:.2f}\n")

    # c) Quantidade de estudantes com nota acima da média
    qtd_acima_media = ml.quantidade_elementos_acima_da_media(notas)
    print(f"Quantidade de estudantes com nota acima da média: {qtd_acima_media}")

    # d) Quantidade de estudantes com nota abaixo da média
    qtd_abaixo_media = ml.quantidade_elementos_abaixo_da_media(notas)
    print(f"Quantidade de estudantes com nota abaixo da média: {qtd_abaixo_media}")

    # e) Quantidade de estudantes aprovados (nota >= 70)
    aprovados = [nota for nota in notas if nota >= 70]
    print(f"\nQuantidade de estudantes aprovados (nota >= 70): {len(aprovados)}")

    # f) Quantidade de estudantes reprovados (nota < 70)
    reprovados = [nota for nota in notas if nota < 70]
    print(f"Quantidade de estudantes reprovados (nota < 70): {len(reprovados)}")

    # g) Quantidade de estudantes que não possuem nota entre 70 e 80 (inclusive)
    nao_entre_70_80 = ml.quantidade_elementos_fora_de_um_intervalo(notas, 70, 80)
    print(f"Quantidade de estudantes que não possuem nota entre 70 e 80 (inclusive): {nao_entre_70_80}\n")

    # h) Exibir as notas encontradas na avaliação (elementos distintos)
    notas_distintas = ml.elementos_distintos(notas)
    print(f"Notas distintas encontradas na avaliação:")
    ml.exibir_lista(notas_distintas)

    # i) Exibir a(s) nota(s) mais frequente(s)
    notas_frequentes = ml.elemento_mais_frequente(notas)
    print(f"\nNota(s) mais frequente(s):")
    ml.exibir_lista(notas_frequentes)
    print("=========================\n")

# Chamar a função principal para executar o programa
if __name__ == "__main__":
    main()
