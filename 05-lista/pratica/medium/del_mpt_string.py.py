"""Exercise 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

Expected output:

["Mike", "Emma", "Kelly", "Brad"]"""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list1)

for item in list1:
    if item == "":
        list1.remove(item)

print(list1)

print("=="*30)

# Usando a função filter()
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list1)

"""Usando o filter para remover os elementos "falsy" da lista
O filter vai manter apenas os elementos que são "truthy" (verdadeiros)
Quando usamos None como função no filter, ele verifica se o valor do item
é "truthy" ou "falsy". Elementos que são "falsy" (como string vazia "") 
serão removidos, e os "truthy" serão mantidos."""
list1 = list(filter(None, list1))

print(list1)