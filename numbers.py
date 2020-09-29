# Daniel Ham
# Numbers



# Function to find the max and min of the numbers
def max_min():
    listOfNumbers = eval(input("Please enter a list of numbers [x, y, z]: "))
    maxOfNumbers = max(listOfNumbers)
    minOfNumbers = min(listOfNumbers)

    print("The largest number is ", maxOfNumbers, ".")
    print("The smallest number is ", minOfNumbers, ".")

# Main
max_min()
