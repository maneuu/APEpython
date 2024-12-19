num = [7, 8, 120, 25, 44, 20, 27]
print(f"Original list: {num}\n")

num = [x for x in num if x % 2 != 0]

print(f"Modified list: {num}")

# or
print('='*50)

num = [7, 8, 120, 25, 44, 20, 27]
print(f"Original list: {num}\n")
odd_num = []

for n in num:
    if n % 2 != 0:
        odd_num.append(n)


print(f"Modified list: {odd_num}")
