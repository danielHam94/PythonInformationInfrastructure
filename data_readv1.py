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

# Print each person in the list
for person in person_list:
    print(person)

## print all the data
print("\nAll the data: ")
print(person_list)

