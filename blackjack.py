import random
import pyinputplus as pyip

suits = ['Hearts', 'Clubs', 'Diamonds', 'Clovers']
values = ['Ace', 'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_values = {'Ace': (1,11), 'King': 10, 'Queen': 10, 'Jack': 10, '2': 2, '3': 3, '4': 4, '5':5, '6':6, '7':7,'8':8, '9':9, '10':10}

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
    
    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self,card):
        self.cards.append(card)

    def eval_val(self):
        for card in self.cards:
            if card.value == 'Ace':
                while True:
                    print('Choose 1 or 11')
                    choice = input('> ')
                    if choice == '1':
                        self.value += 1
                        break
                    elif choice == '11':
                        self.value +=11
                        break
                    else:
                        print('Invalid Input')
                        continue
            else:
                self.value += card.card_value

class Bet:
    def __init__(self):
        self.wallet = 100
        self.bet = 0

    def __str__(self):
        return f'Player Has: ${self.wallet}'

    def bettype(self):
        print('Amount to Bet:')
        print('Minimum Bet: $5 & Maximum Bet: $2000')
        while True:
            amt = pyip.inputNum(min=5, max=2000)
            if amt > self.wallet:
                print('Invalid Bet')
                continue
            else:
                self.currentbet += amt
                break
    
    def win_bet(self):
        #edit if win, wallet + bet  if black jack 1.5 times bet if draw get bet back
        self.wallet += self.bet
    
    def lose_bet(self):
        self.wallet -= self.bet

def win_lose(playerhand, dealerhand):
    if playerhand.value > dealerhand.value:
        print('You Lose')
    else:
        print('You Win')

def hit(hand, deck):
    hand.add_card(deck.deal())
    hand.eval_val()
    for card in hand.cards:
        print(card)

def hit_stand(hand, deck):
    a = True
    while a:
        print('\n')
        hsMenu = pyip.inputMenu(['Hit', 'Stand'])
        if hsMenu == 'Hit':
            hit(hand,deck)
            if hand.value > 21:
                print('You Lose')
                print('Your Current Total Value:')
                print(hand.value)
                print('\n')
                a = False
                break
            else:
                print('Your Current Total Value:')
                print(hand.value)
                print('\n')
                continue
        else:
            a = False
            break

#place bet
player_bet = Bet()
print(player_bet)

#shuffle deck
test_deck = Deck()
test_deck.shuffle()

#dealer deals cards
test_dealer = Hand()
test_player = Hand()
test_dealer.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_dealer.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())

#dealer shows one card from their own hand
print('Out of Two Cards, the Dealer Has:')
for card in test_dealer.cards:
    print(card)
    break
test_dealer.eval_val()

#player evaluates own hand
print('\nYour Hand:')
for card in test_player.cards:
    print(card)
print('Your Current Total Value:')
test_player.eval_val()
print(test_player.value)

#player chooses hit or stand
hit_stand(test_player,test_deck)

#player wins or loses
print('Dealer Reveals Hand:')
for card in test_dealer.cards:
    print(card)
print(test_dealer.value)

#win_lose(test_player, test_dealer)