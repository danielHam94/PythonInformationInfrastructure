# Daniel Ham
# Top 100 Movies


# Load file
with open("top100moviesRT.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

# Print that the file has been loaded
print("The file 'top100moviesRT.txt' has been loaded.")
print("It contains the Top 100 movies of all time, according to Rotten Tomatoes.")

# While loop until stop
while True:
    # Get input of movie title
    title = input("Please enter a movie title (or STOP): ")

    if title.upper() == 'STOP':
        break

    found = False

    # If movie title in list
    for i in range(len(lines)):
        # Print index
        if lines[i] == title:
            print("That's the #", i, "movie of all time.")
            found = True

    if not found:
        print("I couldn't find that movie in the list.")
            
        

    # Else
        # Cant find movie in the list
    

    
