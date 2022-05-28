import random

suits = ['Hearts', 'Clubs', 'Diamonds', 'Clovers']
values = ['Ace', 'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_values = {'Ace': 1, 'King': 10, 'Queen': 10, 'Jack': 10, '2': 2, '3': 3, '4': 4, '5':5, '6':6, '7':7,'8':8, '9':9, '10':10}

class Card:
    def __init__(self, value, suit, card_value):
        self.value = value
        self.suit = suit
        self.card_value = card_value

    def __str__(self):
        return f'{self.value} of {self.suit}. Value: {self.card_value}'

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for value in values:
                for card_value in card_values:
                    self.deck.append(Card(value, suit, card_values[value]))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        pass