## Daniel Ham
## Dictionary

## *********************INSTRUCTIONS*********************
## Prompt the user for a key.
## If the key doesnt exist, print a "Not Found" message
## and prompt the user for a definition. Add it to the dictionary.
## Whether the key was found or added, print the definition.
## Bonus Point: Place everything inside a loop so that you can keep
## adding more information. Make sure the user can escape your loop when done!
## *****************************************************

python_words = {"string": "a sequence of characters", \
                   "int": "a whole number (integer) "}

#add your code here

## while true:
while True:
    ## Get input from user to find a definition
    key = input("Enter a value to find the definition:")
        ## if input = stop
    if key.upper() == 'STOP':
        ## break
        break
    ## if statement to find key in library
    elif key in python_words:
        ## print definition
        print(python_words[key])
    ## else
    else:
        ## print not found
        print("Not found!")
        ## ask user for definition
        key_def = input("Enter the definition of the value: ")
        ## add to library
        python_words[key] = key_def
        ## print definition
        print(python_words[key])
