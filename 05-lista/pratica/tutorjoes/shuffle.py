'''
Write a Python program to shuffle and print a specified list (shuffle)

Sample Output

["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]

['Fox', 'Cat', 'Tiger', 'Lion', 'Dog', 'Ponda', 'Elephant']

'''
from random import shuffle
lista = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
print(f"Antes de embaralhar: {lista}")
shuffle(lista)
print(f"Depois de embaralhar: {lista}")