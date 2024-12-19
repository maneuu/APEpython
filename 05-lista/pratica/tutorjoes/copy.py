list1 = [1, 2, 3, 4, 5]
list2 = list1

# or

list2 = list1.copy()
print(list2)
# or

list2 = list(list1)
print(list2)
# or

list2 = list1[:]
print(list2)
# or

list2 = []
for i in list1:
    list2.append(i)
print(list2)