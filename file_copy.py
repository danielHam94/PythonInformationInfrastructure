# Daniel Ham
# File Copy

# *************************INSTRUCTIONS*************************
# Write a function, copy_file(filename_from, filename_to)
# that copies the contents of a file to another file.
#  Get started with copy_test.py on Canvas!
# NOTE: This function doesn’t need to produce output in IDLE!
# It copies the file, producing a new file
# **************************************************************

def copy_file(filename_from, filename_to):
    text_file = open(filename_from, "r")
    data = text_file.read()
    text_file.close()

    text_file = open(filename_to, "w")
    file.write(data)
    file.close()

# Alternative method
#    with open(filename_from, "r") as f:
#        data = f.read()
#
#    with open(filename_to, "w") as f:
#        f.write(data)


# Main

file_f = input("Please enter the name of the file to copy from: ")
file_t = input("Please enter the name of the file to copy to: ")

copyfile(file_f, file_t)

    







    
