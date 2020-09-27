# Daniel Ham
# Surface Area 1


# *************************** INSTRUCTIONS ***************************
# Write a similar program that calculates the surface area of a cylinder.
# Remember, you can use math.pi if you’ve imported the math module.
#
# You can test your program with a cylinder of radius 5 and height 8. 
# The surface area should be 408.4070449666731
# *************************** INSTRUCTIONS ***************************


import math

# Variables of radius and height
r = 5
h = 8

# Surface Area of a Cylinder
cylinderSA = 2 * (math.pi * (r **2)) + math.pi * r * 2 * h

# Output result
print(cylinderSA)
