import random
#create a deck of cards and randomly print 2 cards
class Card:
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Clovers']
    values = ['Ace', 'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    card_values = {'Ace': 1, 'King': 10, 'Queen': 10, 'Jack': 10, '2': 2, '3': 3, '4': 4, '5':5, '6':6, '7':7,'8':8, '9':9, '10':10}

    def __init__(self, value, suit, card_value):
        self.value = value
        self.suit = suit
        self.card_value = card_value

