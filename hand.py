from random import shuffle

#a class that represents the hadn of cards a player has

class Hand:

    '''
        Default constructor for a Hand
    '''
    def __init__(self, cards=[]):
        self.cards = cards
        self.discarded = []

    def __len__(self):
        return len(self.cards+self.discarded)
        
    '''
        Play the cards specified
    '''
    def play_cards(num=1):
      	cardsPlayed = []
        
        if(len(self.cards) < num):
          	if(len(self.cards)+len(self.discarded) < num):
              	return []
            self.shuffle()
            self.cards += self.discarded
            self.discarded = []
            
        for i in range(num):
            takenCard = self.cards.pop(0)
            cardsPlayed.append(takenCard)
        return cardsPlayed
        
    '''
    '''
    def discard(card_list):
        self.discard += card_list
    '''
        Shuffle the cards in hand
    '''
    def shuffle():
        shuffle(self.discard)

