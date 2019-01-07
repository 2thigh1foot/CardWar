from random import shuffle, randint
from card import Card
# A class that represents a deck of cards

class Deck:

    fullDeck = []
    for i in range(2,15):
        for suit in Card.suits:
            fullDeck.append(Card(i,suit))
              
    '''
        Constructor for a Deck
    '''
    def __init__(self):
        
        #Declare a list of Cards that make up a Deck
        self.cards = fullDeck[::]
        self.discard = []
        
        shuffle(self.cards)
            
    '''
        Draws one random card from the deck.
    '''
    def draw_card(num=1): 
        
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

    def __len__(self):
        return len(self.cards)
    '''
        Removes specified card
    '''
    def discard_card(card):
        self.discard.append(card)
