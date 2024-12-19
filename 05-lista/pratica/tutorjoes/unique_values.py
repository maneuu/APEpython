l = [ 82,4,10,56,78,4,34,5,10,9]
print("Original List : ",l)
# set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set.
s = set(l)
print(f"Unique Numbers : {s}")
new_list = list(s)
print("Unique Numbers : ",new_list)
