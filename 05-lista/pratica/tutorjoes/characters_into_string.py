
"""
This script converts a list of characters into a string.
The script contains two lists of characters:
1. list_of_characters: ['T','u','t','o','r',' ','J','o','e','s']
2. list_of_characters2: ['R','a','i','n','b','o','w',' ','C','o','l','o','r','s']
It then converts these lists into strings using the join() method and prints the results.
The join() method is used to concatenate the elements of the list into a single string. 
It takes one parameter: the separator (in this case, an empty string '').
The method iterates over each element in the list and joins them together with the specified separator.
"""

list_of_characters = ['T','u','t','o','r',' ','J','o','e','s']
list_of_characters2 = ['R','a','i','n','b','o','w',' ','C','o','l','o','r','s']
print(f"List of characters 1: {list_of_characters}")
print(f"List of characters 2: {list_of_characters2}")

# Convert the list of characters into a string

string = ''.join(list_of_characters)
string2 = '_'.join(list_of_characters2)
print(f"Result 1: {string}")
print(f"Result 2: {string2}")