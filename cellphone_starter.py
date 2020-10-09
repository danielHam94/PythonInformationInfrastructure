class CellPhone(object):
    """A virtual cell phone"""

    #add your code here, as described below
    def __init__(self, owner, minutes):
        self.owner = owner
        self.minutes = minutes

    def info(self):
        print("My owner is", self.owner + ".", self.owner, "has", self.minutes, \
           "minutes left.")

    def compare(self, other):
        if self.minutes > other.minutes:
            print(self.owner, "has more minutes.")
        elif other.minutes > self.minutes:
            print(other.owner, "has more minutes.")
        else:
            print("Minutes are equal.")

#main section of the code
phone1 = CellPhone("Amelia", 500)
phone1.info()

phone2 = CellPhone("Bob", 300)
phone2.info()

phone1.compare(phone2)




