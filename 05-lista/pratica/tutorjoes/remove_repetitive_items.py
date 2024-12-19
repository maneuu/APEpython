num = [2,3,4,5,2,6,3,2]
print(f"Original list: {num}\n")
x = []
for i in range(len(num)):
    if num[i] not in x:
        x.append(num[i])


print(f"Removed repetitive items: {x}")