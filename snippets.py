# Daniel Ham
# Snippets

# *********************** INSTRUCTIONS ***********************
# Write a program (using Interactive Mode or Script Mode) that gets a string,
# then three index positions in that string. Finally,
# it prints out the characters that match those index positions.
# ************************************************************

# Get input of favorite food
favorite_food = input("Enter your favorite food: ")

# Get input of the index position
first = int(input("Enter first index position: "))
second = int(input("Enter second index position: "))
third = int(input("Enter third index position: "))

# String to create new word
new_word = ""

# Add to string
new_word = favorite_food[first] + favorite_food[second] + favorite_food[third]

# Print output of new favorite food
print("Your new favorite food is: " + new_word, ".")
