lst = [3,6, 4, 5, 6, 7]
"""
O método sort() é usado para ordenar os elementos da lista em ordem crescente. O método sort() modifica a lista original in-place, ou seja, ele altera a lista diretamente.

Após chamar lst.sort(), a lista lst será organizada em ordem crescente
de - [3, 6, 4, 5, 6, 7]
para - [3, 4, 5, 6, 6, 7]
"""
lst.sort()

print('Second smallest element:', lst[1])
