# Daniel Ham
# Temperatures 2

# Input temperature for conversion
temperature = eval(input("Please enter a temperature: "))

# Input metrics to convert to
metric = input("Would you like that converted to C or F? ")

# Formulas to convert temperature
convert_CtoF = temperature * (9 / 5) + 32
convert_FtoC = (temperature - 32) * (5/9)

if metric == 'F':
    print("The converted temperature is ", convert_CtoF, "F")
elif metric == 'C':
    print("The converted temperature is ", convert_FtoC, "C")
else:
    print("You didn't enter C or F!")
