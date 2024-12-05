import unittest

from src.personnage import Personage

class MyTest_Case(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personage = Personage()
        self.assertEqual(10, personage.get_hp())