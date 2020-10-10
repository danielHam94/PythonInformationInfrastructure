class Puppy(object):
    """Puppy"""

    # Methods
    def __init__(self, name = "Spot"):
        self.name = name
        self.counter = 0

    # str method
    def __str__(self):
        reply = "\nPuppy Object\n"
        reply += "Puppy Name: " + self.name + "\n"
        reply += "Bark Count: " + str(self.counter) + "\n"
        return reply

    # barl method
    def bark(self):
        self.counter += 1
        print("Bark")
        print(self.name, "has barked", self.counter, "time(s).")



# main
puppy1 = Puppy()

for i in range(5):
    puppy1.bark()

print(puppy1)

