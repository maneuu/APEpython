a=[1,2,4,3,6,7,5,8,9,7,8,9,10]
odd_num=[]
for i in a:
	if(i%2==1):
		odd_num.append(i)
print(odd_num)

# or

a=[1,2,4,3,6,7,5,8,9,7,8,9,10]
odd_num=[i for i in a if i%2==1]
print(odd_num)
