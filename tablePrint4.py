# Daniel Ham
# Table Print 4

def tablePrint(headers, data, width):


    output = "{:{}} {:{}}"

    print(output.format(headers[0], width, headers[1], width))

    print("-" * (width + 1) * 2)

    for item in data:
        print(output.format(item[0], width, item[1], width))
    print()

# Main
labels = ["Nest", "Eggs"]
nests = []

longest = 0

for i in range(4):
    dinoName = input("\nPlease enter the dinosaur's name: ")
    eggCount = input("Please enter how many eggs were found: ")
    nests.append((dinoName, eggCount))

    if len(dinoName) > longest:
        longest = len(dinoName)

    if len(eggCount) > longest:
        longest = len(eggCount)


    print("Current fossilized dinosaur egg count: \n")
    tablePrint(labels, nests, longest + 2)
