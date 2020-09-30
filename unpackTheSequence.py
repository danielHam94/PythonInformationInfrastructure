# Daniel Ham
# Unpack the Sequence


# **************************INSTRUCTIONS**************************
# Use unpacking and the .format() method to print the data
# about each dinosaur in a nicely spaced table.
# Note: you might have to convert the weight to a string
# to get it to play nice when printing.
# ****************************************************************


# Function to create display chart of dinosaurs
def dinosaurCall(dinosaurs, headers):
    output = "{0:20} {1:<15} {2:15} {3:20}"

    print(output.format(headers[0], headers[1], headers[2], headers[3]))
    print("-" * 72)

    for dinosaur in dinosaurs:
        name, weight, diet, time = dinosaur
        print(output.format(name, weight, diet, time))



# Main

# List
title = ["Name", "Weight(lbs)", "Diet", "Time"]
dinosaursList = [["Tyrannosaurus", 16000, "carbivore", "Late Cretaceous"],
                ["Ankylosaurus", 10000, "herbiore", "Late Cretaceous"],
                ["Stegosaurus", 6000, "herbivore", "Late Jurassic"],
                ["Deinonychus", 175, "carbivore", "Early Cretaceous"]]

# Call function
dinosaurCall(dinosaursList, title)
