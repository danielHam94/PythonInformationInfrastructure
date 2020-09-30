# Daniel Ham
# Word Triangle

# ******************************INSTRUCTIONS******************************
# Use slicing to write a program that can replicate this exchange:
# ************************************************************************

def wordTriangle(message):

    for i in range(len(message)):
        print(message[:i+1])

# Main

# Get input from user
message = input("Please enter a message: ")
# Return results with function
wordTriangle(message)
    
