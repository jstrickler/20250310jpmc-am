from playingcard import PlayingCard
from carddeck import CardDeck

class CardGame:
    def start_game(self):
        print("starting game")

class JokerDeck(CardGame, CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            card = PlayingCard(f"JOKER {joker_number}", "**JOKER**")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    for i in range(5):
        print(j.draw())
    j.start_game()
    print(f"{JokerDeck.mro() = }")
    