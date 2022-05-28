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
                self.deck.append(Card(value, suit, card_values[value]))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return 'The deck has:' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.aces = 0
        #self.value = 0

    def add_card(self,card):
        self.cards.append(card)
        #self.value += values

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())

for card in test_player.cards:
    print(card)
