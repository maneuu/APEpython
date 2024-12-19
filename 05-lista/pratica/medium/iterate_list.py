"""Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:

10 400
20 300
30 200
40 100"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Inverter list2
list2.reverse()

# Iterar pelas duas listas simultaneamente
for i in range(len(list1)):
    print(list1[i], list2[i])


print("=="*30)

# Com a função zip()
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Inverter list2
list2.reverse()

# Usar zip para iterar ambas as listas
for item1, item2 in zip(list1, list2):
    print(item1, item2)
