# Write a Python program to print the numbers of a specified list after removing even numbers from it

# Sample Output

# [7,32,81,20,25,14,23,27]

# [7, 81, 25, 23, 27]

lista = [7,32,81,20,25,14,23,27]
print(f"Lista original: {lista}")
lista = [i for i in lista if i % 2 != 0]
print(f"Lista sem números pares: {lista}")

# or
print("============================================")

lista = [7,32,81,20,25,14,23,27]
print(f"Lista original: {lista}")
for i in lista:
    if i % 2 == 0:
        lista.remove(i)
print(f"Lista sem números pares: {lista}")
