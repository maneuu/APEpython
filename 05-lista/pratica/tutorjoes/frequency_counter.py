import collections
l = [10,30,50,10,20,60,20,60,40,40,50,50,30]
print("Original List : ",l)
# Count the frequency of the elements in the list using the Counter() method from the collections module and store it in a variable f
f = collections.Counter(l)
print("Frequency of the Elements: ",f)