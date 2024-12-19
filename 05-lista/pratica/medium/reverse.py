# Lista original com algumas letras
lst = ['A', 'P', 'B', 'Q', 'C', 'D']

"""
A operação lst[::-1] inverte a lista original
- O primeiro ':' indica que queremos considerar todos os elementos da lista.
- O '-1' especifica o passo da fatia, ou seja, ao invés de pegar os elementos na ordem original,
  o '-1' faz com que eles sejam selecionados de trás para frente.
O resultado é uma nova lista, rev, com os elementos da lista original invertidos.
"""
rev = lst[::-1]

print(rev)
