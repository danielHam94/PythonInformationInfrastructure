# Daniel Ham
# Dasher2

# ***************************** INSTRUCTIONS *****************************
# Write a function that takes a string and returns that string
# with some number of "-" to either side,
# such that the total length of the line is always 20. 
# If the original string is more than 20 characters long,
# return an error message with dashes.
# If there’s an odd number of dashes, put them on the right. 
# ************************************************************************

# Function that creates a string with dashes between each letter
def dasher(string):
    
    if len(string) > 20:
        string = "Error"
        
    numberOfDashes = 20 - len(string)
    dashesEven = numberOfDashes // 2
    dashes = "-" * dashesEven
    
    if len(string) % 2 == 0:
        newString = dashes + string + dashes
    else:
        newString = dashes + string + dashes + "-"

    return newString

# Main
print(dasher("Hello"))
print(dasher("Welcome"))
print(dasher("super long string test man"))



        
    
