num = ["Hello", 34, 45, '', 40]
print(f"List before removing empty strings: {num}")
while("" in num):
    num.remove("")

print(f"List after removing empty strings: {num}")