# Daniel Ham
# Vowel Counter

# ************************** INSTRUCTIONS **************************
# This program has errors in it. When we run it, we should get:
# >>> 
# The message has 13 vowels in it.
# It also has 2 ys in it.
# ******************************************************************

# Added : at the end
def vowel_count(string):
    count = 0
    y_count = 0

    # Added .lower() to match lowercase and changed 'as' to 'in'
    for letter in string.lower():
        if letter in vowels:
            count += 1
        # Changed != to ==
        elif letter == "y":
            y_count += 1
    # Changed to return two values
    return count, y_count

# Main
# Quoted the strings
vowels = ['a','e' ,'i' ,'o' ,'u']

# Added quotation at the end
message = "This is a test message. This is only a test. Only!"

# Added 'message' to the function
total, ys = vowel_count(message)
print("The message has", total, "vowels in it.")
print("It also has", ys, "ys in it.")

