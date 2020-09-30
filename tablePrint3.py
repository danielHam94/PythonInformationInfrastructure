# Daniel Ham
# Table Print 3

# Function to print tables

def table_print(name, data, width):
    print(name[0],name[1], sep="\t")
    print("-" * width * 2)

    output = "{:>{}} {:>{}}"

    print("-" * (width + 1) * 2)

    for i in range(len(data)):
        print(output.format(data[i][0], data[i][1], width))

    print("")








# main - Don't change this part!
labels = ["Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores, 6)

labels2 = ["Capital", "State"]
state_data = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels2, state_data, 8)
