# Daniel Ham
# Top 100 Movies

# ***********************INSTRUCTIONS***********************
# Download top100moviesAFI.txt and top100moviesRT.txt from Canvas. 
# 
# These contain the Top 100 Movies from the American Film Institute
# and Rotten Tomatoes, respectively.
# 
# Write a program that figures out which movies appear on both lists. 
# Sets make this easy!
# 
# BONUS POINT: Alphabetize your output
# **********************************************************

# Open and create set of afi movies
with open('top100moviesAFI.txt', 'r') as f:
    afi_movies = set(f.readlines())

# Open and create set of rt movies
with open('top100moviesRT.txt', 'r') as g:
    rt_movies = set(g.readlines())




print("The movies on both lists are: ")

# Print each movie that is found in BOTH sets of movies
for movie in sorted(afi_movies & rt_movies):
    print(movie.strip())




