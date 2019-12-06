from abstract_player import AbstractPlayer
from player_manager import PlayerManager
from center import Center
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
        self.player2 = Center(1, "Dwight", "Howard", 210, 90, 2002, "center", 1054, "Aggresive")
        self.player_manager.add_player(self.player2)
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
        self.assertEqual(1, self.player2.get_player_id(), "Player number should be number 1")
        self.assertEqual("Los Angeles Lakers", self.player_manager.get_team_name(), "Team Name should be Los Angeles Lakers")
    
    def test_constructor_invalid_input(self):
        """ Tests the constructor with invalid inputs """
        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Center, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of rebounds should be positive", Center, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Play-type should be a string", Center, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)
    
    def test_get_description(self):
        """ Tests the get_description method """
        string =  "1: Dwight Howard is 210.00 cm tall, weighs 90.00 kg, drafted on 2002, has 1054 rebounds and plays Aggresive"
        self.assertEqual(string, self.player2.get_description(), "These two strings should be equal")
    
    def test_get_num_rebounds(self):
        """ Tests the get_num_rebounds method """
        self.assertEqual(1054, self.player2.get_num_rebounds(), "These two values should be equal")
    
    def test_get_play_type(self):
        """ Tests the get_play_type method """
        self.assertEqual("Aggresive", self.player2.get_play_type(), "These two strings should be equal")

    def test_get_type(self):
        """ Tests the get_type method """
        self.assertEqual("CENTER", self.player2.get_type(), "These two strings should be equal")

        
if __name__ == "__main__":
    unittest.main()
    