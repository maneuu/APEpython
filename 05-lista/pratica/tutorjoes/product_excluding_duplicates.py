a = [2,1,2,4,6,4,3,2,1]
print (f"Original list : {a}")
 
b=list(set(a))
print(f"List after removing duplicates : {b}\n")
p=1
for i in b:
	p*=i
 
print (f"Product of the list excluding duplicates : {p}")