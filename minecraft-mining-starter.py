import minecraft

## Part Two: Mine stuff
def dig(mine):
	
        # We'll return anything we found as a dictionary
	# {name_of_ore : count}
	materials_found = {}

	# First ask how deep to dig.
	# Print out input to test this part of your program
	# Use try/except for this part
	# If the user doesn't enter expected input, quit out by returning {}
	try:
                depth = int(input("How deep would you like to dig? "))
                if(depth < 10) or (depth > 100):
                        print("Please choose a depth between 10 and 100.")
                        return{}
        except NameError:
                print("Try again. You did not enter a number.")
                return{}
        else:
                print(depth)

                

	# Then, do the digging.
	# Note: this code should only run if the "how deep" checks out


	return(materials_found)


## Main

# 1A: READ IN MATERIALS LIST
try:
        file = open("mining_list.txt", "r")
        materials = file.readlines()
        file.close()
except:
        print("Materials not found.")
else:
        print("Materials found.")


# 1B: CREATE MINE
# Hint: temporarily print out your mine to see what the list looks like
# Module function create_mine returns a random list of materials 
# The length of this list will be between 10 and 100 materials
print(minecraft.create_mine(materials))



# 2: MINE MATERIALS


# 3: LOOK THROUGH THE LOOT
# If you found some ore, did you find any rare items 
# like obsidian, diamonds or gold?





