class Puppy(object):
    """A virtual puppy"""

    def __init__(self, name):	
        self.__name = name
        self.__barkCounter = 0

    def __str__(self):
        reply = "\nPuppy object\n"
        reply += "Name: " + self.__name +"\n"
        reply += "Bark Counter: "
        reply += str(self.__barkCounter) + "\n"
        return reply

    def bark(self):
        self.barkCounter += 1
        print("Bark!")
        print(self.__name, "has barked",
              self.__barkCounter, "time(s).\n")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            print("Name change successful.")
        else:
            print("Name can't be blank.")

#main
dog1 = Puppy("Spot")

dog1.set_name("")
print(dog1.get_name())
dog1.set_name("Rex")
print(dog1.get_name())
