from tools import *

class Puppy(object):
    """Puppy"""

    names = {}

    # Methods

    @staticmethod
    def dog_names():
        table_print(("Name", "Times"), sorted(Puppy.names.items()), 7)

    def __init__(self, name = "Spot"):
        self.name = name
        self.counter = 0
        if name in Puppy.names:
            Puppy.names[name] += 1
        else:
            Puppy.names[name] = 1
            

    # str method
    def __str__(self):
        reply = "\nPuppy Object\n"
        reply += "Puppy Name: " + self.name + "\n"
        reply += "Bark Count: " + str(self.counter) + "\n"
        return reply

    # bark method
    def bark(self):
        self.counter += 1
        print("Bark")
        print(self.name, "has barked", self.counter, "time(s).")


# main
dog1 = Puppy("Spot")
dog2 = Puppy("Rover")
dog3 = Puppy("Spot")
dog4 = Puppy("Rover")
dog5 = Puppy("Rover")
dog6 = Puppy("Lassie")

Puppy.dog_names()

