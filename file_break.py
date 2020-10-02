# Daniel Ham
# File Break


while True:
    file_name = input("Please enter a file name or STOP: ")

    if file_name.upper() == 'STOP':
        break

    with open(file_name, "r") as f:
        lines = f.readlines()
        
    print(file_name, "has", len(lines), "lines of data in it!\n")


    

    
