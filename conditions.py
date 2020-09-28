# Daniel Ham
# Conditions


# *************************** INSTRUCTIONS ***************************
# Write a program that can do this,using if and elsestatements.
# ********************************************************************

# Get input from user 
print("What would you like to do this weekend?")
to_do = input("Do you want to go to the park or to a movie? ")


if to_do == "park":
    print("Great! Let's go!")
elif to_do == "movie":
    enough_money = input("Is it true that we have enough money for tickets? [True, False] ")
    if enough_money == "True":
        print("Excellent! Bring on the popcorn. ")
    else:
        print("That's ok. It's a nice day for the park.")
else:
    print("That's not something we can do this weekend.")
