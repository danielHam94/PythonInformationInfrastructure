# pass is used to prevent Python from throwing an error
# when a method has no code. You can remove it when you
# implement each method. There is a LOT of test code below.

class Fish(object):

    def __init__(self, name, length):
        #your code here
        pass

    def __str__(self):
        #your code here
        return "Replace this with better code!"

    def __gt__(self, other):
        #your code here
        pass

    def catch(self):
        #your code here
        pass

# Comment parts of this test code in as you implement them above

# test code for Part 1 ONLY
fish1 = Fish("Bass", 10)
fish2 = Fish("Goldfish", 2)
fish3 = Fish("Shark", 50)
print(fish3)

# This is the rest of the test code for Part 1, but it's easier
# to test without it first.

##
##print(fish1.name, "is longer than", fish2.name, ":", fish1 > fish2)
##print(fish1.name, "is longer than", fish3.name, ":", fish1 > fish3)
##print()
##
##fish1.catch()
##fish1.catch()


### test code for Part 2 - delete above test code

##fish1 = Fish("Bass", 10)
##fish2 = Fish("Goldfish", 2)
##fish3 = Fish("Shark", 50)
##Fish.remaining()
##Fish.largest()
##fish1.catch()
##Fish.remaining()

### test code for Part 3 - delete above test code

##fish1 = StealthFish("007", 11)
##fish2 = FancyFish("Lord","Grantham", 10)
##fish3 = NiceFish("Nemo", 3)
##fish1.catch()
##fish2.catch()
##fish3.catch()
##fish3.release()
##fish3.release()
##Fish.remaining()


