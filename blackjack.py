# Daniel Ham
# Blackjack

# Create variable of list of cards, sum, and number of cards
card_list = []
sum_of_cards = 0
number_of_cards = 0

# Loop while total < 21 and card != 3
while (sum_of_cards < 21) and (number_of_cards != 3):
    
    # get card value input from user
    card_value = eval(input("Please enter a card value: "))
    # add card value to list
    card_list.append(card_value)
    # add card sum
    sum_of_cards = sum(card_list)
    number_of_cards = len(card_list)

# print final hand list of cards
print("Your final hand is:", card_list)
# print value
print("Its value is: ", sum_of_cards)

# if sum > 21, = 21, < 21
if sum_of_cards > 21:
    print("Too high!")
elif sum_of_cards == 21:
    print("Perfect!")
else:
    print("Not bad!")
