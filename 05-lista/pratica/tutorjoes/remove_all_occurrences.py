val = [1, 3, 4, 6, 5, 1]
a = 1
print ("Original list :" ,val)
c = val.count(a)
print(f"Number of occurrences of the number {a} in the list: {c}\n")

for i in range(c):
    val.remove(a)
print (f"List after removing all occurrences of the number {a}:", val)