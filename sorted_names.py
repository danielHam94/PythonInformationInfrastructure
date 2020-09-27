# Daniel Ham
# Sorted Names

# Create a string variable that contains all the last (family) names of your group members, separated by spaces.
last_names = "Ham Kim Jones"

# Convert this value to a list of characters.
letters = list(last_names)
print(letters)

# Sort the list of characters.
letters.sort()
print(letters)

# Use .join() to re-assemble the characters into a string.
"".join(letters)
print(letters)
