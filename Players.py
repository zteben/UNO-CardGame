"""
Sung Hyun Kim, 1930074
Friday, May 7
R. Vincent, instructor
Final Project
"""


class Player(list):
    def __init__(self, p):
        super().__init__()
        self.position = p

    def draw_card(self, deck, n):
        """
        Player draws a certain number of cards from the deck
        :param deck: Deck
        :param n: Number of cards to draw (int)
        """
        count = n
        while count > 0:
            new_card = deck.pop()
            self.append(new_card)
            count -= 1

    def play_card(self, card, pile):
        """
        Play a card from the player's hand
        :param card: Card
        :param pile: Discarded pile of cards(list)
        """
        self.remove(card)
        pile.insert(0, card)
