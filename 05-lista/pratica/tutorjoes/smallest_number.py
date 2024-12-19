list1 = [10, 20, 4, 45, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.sort()
print("Smallest element is:", list1[0])

# OR

list1 = [10, 20, 4, 45, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Smallest element is:", min(list1))

# OR

list1 = [10, 20, 4, 45, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min = list1[0]
for i in list1:
    if i < min:
        min = i
print("Smallest element is:", min)