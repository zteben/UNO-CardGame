"""
Sung Hyun Kim, 1930074
Friday, May 7
R. Vincent, instructor
Final Project
"""


class Card:
    def __init__(self, c, v):
        self.color = c
        self.value = v

    def isPlayable(self, topcard):
        """
        Checks if the card is playable
        :param topcard: card at the top of the used pile (Card)
        :return: bool
        """
        if self.color == 'WILD' or self.color == 'WILD DRAW FOUR':
            return True
        elif self.color == topcard.color or self.value == topcard.value:
            return True
        else:
            return False

