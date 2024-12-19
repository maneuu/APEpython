# Given a list of numbers. write a program to turn every item of a list into its square.

numbers = [1, 2, 3, 4, 5, 6, 7]
square = []
for item in numbers:
    square.append(item**2) #or square.append(i * i)
print(square)