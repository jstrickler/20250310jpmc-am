
class PlayingCard: # inherits from object
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):  # getter property
        return self._rank


    @property
    def suit(self):  # getter property
        return self._suit
    
    @suit.setter  # setter
    def suit(self, value):
        if value not in ('Clubs Diamonds Hearts Spades'.split()):
            raise ValueError("invalid suit")
        else:
            self._suit = value

    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = PlayingCard('8', 'Diamonds')
    c2 = PlayingCard('Q', 'Spades')
    print(f"{c1 = }")  # repr()
    print(c1.rank)
    print(c1.suit)
    print(c1)  # str()
    print(c2)
    print(repr(c1))
#    c1.suit = "Wombats"