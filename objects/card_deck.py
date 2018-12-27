import random as rd


class Deck:

    def __init__(self, name, cards):
        self.name = name
        self.deck = rd.sample(cards, len(cards))

    def shuffle(self):
        self.deck = rd.sample(cards, len(cards))

