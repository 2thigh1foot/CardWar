import random
from random import shuffle

# A class that represents a deck of cards

#TO-DO: add "Once the deck runs out, this class should shuffle the discard deck and make it the deck." functionality

class Deck:

    '''
        Default constructor for a Deck
    '''
    def __init__(card):
        
        #Declare a list of Cards that make up a Deck
        self.cards = []
        self.lostCards = []

        #Add all of the numbered cards to the deck (36/52)
        for (int i=1; i<11; i+=1):
            for(suit : card.suits):
                cards.append(Card(i, suit))

        #Add all of the named cards to the deck (16/52)
        for(name : card.named):
            for(suit : card.suits):
                cards.append(Card(i, suit))
            
    '''
        Draws one random card from the deck.
    '''
    def draw_card(num=1): 
        self.cards.pop(0)

        #Check if deck now empty
        if (len(self.cards)== 0):
            self.cards = self.lostCards
            self.cards.shuffle()

    '''
        Shuffles the deck using random object shuffle.
    '''
    def shuffle():
        random.shuffle(self.cards)
    
    '''
        Returns the cards in the deck.
    '''
    def remaining():
        return self.cards

    '''
        Returns a list of cards removed from the deck
    '''
    def removed():
        return lostCards

    '''
        Resets the deck to a full one
    '''
    def reset():
        resetDeck = remaining().append(removed())
        self.cards = resetDeck

    '''
        Draws a random card from the deck
    '''
    def draw_random(num=1):
        #Selects random card
        cardToPull =self.cards[random.randint(1,52)-1]

        #Removes the card
        lostCards.append(cardToPull)
        self.cards.remove(cardToPull)

        #Check if deck now empty
        if (len(self.cards)== 0):
            self.cards = self.lostCards
            self.cards.shuffle()

        return cardToPull

    '''
        Removes specified card
    '''
    def discard(card, to_disard=True):
        self.cards.remove(card)





        
        