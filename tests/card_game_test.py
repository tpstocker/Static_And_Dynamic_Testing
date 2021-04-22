import unittest
from src.card import *
from src.card_game import *


class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.game = CardGame()
        self.card = Card("hearts", 1)
        self.card1 = Card("diamonds", 5)


    def test_check_for_ace(self):
        self.assertEqual (True, self.game.check_for_ace(self.card))

    
    def test_highest_card(self):
        self.assertEqual(self.card1, self.game.highest_card(self.card, self.card1))

    def test_cards_total(self):
        array_of_cards = []
        array_of_cards.append(self.card)
        array_of_cards.append(self.card1)
        self.assertEqual("You have a total of 6", self.game.cards_total(array_of_cards))

