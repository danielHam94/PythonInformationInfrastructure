# Daniel Ham
# Table Print 2

# Function to print tables

def table_print(name, data):
    print("i",name[0],name[1], sep="\t")
    print("-" * 25)

    for i in range(len(data)):
        print(i, data[i][0], data[i][1], sep = "\t")

    print("")








# main - Don't change this part!
labels = ["Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores)

labels2 = ["Capital", "State"]
state_data = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels2, state_data)
