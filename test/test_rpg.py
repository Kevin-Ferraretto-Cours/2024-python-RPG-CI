import unittest

from src.personnage import Personage

class MyTest_Case(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personage = Personage()
        self.assertEqual(20, personage.get_hp())

    def test_attaquer_enleve_1_hp(self):
        attaquant = Personage()
        defenseur = Personage()
        attaquant.attaquer(defenseur)
        self.assertEqual(19, defenseur.get_hp())