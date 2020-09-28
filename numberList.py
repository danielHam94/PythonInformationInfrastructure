# Daniel Ham
# Number List

# Input list of numbers
numberList = eval(input("Please enter a list of numbers [x,y,z,etc]: "))

largestNumber = max(numberList)
smallestNumber = min(numberList)

# Print the largest and smallest number in the list
print("The largest number in your list is: ", largestNumber)
print("The smallest number in your list is: ", smallestNumber)

# Input number to add or remove
numberAddRemove = input("Would you like to Add a number or Remove one? [Add,Remove] ")

# If-else statement to add, remove number and print new list
if numberAddRemove == "Add":
    addNumber = eval(input("What is the new number? "))
    numberList.append(addNumber)
    print("The new list is: ", numberList)
elif numberAddRemove == "Remove":
    removeNumber = eval(input("What number should we remove? "))
    if removeNumber in numberList:
        numberList.remove(removeNumber)
        print("The new list is: ", numberList)
    else:
        print("That number isn't in the list!")
else:
    print("That's not a valid choice!")
    
