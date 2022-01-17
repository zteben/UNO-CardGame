"""
Sung Hyun Kim, 1930074
Friday, May 7
R. Vincent, instructor
Final Project
"""
from Players import Player
from Decks import Deck
from random import choice, sample

# Starting deck of UNO cards
deck = Deck()
deck.new_build()
deck.shuffle_cards()

# Number of players for the game of UNO
while True:
    n_players = input('Enter the number of players (2-10):  ')
    try:
        n_players = int(n_players)
        if 10 >= n_players >= 2:
            break
        print('Please enter an appropriate number!')
    except ValueError:
        print('Please enter an appropriate number!')

players = []
for n in range(n_players):
    players.append(Player(n))

# Distribute cards to each player
for p in players:
    p.draw_card(deck, 7)

# First top card
pile = []
while True:
    topcard = deck.pop()
    if topcard.value in ("WILD", "WILD DRAW FOUR"):
        deck.insert(0, topcard)
    else:
        pile.append(topcard)
        break

PLAYING = True
turn = 0
while PLAYING:

    if len(deck) < 20:  # Restock the deck
        reuse = sample(pile[1:], len(pile[1:]))
        for c in reuse:
            deck.insert(0, c)

    hand = players[turn]
    print("top card:", topcard.color, topcard.value)
    if hand.position == 0:
        print("\nYOUR TURN")
        n = 1
        for c in hand:      # Show all the cards in the player's hand
            if c.value in ("WILD", "WILD DRAW FOUR"):
                print("{}-".format(n), c.value)
            else:
                print("{}-".format(n), c.color, c.value)
            n += 1
        print("{}- Draw a card".format(n))
    else:
        print("\nPLAYER {}'S TURN".format(hand.position + 1))  # Indicates which player's turn it is

    while True:
        try:
            # Card selection
            if hand.position == 0:
                option = input("Enter the number of the card you want to play:  ")
            else:
                options = []
                for c in hand:
                    if c.isPlayable(topcard):
                        options.append(hand.index(c)+1)
                if not options:
                    option = len(hand) + 1
                else: 
                    option = choice(options)

            if 0 < int(option) <= len(hand):
                choose = hand[int(option) - 1]
                if choose.isPlayable(topcard):  # Play a playable card
                    players[turn].play_card(choose, pile)
                    
                    if len(players[turn]) == 0:  # Game is over if there are no cards left in the player's hand
                        PLAYING = False

                    # Special card effects
                    if choose.value == "REVERSE":  # Order of play switches direction
                        players.reverse()
                        turn = players.index(hand)
                    elif choose.value == "SKIP":  # Next player's turn is skipped
                        turn += 1
                        if turn >= len(players):
                            turn = 0
                    elif choose.value == "DRAW TWO":  # Next player draws two cards and misses a turn
                        turn += 1
                        if turn >= len(players):
                            turn = 0
                        players[turn].draw_card(deck, 2)
                    elif choose.value == "WILD":    # Player declares a color of choice
                        if players[turn].position == 0:
                            while True:
                                select = input("\n 1- Red \n 2- Yellow \n 3- Green \n 4- Blue \n")
                                try:
                                    select = int(select)
                                    if select == 1:
                                        choose.color = "Red"
                                        break
                                    elif select == 2:
                                        choose.color = "Yellow"
                                        break
                                    elif select == 3:
                                        choose.color = "Green"
                                        break
                                    elif select == 4:
                                        choose.color = "Blue"
                                        break
                                    else:
                                        print("Please enter an appropriate number!")
                                except ValueError:
                                    print("Please enter an appropriate number!")
                        else:
                            colors = ["Red", "Yellow", "Green", "Blue"]
                            choose.color = choice(colors)
                            
                    elif choose.value == "WILD DRAW FOUR":
                        if players[turn].position == 0:     # Player declares a color of choice
                            while True:
                                select = input("\n 1- Red \n 2- Yellow \n 3- Green \n 4- Blue \n")
                                try:
                                    select = int(select)
                                    if select == 1:
                                        choose.color = "Red"
                                        break
                                    elif select == 2:
                                        choose.color = "Yellow"
                                        break
                                    elif select == 3:
                                        choose.color = "Green"
                                        break
                                    elif select == 4:
                                        choose.color = "Blue"
                                        break
                                    else:
                                        print("Please enter an appropriate number!")
                                except ValueError:
                                    print("Please enter an appropriate number!")
                        else:
                            colors = ["Red", "Yellow", "Green", "Blue"]
                            choose.color = choice(colors)

                        # Next player draws four cards and misses a turn
                        turn += 1
                        if turn >= len(players):
                            turn = 0
                        players[turn].draw_card(deck, 4)

                    break   # Turn is over

                else:  # Card cannot be played
                    print("This card cannot be played!")

            elif int(option) == len(hand)+1:    # Draw a card
                players[turn].draw_card(deck, 1)
                break
            else:
                print("Please enter an appropriate number!")
        except ValueError:
            print("Please enter an appropriate number!")

    topcard = pile[0]   # Update top card

    if PLAYING:
        turn += 1   # Update turn for next player
        if turn >= len(players):
            turn = 0

# Announce winner of the game
if players[turn].position == 0:
    print("\nYOU ARE THE WINNER!!!")
else:
    print("\nPLAYER {} IS THE WINNER!!!".format(1 + players[turn].position))
