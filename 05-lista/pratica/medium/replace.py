list1 = [20,5, 10, 15, 2, 25, 50, 2]
print(f"LISTA ATUAL:\n {list1}")
if 20 in list1:
    print("Numero 20 existe na lista// substituindo o numero 20 pelo 200")
    list1[list1.index(20)] = 200

print(f"LISTA APOS MODIFICAÇÃO:\n{list1}")
