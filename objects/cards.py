# A module to define a game card and all of its subtypes


class Card:
    """A generic card used in gameplay"""

    def __init__(self, deck):
        self.add_to_deck(deck)
        self.deck = deck

    def add_to_deck(self, deck):
        # add_card to deck
        pass

    def draw_card(self, player):
        # a player draws a card
        pass

    def flip(self):
        # flip a card over to reveal face
        pass

    def play(self):
        # play the card
        pass

    def display(self):
        # draw the card on the game board with whichever face should be up
        pass