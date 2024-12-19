list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

print("Elementos em comum:")
for i in list_a:
    if i in list_b:
        print(i)
        
print("-"*30)

# OU 

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

# O operador & em Python, quando aplicado a conjuntos, retorna um novo conjunto contendo apenas os elementos que estão presentes em ambos os conjuntos.

# A função list torna os conjuntos de volta para uma lista
common = list(set(list_a) & set(list_b))
print("Elementos em comum:")
print(common)