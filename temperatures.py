# Daniel Ham
# Temperatures

# Input temperature for conversion
temperature = eval(input("Please enter a temperature: "))

# Formulas to convert temperature
convert_CtoF = temperature * (9 / 5) + 32
convert_FtoC = (temperature - 32) * (5/9)

# Output the converted temperatures
print(temperature, "F is", convert_FtoC, "C.")
print(temperature, "C is", convert_CtoF, "F.")
