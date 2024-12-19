# Lista original com alguns números
lst = [5, 10, 15, 200, 25, 50, 20]

"""O método insert() insere um elemento em uma posição específica na lista.
A sintaxe é: lst.insert(posição, valor), onde:
- 'posição' é o índice onde o valor será inserido.
- 'valor' é o elemento a ser inserido na lista.
Aqui, estamos inserindo o valor 500 no índice 2 da lista (lembrando que os índices começam de 0).
O valor 500 será inserido antes do elemento que já está no índice 2, que é o valor 15."""
lst.insert(2, 500)

print(lst)
