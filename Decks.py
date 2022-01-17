"""
Sung Hyun Kim, 1930074
Friday, May 7
R. Vincent, instructor
Final Project
"""

# rules
'''
2 - 10 players
7 cards for each player at start

Turn choice:
    Play card (number or color)
    Play Wild or Wild Draw Four
    Draw a card
'''
from random import shuffle
from Cards import Card


class Deck(list):
    def new_build(self):
        """
        Creates a deck of UNO cards (list)

        Number of cards = 108
        Four colors: red, yellow, green, blue
            For each color, there are two sets of cards with the values 1 to 9, REVERSE, SKIP, and DRAW TWO
            For each color, there is only one card with the value 0
        There are 4 WILD cards and 4 WILD DRAW FOUR cards
        """
        colors = ['Red', 'Yellow', 'Green', 'Blue']
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'REVERSE', 'SKIP', 'DRAW TWO']
        wilds = ['WILD', 'WILD DRAW FOUR']

        for c in colors:
            self.append(Card(c, 0))
            for v in values[1:]:
                self.append(Card(c, v))
                self.append(Card(c, v))
            self.append(Card(wilds[0], wilds[0]))
            self.append(Card(wilds[1], wilds[1]))

    def shuffle_cards(self):
        """Randomly shuffles the deck of cards"""
        shuffle(self)
