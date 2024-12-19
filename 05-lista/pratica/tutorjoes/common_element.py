"""
Write a Program that get two lists as input and check if they have at least one common member

Sample Output

[1,2,3,4,5]

[5,6,7,8,9]

Lists have at least one common member

"""
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
# Find the common elements in the lists
# set() function is used to convert the list to a set to find the common elements & operator is used to find the common elements in the lists 
common_word = list(set(list1) & set(list2))
print(f"Common elements in the lists: {common_word}") if common_word else print("No common elements in the lists")

# or

list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
result = False
for x in list1:
    for y in list2:
        if x == y:
            result = True
            print(f"Common element: {x}")
if result:
    print("Lists have at least one common member")
else:
    print("Lists do not have any common member")