"""Exercise 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

for item in list1:
    for item2 in list2:
        result = item + item2
        list3.append(result)

print(list3)