from abstract_player import AbstractPlayer
from player_manager import PlayerManager
from guard import Guard
import unittest
from unittest import TestCase
import inspect
import re

class TestForward(TestCase):
    """ Unit tests for the Center class """

    def setUp(self):
        """ Sets up data and calls logPoint """
        self.logPoint()
        self.player_manager = PlayerManager("Los Angeles Lakers", "file.txt")
        self.player1 = Guard(1, "Rajon", "Rondo", 190, 76, 2004, "guard", 909, 1203)
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
        """ Tests for constructor with valid input """
        self.assertEqual(1, self.player1.get_player_id(), "Player number should be number 1")
        self.assertEqual("Los Angeles Lakers", self.player_manager.get_team_name(), "Team Name should be Los Angeles Lakers")
    
    def test_constructor_invalid_input(self):
        """ Tests for constructor with invalid input """
        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Guard, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of steals made should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of assists should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)

    def test_get_description(self):
        """ Tests the get_description method """
        string = "1: Rajon Rondo is 190.00 cm tall, weighs 76.00 kg, drafted on 2004, has 909 steals and 1203 assists"
        self.assertEqual(string, self.player1.get_description(), "These two strings should be equal")

    def test_get_num_steals(self):
        """ Tests the get_num_steals method """
        self.assertEqual(909, self.player1.get_num_steals(), "These two values should be equal")

    def test_get_num_assists(self):
        """ Tests the get_num_assists method """
        self.assertEqual(1203, self.player1.get_num_assists(), "These two values should be equal")

    def test_get_type(self):
        """ Tests the get_type method """
        self.assertEqual("GUARD", self.player1.get_type(), "These two strings should be equal")

if __name__ == "__main__":
    unittest.main()