class Robot(object):

    def __init__(self, name, weapon, strength):
        print("Robot created!", name, "\n")
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.online = True

    def __str__(self):
        reply = "-" * 20 + "\n"
        reply += "Fighting Robot\n"
        reply += "Name: " + self.name + "\n"
        reply += "Weapon: " + self.weapon + "\n"
        reply += "Strength: " + str(self.strength) + "\n"
        if self.online:
            reply += "Status: ONLINE\n"
        else:
            reply += "Status: OFFLINE\n"
        reply += "-" * 20 + "\n"
        return reply

#main
r2d2 = Robot("R2D2", "Beeps", 2)
c3p0 = Robot("C3P0", "Conversation", 2)

print(r2d2)
print(c3p0)
