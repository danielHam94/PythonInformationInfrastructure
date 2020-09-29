# Daniel Ham
# Disemvoweler

# ********************INSTRUCTIONS********************
# Prompt the user for some text.
# Remove all the vowels from it, and print it back to the user. 
# ****************************************************

# Get input of string
text = input("Please enter some text: ")

# Create vowel variable string
vowels = "aeiou"

# Create a new string that have vowels removed
newText = ""

# For loop to iterate and remove vowel
for i in range(len(text)):
    if text[i] not in vowels:
        newText += text[i]
    

# Output the value of the new string without vowels
print("With the vowels removed: ", newText)
