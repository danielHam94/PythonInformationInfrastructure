def open_file(filename):

    while True:
        try:
            in_file = open(filename, "r")
            lines = in_files.readlines()
            in_file.close()
        except:
            filename = input("That filename doesn't exist. Please enter a filename: ")
        else:
            break

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    return lines
        
        

#main

data = open_file("doesn'texist.txt")
print("The contents of the file:")
print(data)
