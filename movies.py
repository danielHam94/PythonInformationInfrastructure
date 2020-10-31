class Movie(object):
    def __init__(self, title, rating):    	# Constructor
        self.title = title
        self.rating = rating

    def __str__(self):		# to – string method
        return self.title + "is rated" + str(self.rating) + "/10"
     
class Action(Movie):
    def content(self):
        return 'Explosion'
 
class Comedy(Movie):
    def content(self):
        return 'Crass Humor'

class Drama(Movie):
    def content(self):
        return 'Serious Moments'
 
#main
movies = [Action('Mad Max: Fury Road', 9), Comedy('Tucker & Dale vs. Evil', 7), Drama('The Imitation Game', 8)]

for movie in movies:
 print(movie, "It has lots of", movie.content())

