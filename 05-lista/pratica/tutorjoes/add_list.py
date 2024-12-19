'''
Write a Python program to add a list to the second list

Sample Output

[10, 20, 30, 40]

["Cat", "Dog", "Lion", "Ponda"]

[10, 20, 30, 40, 'Cat', 'Dog', 'Lion', 'Ponda']
'''
list1 = [10, 20, 30, 40]
print(f"List1: {list1}")
list2 = ["Cat", "Dog", "Lion", "Ponda"]
print(f"List2: {list2}")

# Merge list2 into list1
list1.extend(list2)

print(f"Merge list1 and list2: {list1}")

# OR
print('='*50)

list1 = [10, 20, 30, 40]
print(f"List1: {list1}")
list2 = ["Cat", "Dog", "Lion", "Ponda"]
print(f"List2: {list2}")
final_list = list1 + list2
print(f"Merge list1 and list2: {final_list}")