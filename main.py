# TASK: Write a function that reverses a word and capitalizes it.

# Define a function that takes a string parameter
def get_word(word):
# Create an empty string to store the reversed word
    reversed_word=""
# Loop through each character in the word
    for char in word:
        reversed_word=char+reversed_word
# Add each character to the front of the new string
    return reversed_word.upper()
# Convert the reversed word to uppercase
# Return the final result
# Prompt the user for input and call the function
new_word=get_word(input('enter your word '))
# Display the transformed word
print(new_word)