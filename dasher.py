# Daniel Ham
# Dasher

# ***************************** INSTRUCTIONS *****************************
# Write a function that takes a string and returns (not just prints!)
# that string with "-" around and between each character. 
# ************************************************************************

# Function that creates a string with dashes between each letter
def dasher(string):
    newString = "-"

    for letter in string:
        newString += letter + "-"

    return newString

# Main
print(dasher("Hello"))
print(dasher("Greetings"))
print(dasher(dasher("TEST?")))



        
    
