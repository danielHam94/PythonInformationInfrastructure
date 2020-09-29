# Daniel Ham
# Dasher3

# Method
def dasher3(string = "Default" , length = 20):
    count = len(string)
    dashCount = length - count
    dashEachSide = dashCount // 2
    formatted = ""
    if count <= length:
        if count % 2 == 0:
            formatted += "-" * dashEachSide + string + "-" * dashEachSide
        else:
            formatted += "-" * dashEachSide + string + "-" * dashEachSide + "-"
    else:
        formatted += "-" * 7 +"Error" + "-" * 8

    return formatted


## Main
print(dasher3("Hello", 10))
print(dasher3("Welcome", 15))
print(dasher3("Super long string test"))
