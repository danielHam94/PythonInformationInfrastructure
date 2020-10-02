# Daniel Ham
# File Sum

numbers_file = open("numbers.txt","r")
lines = numbers_file.readlines()
numbers_file.close()

total = 0

for num in lines:
    total += int(num)

print("The total is ", total, ".")
