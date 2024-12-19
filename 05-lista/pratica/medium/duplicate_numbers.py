# Lista original com alguns números, incluindo duplicatas
lst = [6, 3, 98, 24, 3, 5, 74, 1, 5, 6, 3]

# A função set() converte a lista em um conjunto (set), que é uma estrutura de dados que
# **não permite elementos duplicados**. Ao passar a lista para o set, ele automaticamente 
# remove qualquer valor repetido, mantendo apenas um de cada valor único.
# A função list() é então usada para converter o conjunto de volta em uma lista, 
# pois o set não mantém a ordem original dos elementos. O resultado será uma lista com
# os valores únicos, mas a ordem pode não ser a mesma da lista original.
print(f"List with duplicates: {lst}")
print(f"How 'set' works: {set(lst)}")
print(f'List without duplicates: {list(set(lst))}')
