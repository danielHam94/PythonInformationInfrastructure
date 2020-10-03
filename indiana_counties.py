## Daniel Ham
## IN Counties pt 1

## ******************** INSTRUCTIONS ********************
## Download INCounties2015.txt – this file contains statistical data
## about the population of Indiana’s counties in 2015.
## Write a program that can loadthis data into a dictionary.
## ******************************************************



## Dictionary list
pop_dictionary = {}
## open file and read file
with open("INCounties2015.txt", "r") as f:
    pop_IN = f.readlines()
    
## For loop to go through each data and split to add to dictionary
for data in pop_IN:
    county, pop = data.split("\t ")
    pop_dictionary[county] = int(pop.replace(",","").strip())
    

## Check output
print(pop_dictionary)
