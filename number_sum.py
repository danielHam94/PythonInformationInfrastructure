# Daniel Ham
# Number Sum


num_list = []

while True:
    num = input("Please enter a number or STOP: ")

    if num.upper() == 'STOP':
        break
    num_list.append(int(num))
    
print("The total sum is", sum(num_list))

    
