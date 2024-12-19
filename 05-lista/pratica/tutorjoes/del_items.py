"""Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. (enumerate)

Sample Output

["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]

['Dog', 'Elephant', 'Fox', 'Ponda']
"""
list1 = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
print('Original list:', list1)
for i,x in enumerate(list1):
    if i in (0,4,5):
        del list1[i]

print(f"List after removing the 0th, 4th and 5th elements: {list1}")