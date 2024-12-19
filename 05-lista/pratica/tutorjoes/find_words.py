# Write a Python program to find the list of words that are longer than n from a given list of words

# List of words
word = ['Words', 'Longer', 'given', 'Words', 'list', 'words', 'a', 'list', 'words', 'longer', 'than', 'n', 'from', 'a', 'given', 'list', 'words']
# Initialize a counter to zero
ch = 4
# Initialize an empty list to store the words that are longer than n
longer_words = []
# Iterate through each word in the list
for w in word:
    # Check if the length of the word is greater than n
    if len(w) > ch:
        # Append the word to the list if the condition is met
        longer_words.append(w)

# Print the list of words that are longer than n
print(longer_words)