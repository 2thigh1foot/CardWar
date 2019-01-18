from random import shuffle

# a class that represents the hadn of cards a player has


class Hand:

    '''
        Default constructor for a Hand
    '''

    def __init__(self, cards=[]):
        self.cards = cards
        self.discarded = []

    '''
        Play the cards specified
    '''

    def play_cards(self, num=1):
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

    def discard(self, card_list):
        self.discarded += card_list

    def shuffle(self):
        '''
        Shuffle the cards in hand
        '''
        shuffle(self.discarded)

    # Tells of is hand is empty
    def is_empty(self):
        return len(self.cards) == 0
    # print out hands

    def __repr__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards+self.discarded)
