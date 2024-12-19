list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])

# OR

list1 = [10, 20, 4, 45, 99]
print("Largest element is:", max(list1))

# OR

list1 = [10, 20, 4, 45, 99]
max = list1[0]
for i in list1:
    if i > max:
        max = i
print("Largest element is:", max)