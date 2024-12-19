# Lista original que contém números e uma sublista dentro da sublista
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

'''A expressão list1[2] acessa o terceiro elemento da lista (lembre-se que o índice começa em 0),
que é a sublista [300, 400, [5000, 6000], 500].
Dentro dessa sublista, list1[2][2] acessa o terceiro elemento, que é a sublista interna [5000, 6000].
O método append(7000) adiciona o valor 7000 no final dessa sublista [5000, 6000].
Após a execução do append, a sublista [5000, 6000] se torna [5000, 6000, 7000].'''
list1[2][2].append(7000)

# Exibe a lista modificada
print(list1)
