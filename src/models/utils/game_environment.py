import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class OomiGame:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck = self.create_deck()
        self.hands = self.deal_cards()
        self.played_cards = []
        self.current_player = 0
        self.current_trick = []
        self.tricks_won = {'team1': 0, 'team2': 0}
        self.trump_suit = None

    def create_deck(self):
        return [Card(suit, value) for suit in self.SUITS for value in self.VALUES]

    def deal_cards(self):
        random.shuffle(self.deck)
        return [self.deck[i::4] for i in range(4)]

    def choose_trump(self, suit):
        self.trump_suit = suit

    def play_move(self, card):
        # Implementation of playing a card
        pass

    def is_game_over(self):
        return all(len(hand) == 0 for hand in self.hands)

    def get_winner(self):
        if self.tricks_won['team1'] > self.tricks_won['team2']:
            return 'team1'
        elif self.tricks_won['team2'] > self.tricks_won['team1']:
            return 'team2'
        else:
            return 'tie'