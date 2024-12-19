# List of words and numbers as strings
word=["madem","3643","apple","3756"]

# Initialize a counter to zero
ch = 0

# Iterate through each word in the list
for w in word:
    # Check if the length of the word is greater than 1 and the first and last characters are the same
    if len(w) > 1 and w[0] == w[-1]:
        # Increment the counter if the condition is met
        ch += 1

# Print the final count
print(ch)