# A class that represents a playing card

class Card:

    suits = {"heart","spade","diamond","club"}
    named = ["jack", "queen", "king","ace"]
    def __init__(self, value=None, suit=None, color=None):
        
        # If no card specified, set all value to None
        if value == None or suit == None:
            self.make_null()
            return
        
        # Check types of value and suit
        if type(value) != int or type(suit) != str:
            self.make_null()
            return

        if suit not in {"heart","spade","diamond","club"}:
            self.make_null()
            return

        if value < 2 or value > 14:
            self.make_null()
            return
        
        self.value = value
        self.suit  = suit
        self.color = "black" if suit in {"spade","club"} else "red"

    def make_null(self):
        self.value = None
        self.suit  = None
        self.color = None
    
    def __repr__(self):
        if self.value == None:
            return "Blank"
        if self.value < 11:
            return "{} of {}s".format(self.value, self.suit).title()
        name = self.named[self.value-11]
        return "{} of {}s".format(name, self.suit).title()
