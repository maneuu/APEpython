list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Iterando sobre uma cópia da lista para remover as strings vazias
for item in list1:
    if item == "":
        list1.remove(item)

print(list1)