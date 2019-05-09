import unittest
from deck_of_cards import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        """Creating card"""
        self.card = Card('Hearts', 'A')

    def testCardCreation(self):
        """Checking card creation"""
        self.assertEqual(self.card.suit, 'Hearts', 'card should be A of Hearts')
        self.assertEqual(self.card.value, 'A', 'card should be A of Hearts')

    def testCardRepr(self):
        self.assertEqual(repr(self.card), 'A of Hearts', 'card should be A of Hearts')


class DeckTests(unittest.TestCase):
    def setUp(self):
        """Creating deck of cards"""
        self.deck = Deck()


if __name__ == '__main__':
    unittest.main()
