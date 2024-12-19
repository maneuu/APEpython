num = [22,'PythonLobby',22.3,1>0, 1+2, 1+2j, {1,2,3}, (1,2,3), [1,2,3],{'a':1,'b':2},None]
print(f"Original list: {num}\n")

for i in range(len(num)):
    print(f"Type of {num[i]} is {type(num[i])}")
