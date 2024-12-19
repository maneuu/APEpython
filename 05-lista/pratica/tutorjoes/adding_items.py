# Adding items to a list using insert() and append() in Python

# append() method
numbers = [10,20,30,40,50,60]

numbers.append(70)
print(numbers)

# If we use the insert method to add items to a list, we have to specify the position at which we want to insert an item. The insert() method takes two arguments [ insert(position,item) ].
numbers = [10,20,30,40,50,60]

numbers.insert(0,5)
print(numbers)

