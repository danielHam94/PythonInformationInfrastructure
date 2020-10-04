# Daniel Ham
# Data Read v1

# **********************INSTRUCTIONS**********************
# Download professions.txt
# Produce this output:
# ********************************************************

# Open file and read lines
with open('professions.txt', 'r') as f:
    people = f.readlines()

# Create list of people and append
person_list = []
for person in people:
    person_list.append(person.strip().split(", "))

sorted_data = [person_list.pop()]

while person_list:
    person = person_list.pop()

    inserted = False

    for i in range(len(sorted_data)):

        if int(person[1]) < int(sorted_data[i][1]):
            sorted_data.insert(i, person)

            inserted = True
            break
    if not inserted:
        sorted_data.append(person)

for entry in sorted_data:
    print(entry)

    

##print(sorted_data)

# Print each person in the list
##for person in person_list:
##    print(person)
##
## print all the data
##print("\nAll the data: ")
##print(person_list)

