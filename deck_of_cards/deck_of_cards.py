from random import shuffle


class Card:
    _VALUES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    _SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

    def __init__(self, suit: str, value: str) -> object:
        if suit not in Card._SUITS:
            raise ValueError(f'Suit "{suit}" not in available suits')
        if value not in Card._VALUES:
            raise ValueError(f'Value "{value}" not in available values')
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self) -> None:
        self.cards = [Card(s, v) for s in Card._SUITS for v in Card._VALUES]
        self.iter_i = 1

    def __repr__(self) -> str:
        return f'Deck of {self.count()} cards'

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, num: int) -> list:
        if self.count() == 0:
            raise ValueError('All cards have been dealt')
        deal = []
        for i in range(0, min(num, self.count())):
            deal.append(self.cards.pop(0))
        return deal

    def count(self) -> int:
        return len(self.cards)

    def shuffle(self) -> object:
        if len(self.cards) < 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)
        return self

    def deal_card(self) -> object:
        return self._deal(1)[0]

    def deal_hand(self, num: int) -> list:
        return self._deal(num)


if __name__ == '__main__':
    deck = Deck()
    print(deck)
    print(deck.count())
    deck.shuffle()
    print(deck.deal_card())
    print(deck.deal_hand(5))
    print(deck)
    print(deck.deal_hand(5))

    for card in deck:
        print(card)