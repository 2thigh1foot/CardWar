# A class that will wrap all our game data together
import random


class War:

    def __init__(self, deck, num_players=2):

        self.num_players = num_players
        # Creates empty lists of hands
        self.hands = [[] for i in range(self.num_players)]
        self.deck = deck

    def deal_cards(self, deck):
        # Distributes the cards from the deck to the player
        i = 0
        while (len(deck) != 0 and deck != None):
            player = i % self.num_players
            card = random.choice(deck)
            self.hands[player].append(card)
            i += 1
            deck.remove(card)
            # self.deck.remaining().remove(card)
            # self.deck.removed().add(card)

        return self.hands

    def check_winner(self, hands):
        # Checks to see which player is the winner on the first index of the hands played.
        winning_card = hands[0].pop(0)
        visible_cards = [winning_card]
        winning_index = 0
        for i in range(1, self.num_players):
            checked_card = hands[i].pop(0)
            if checked_card > winning_card:
                winning_card = checked_card
                winning_index = i  # keep check of which player was the winner
            visible_cards.append(checked_card)

        # grant the winner their won cards
        hands[winning_index] += visible_cards

        return hands
