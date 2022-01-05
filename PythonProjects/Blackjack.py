##Import module and set up cards
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

##Classes
class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck consists of:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    
    def __init__(self):
        self.total = 0
        self.bet = 0

    def chip_deposit(self):
        q = input("Do you want to exchange money for chips? Enter 'y' or 'n' ")

        while q[0].lower() == 'y':
            try:
                self.total += int(input('How much money do you want to exchange for chips? '))
            except:
                print('Sorry, your input needs to be a number. Please try again!')
                continue
            else:
                break

        print(f'\nYou currently have {self.total} chips.')
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

##Functions
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

#Functions for player actions
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        action = input("Do you want to HIT or STAND? Enter 'h' or 's': ")

        if action[0].lower() == 'h':
            hit(deck,hand)
        elif action[0].lower() == 's':
            print('\nPlayer stands. Dealer is playing')
            playing = False
        else:
            print("Input incorrect. Please choose 'h' or 's'")
        break

#Functions for showing cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#Functions for end of game scenarios
def player_busts(player,dealer,chips):
    print('\nPlayer busts! Dealer wins!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('\nPlayer wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('\nDealer busts! Player wins!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('\nDealer wins!')
    chips.lose_bet()
    
def push(player,dealer):
    print("\nPlayer and Dealer tie! It's a push")

##Game logic
playing = True

while True:
    #Opening statement
    print('Welcome to BlackJack!\n Get as close to 21 as you can without going over!\n Dealer hits until total value of 17 has been reached.\n Aces count as 1 or 11.')
    
    #Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    #Set up the Player's chips
    player_chips = Chips()
    player_chips.chip_deposit()
    
    #Prompt the Player for their bet
    take_bet(player_chips)
    
    #Show cards
    show_some(player_hand, dealer_hand)
    
    while playing:
        #Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        
        #If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    #If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
    
        #Show cards
        show_all(player_hand, dealer_hand)
    
        #Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)
    
    #Inform Player of their chips total
    print(f'\nPlayer has a total of {player_chips.total} chips.')
    
    #Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")

    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('\nThank you for playing! Enjoy your winnings!')
        break