import random
from abc import ABCMeta, abstractmethod
from playingcard import PlayingCard

class DeckBase(metaclass=ABCMeta):

    @abstractmethod
    def flip(self):
        pass

    def spam(self):
        pass
class CardDeck(DeckBase):
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    def __init__(self):
        self._make_deck()

    # def flip(self):
    #     print("flipping")

    def _make_deck(self):
        self._cards = []  # list of 52 cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
    
    @classmethod
    def get_suits(cls):
        return cls.SUITS

if __name__ == "__main__":
    c1 = CardDeck()
    print(f"{c1 = }")
    c1.shuffle()
    print(c1.cards)
    for i in range(5):
        print(c1.draw())
    print(c1.get_suits())
    print(CardDeck.get_suits())
    c2  = CardDeck()
    print(c2.get_suits())
