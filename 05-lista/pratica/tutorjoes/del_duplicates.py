# Define a list with duplicate numbers
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original list: {list_numbers}")

# Convert the list to a set to remove duplicates
# Sets do not allow duplicate values, so this will automatically remove any duplicates
list_numbers = list(set(list_numbers))

print(f"List without duplicates: {list_numbers}")