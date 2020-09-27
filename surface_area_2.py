## Daniel Ham
## Surface Area 2

## *********************** Instructions ***********************
##Re-write your surface area program in Script Mode:
##Prompt the user for the values to be stored in radius and  height.
##You’ll still need to import the math module,
##and you will need to convert the data from a string to an integer and back!
## ************************************************************

import math

## Get input of radius and height
print("This is a program that finds the surface area of a cylinder")
r = int(input("Enter the radius: "))
h = int(input("Enter the height: "))

## Function to find the cylinder surface area
cylinderSA = 2 * (math.pi * (r ** 2)) + math.pi * r * 2 * h

## Output of the surface area of the cylinder
print("The surface area of the cylinder is " + str(cylinderSA) + ".")







