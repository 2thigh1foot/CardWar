# A class that will wrap all our game data together
import random
from deck import Deck
from hand import Hand

class War:

    def __init__(self, num_players=2):

        self.num_players = num_players
        
        self.hands = [None for _ in range(num_players)]
        self.deck = Deck()

    def deal_cards(self):
        # Distributes the cards from the deck to the player
        deck.shuffle()
        cards_to_give = len(self.deck) // num_players
        
        for i in range(len(self.hands)):
            self.hands[i] = Hand(self.deck.draw_card(cards_to_give))
            
        return self.deck

    def check_winner(self):
        # Checks to see which player is winner
        winners = [len(c)==len(Deck.fullDeck) for c in self.hands]
        if sum(winners) == 0:
            return -1
        return winners.index(True)
