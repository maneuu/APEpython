'''
Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

Sample Output

First 5 elements : [1, 4, 9, 16, 25]

Last 5 elements : [625, 676, 729, 784, 841]
'''
lista = list(range(1,31))
print("First 5 elements :", [i**2 for i in lista[:5]])
print("Last 5 elements :", [i**2 for i in lista[-5:]])

# or

lista = list(range(1,31))
print(f"Lista completa: {lista}")
print(f"First 5 elements: {lista[:5]}")
for i in range(5):
    print(lista[i]**2, end=" ")
print()
print(f"Last 5 elements: {lista[-5:]}")
for i in range(25,30):
    print(lista[i]**2, end=" ")
