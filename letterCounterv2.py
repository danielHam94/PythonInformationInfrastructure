# Daniel Ham
# Letter Counter v2

# ********************INSTRUCTIONS********************
# Write a program that asks the user to give you a lowercase string,
# and a letter that might be in the string.
# USE A LOOP to tell them how many times that letter occurs.
# Change your program to also inform the user where the letter was found
# ****************************************************


# Get a lower string
string = input("Please enter a string in lowercase: ")

# Get input of letter to find
letter = input("What letter are you looking for: ")

# Variable to carry count of letter in string
counter = 0

# Iterate through each character of word and add to counter if it matches
for i in range(len(string)):
    if letter == string[i]:
        print(letter, "found at position", i)
        counter += 1
    
# Output of number of letters
print(letter, "was found", counter, "times!")
