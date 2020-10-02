# Daniel Ham
# Donut Starter

# Main

# Get donut count
donuts = eval(input("Aaron, Beth, and Cody go out for donuts." + \
                    "How many donuts do they buy?: "))

# Loop till donut counts are less than 3
while donuts >= 3:
    print("Aaron takes a donut.")
    print("Beth takes a donut.")
    print("Cody takes a donut.")
    donuts -= 3

# Leftover donuts
if donuts != 0: 
    print("There are", donuts, "left!")	#Here we trace!
else:
    print("They took all the donuts!")
