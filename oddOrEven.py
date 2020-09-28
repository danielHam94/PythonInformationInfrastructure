# Daniel Ham
# Odd or Even


# Input number to check if odd, even, or neither
number = eval(input("Please enter a number: "))


# If-else statements to check if number is odd, even, or neither
if number % 2 == 0:
    print("Even number detected.")
elif number % 2 == 1:
    print("Odd number detected.")
else:
    print("Brace yourself - that's not a whole number")
