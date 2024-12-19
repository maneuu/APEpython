# Importando o módulo random, que contém funções para gerar números aleatórios e manipular listas de forma aleatória
import random

# Definindo uma lista com os números de 1 a 5
lst = [1, 2, 3, 4, 5]
print("Lista não embaralhada")
print(lst)

# Embaralhando os elementos da lista de forma aleatória
print("\nLista embaralhada")
random.shuffle(lst)
print(lst)
