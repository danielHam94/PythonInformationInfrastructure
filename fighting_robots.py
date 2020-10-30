class Robot(object):

    robot_list = []

    @static method
    def contendors():
        robots = len(Robot.robot_list)
        print("There are ", robots, "robots.")
        if robots:
            print("Here is a list of them:\n")
            for robot in Robot.robot_list:
                print(robot)

    def __init__(self, name, weapon, strength):
        print("Robot created!", name, "\n")
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.online = True
        Robot.robot_list.append(self)

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
