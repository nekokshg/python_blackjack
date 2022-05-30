import random
import pyinputplus as pyip

suits = ['Hearts', 'Clubs', 'Diamonds', 'Clovers']
values = ['Ace' ,'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
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
        self.Playvalue = 0
        self.Dealvalue = 0
        self.aceval = 0

    def add_card(self,card):
        self.cards.append(card)

    def ace_choice(self):
        while True:
            print('Choose 1 or 11')
            choice = input('> ')
            if choice == '1':
                self.Playvalue += 1
                self.aceval +=1
                break
            elif choice == '11':
                self.Playvalue +=11
                self.aceval += 11
                break
            else:
                print('Invalid Input')
                continue

    def Playeval_val(self):
        for card in self.cards:
            if card.value == 'Ace':
                self.ace_choice()
            else:
                self.Playvalue += card.card_value

#EDIT not DRY code & if over 6 cards the code breaks
#probability of four aces in a row is low but coded it just in case
    def hitPlayeval_val(self):
        hit_hand = self.cards
        lenhit_hand = len(hit_hand)
        for card in hit_hand:
            if lenhit_hand == 3:
                if card == hit_hand[2]:
                    if card.value == 'Ace':
                        self.ace_choice()    
                    else:
                        if card.value != 'Ace':
                            self.Playvalue += card.card_value
            elif lenhit_hand == 4:
                if card == hit_hand[3]:
                    if card.value == 'Ace':
                        self.ace_choice()
                    elif card.value != 'Ace':
                        self.Playvalue += card.card_value
            elif lenhit_hand == 5:
                if card == hit_hand[4]:
                    if card.value == 'Ace':
                        self.ace_choice()
                    elif card.value != 'Ace':
                        self.Playvalue += card.card_value
            elif lenhit_hand == 6:
                if card == hit_hand[5]:
                    if card.value == 'Ace':
                        self.ace_choice()
                    elif card.value != 'Ace':
                        self.Playvalue += card.card_value

#EDIT
#if first card is 10 dealer should choose ace 11
#fixed code not sure if it works
    def Dealeval_val(self):
        dealer_hand = self.cards
        for card in dealer_hand:
            if card == dealer_hand[0]:
                if card.value == 'Ace':
                    self.Dealvalue += 11
                    self.aceval += 11
                else:
                    self.Dealvalue += card.card_value
            elif card == dealer_hand[1]:
                if dealer_hand[0] == 10:
                    if card.value == 'Ace':
                        self.Dealvalue += 11
                        self.aceval += 11
                else:
                    if card.value == 'Ace':
                        self.Dealvalue += 1
                        self.aceval += 1
                    else:
                        self.Dealvalue += card.card_value

class Bet:
    global b
    b = True

    def __init__(self):
        self.wallet = 100
        self.bet = 0

    def bettype(self):
        print(f'Minimum Bet: $5 & Maximum Bet: {self.wallet}')
        print('Amount to Bet:')
        while True:
            amt = pyip.inputNum(min=5, max=2000)
            if amt > self.wallet:
                print('Invalid Bet')
                continue
            else:
                self.bet += amt
                break

    def draw(self):
        self.bet = 0

    def win_bet(self):
        #edit if win, wallet + bet  if black jack 1.5 times bet if draw get bet back
        self.wallet += self.bet
        print('\nYou Win')
        print(f'Remaining Amount in Wallet: {self.wallet}')
        print('Would you like to play again?')
        plyagainMenu = pyip.inputMenu(['Y', 'N'])
        if plyagainMenu == 'Y':
            b = True
        else:
            print('\nWinnings:')
            print(self.wallet)
            b = False
            quit()

    def lose_bet(self):
        self.wallet -= self.wallet
        print('\nYou Lose')
        if self.wallet <= 0:
            print('You have no more money')
            b = False
            quit()
        else:
            print(f'Remaining Amount in Wallet: {self.wallet}')
            print('Would you like to play again?')
            plyagainMenu = pyip.inputMenu(['Y', 'N'])
            if plyagainMenu == 'Y':
                b = True
            else:
                print('\nWinnings:')
                print(self.wallet)
                b = False
                quit()

def win_lose(playerhand, dealerhand, bet):
    #player hand exceeds 21
    if playerhand.Playvalue > 21:
        bet.lose_bet()
    #dealer hand exceeds 21
    elif dealerhand.Dealvalue> 21:
        bet.win_bet()
    #player hand less than dealer hand
    elif playerhand.Playvalue < dealerhand.Dealvalue:
        bet.lose_bet()
    #player hand greater than dealer hand
    elif playerhand.Playvalue > dealerhand.Dealvalue:
        if playerhand.Playvalue <= 21:
            bet.win_bet()
    #player hand equals dealer hand
    else:
        print('\nDraw')
        bet.draw()

def showCard(hand):
    for card in hand.cards:
        print(card)

def hit(hand, deck):
    hand.add_card(deck.deal())
    showCard(hand)
    hand.hitPlayeval_val()

def hit_stand(hand, deck):
    a = True
    while a:
        hsMenu = pyip.inputMenu(['Hit', 'Stand'])
        if hsMenu == 'Hit':
            hit(hand,deck)
            if hand.Playvalue > 21:
                print('Your Current Total Value:')
                print(hand.Playvalue)
                a = False
                break
            else:
                print('Your Current Total Value:')
                print(hand.Playvalue)
                continue
        else:
            a = False
            break

player_bet = Bet()
while b:
    #place bet
    print(f'\nAmount in Wallet: {player_bet.wallet}')
    player_bet.bettype()

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
    print('\nOut of Two Cards, the Dealer Has:')
    test_dealer.Dealeval_val()
    for card in test_dealer.cards:
        print(card)
        break

    #player evaluates own hand
    print('\nYour Hand:')
    showCard(test_player)
    test_player.Playeval_val()
    print('Your Current Total Value:')
    print(test_player.Playvalue)

    #player chooses hit or stand
    hit_stand(test_player,test_deck)

    #dealer evaluates hand
    #dealer must take a card if he hits 16 or below
    #deal card limit is 4 beyond that code breaks
    print('\nDealer Reveals Hand:')
    showCard(test_dealer)
    while True:
        if test_dealer.Dealvalue < 16:
            print('\nDealer Draws a Card...')
            test_dealer.add_card(test_deck.deal())
            showCard(test_dealer)
            for card in test_dealer.cards:
                try: 
                    if card == test_dealer.cards[3]:
                        if card.value == 'Ace':
                            test_dealer.Dealvalue += 1
                        else:
                            test_dealer.Dealvalue += card.card_value
                except:
                    if card == test_dealer.cards[2]:
                        if card.value == 'Ace':
                            test_dealer.Dealvalue += 1
                        else:
                            test_dealer.Dealvalue += card.card_value
        else:
            print('Dealer\'s Total Value:')
            print(test_dealer.Dealvalue)
            break
    
    #player wins or loses
    win_lose(test_player, test_dealer, player_bet)
