from random import shuffle, randint
from card import Card
# A class that represents a deck of cards

class Deck:

    '''
        Constructor for a Deck
    '''
    fullDeck = []
    for i in range(2,15):
        for suit in Card.suits:
            fullDeck.append(Card(i,suit))
              
    def __init__(self, cards=None, lostCards=None):
        
        #Declare a list of Cards that make up a Deck
        self.cards = fullDeck[::]
		self.discard = []
        
      	shuffle(self.cards)
            
    '''
        Draws one random card from the deck.
    '''
    def draw_card(num=1): 
      	# draw_cards() -> draw_cards(1)
        # draw_cards(5) 
      	removedCards = []
        for i in range(num):
          	card = self.cards.pop(0)
        	removedCards.append(card)
            
		return removedCards

    def discarded():
    	return self.discard
    '''
        Shuffles the deck using random object shuffle.
    '''
    def shuffle():
        shuffle(self.cards)
    
    '''
        Returns the cards in the deck.
    '''
    def remaining():
        return self.cards

    '''
        Resets the deck to a full one
    '''
    def reset():
        self.lostCards = []
        self.cards = fullDeck[::]
        shuffle(self.cards)

    '''
        Draws a random card from the deck
    '''
    def draw_random(num=1):
        #Selects random card
        removedCards = []
        for i in range(num):
        	card = self.cards.pop(randint(0,len(self.cards)-1))
        	removedCard.append(card)
            self.lostCards(card)

        return removedCards

    '''
        Removes specified card
    '''
    def discard(card):
        self.discard.append(card)
