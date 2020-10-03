scores = {"Dan": 125, "Abby": 100, "Carrie": 275, "Ben": 150}

print("Current players:")

# How could we get this to print out without the [ ] and '' ?
for player in sorted(scores.keys())):
    print(player, end = " ")
print()

# Ask the user for a name
name = input("Please enter a Player Name: ")

# Use that name to look up the player or print 'Not found'
print("The score for", name, "is", scores.get(name, "not found."))
