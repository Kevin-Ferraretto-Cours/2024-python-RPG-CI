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

    def test_personnage_meurt_a_0_hp(self):
        attaquant = Personage()
        defenseur = Personage()
        for _ in range(20):
            attaquant.attaquer(defenseur)
        self.assertEqual(0, defenseur.get_hp())
        self.assertFalse(defenseur.est_vivant())