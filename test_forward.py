from abstract_player import AbstractPlayer
from player_manager import PlayerManager
from forward import Forward
import unittest
from unittest import TestCase
import inspect
import re

class TestCenter(TestCase):
    """ Unit tests for the Center class """

    def setUp(self):
        """ Sets up data and calls logPoint """
        self.logPoint()
        self.player_manager = PlayerManager("Los Angeles Lakers", "file.txt")
        self.player1 = Forward(1, "Lebron", "James", 201, 81, 2003, "forward", 1028, 690)
        self.player_manager.add_player(self.player1)
        self.assertIsNotNone(self.player_manager)
    
    def tearDown(self):
        """ Destroys data and sets up logPoint """
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor_valid_input(self):
        """ Tests the constructor with valid inputs """
        self.assertEqual(1, self.player1.get_player_id(), "Player number should be number 1")
        self.assertEqual("Los Angeles Lakers", self.player_manager.get_team_name(), "Team Name should be Los Angeles Lakers")
    
    def test_constructor_invalid_input(self):
        """ Tests the constructor with invalid inputs """
        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Forward, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots took should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots made should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)

    def test_get_description(self):
        """ Tests the get_description method """
        string = "1: Lebron James is 201.00 cm tall, weighs 81.00 kg, drafted on 2003, took 1028 shots and made 690"
        self.assertEqual(string, self.player1.get_description(), "These two strings should be equal")

    def test_get_num_shots_took(self):
        """ Tests the get_num_shots_took method """
        self.assertEqual(1028, self.player1.get_num_shots_took(), "These two values should be equal")

    def test_get_num_shots_made(self):
        """ Tests thge get_num_shots_made method """
        self.assertEqual(690, self.player1.get_num_shots_made(), "These two values should be equal")

    def test_get_type(self):
        """ Tests the get_type method """
        self.assertEqual("FORWARD", self.player1.get_type(), "These two strings should be equal")

if __name__ == "__main__":
    unittest.main()