## Daniel Ham
## IN Counties pt 2

## ******************** INSTRUCTIONS ********************
## Further develop the dictionaries to output the counties of Indiana
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
    

## Print counties of Indiana
print("The counties in Indiana are: \n", ", ".join(sorted(pop_dictionary.keys())))
print()
print("The population of Monroe Count as of 2015 was:", pop_dictionary.get("Monroe"))
print("The total IN population as of 2015 was: ", sum(pop_dictionary.values()))
print("So Monroe County accounts for", 100 * (pop_dictionary["Monroe"]/ sum(pop_dictionary.values())), "% of IN's population.")

