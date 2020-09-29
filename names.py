# Daniel Ham
# Names

# Function that finds frequent names in the list
def frequentNames(nameList):
    ## Variables to carry count and name of highest occuring name
    freqName = ""
    freqCount = 0
    
    ## for loop to iterate through name list
    for name in nameList:
        if nameList.count(name) > freqCount:
            freqCount = nameList.count(name)
            freqName = name

    ## Return result
    return freqName




    






## Main


## Get a list of names
listOfNames = eval(input("Please enter a list of names ['x', 'y', 'z']: "))
## Function to get results
print("The most frequently occuring name is:", frequentNames(listOfNames))
