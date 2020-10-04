# Daniel Ham
# Marathon

# **********************INSTRUCTIONS**********************
# Use the two Top 100 movie files to implement this program,
# which shows the user a random listing of movies for a marathon.
# 
# Movies should be drawn from both Top 100 files at random but
# without creating duplicates in your movie pool!
# ********************************************************

import random

# Open and create set of afi movies
with open('top100moviesAFI.txt', 'r') as f:
    afi_movies = set(f.readlines())

# Open and create set of rt movies
with open('top100moviesRT.txt', 'r') as g:
    rt_movies = set(g.readlines())

# Create movie list which carries both movies
movie_list = []
for movie in sorted(afi_movies & rt_movies):
    movie_list.append(movie.strip())

# Get input of how many movies
movie_count = input("How many movies in your marathon? ")
print()
print("Your custom", movie_count, "marathon:")

# For loop to iterate the count of random movie from the list
for i in range(int(movie_count)):
    print(random.choice(movie_list))
