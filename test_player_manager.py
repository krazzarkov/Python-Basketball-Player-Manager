from sqlalchemy import create_engine
from base import Base

from abstract_player import AbstractPlayer
from player_stats import PlayerStats
from player_manager import PlayerManager
from guard import Guard
from forward import Forward
from center import Center
import unittest
from unittest import TestCase
import os

import inspect
import re

class TestPlayer(TestCase):
    """ Unit tests for the Player Class """

    def setUp(self):
        engine = create_engine('sqlite:///test_players.sqlite')

        # Create all the tables
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        """ Sets up data and calls logPoint """
        self.logPoint()

        self.player_manager = PlayerManager("test_players.sqlite")
        self.player1 = Forward(1, "Lebron", "James", 201, 81, 2003, "forward", 1028, 690)
        self.player2 = Center(2, "Dwight", "Howard", 210, 90, 2002, "guard", 1054, "Aggresive")
        self.player3 = Guard(3, "Rajon", "Rondo", 190, 76, 2004, "center", 909, 1203)
        self.player_manager.add_player(self.player1)
        self.player_manager.add_player(self.player2)
        self.player_manager.add_player(self.player3)
        self.assertIsNotNone(self.player_manager)
    
    def tearDown(self):
        """ Destroys data and sets up logPoint """
        os.remove("test_players.sqlite")
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor_valid_input(self):
        """ Tests the constructor with valid inputs """
        self.assertEqual(1, self.player1.get_player_id(), "Player number should be number 1")
        self.assertEqual(2, self.player2.get_player_id(), "Player number should be number 2")
        self.assertEqual(3, self.player3.get_player_id(), "Player number should be number 3")
        self.assertEqual("Los Angeles Lakers", self.player_manager.get_team_name(), "Team Name should be Los Angeles Lakers")
    
    def test_constructor_invalid_input(self):
        """ Tests the constructor with invalid inputs """
        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Forward, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots took should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots made should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)

        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Guard, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of steals made should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of assists should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)

        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Center, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of rebounds should be positive", Center, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Play-type should be a string", Center, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)
    
    def test_get_player(self):
        """ Tests the get_player method """
        player23 = self.player_manager.get_player(3)
        self.assertEqual(3, player23.get_player_id(), "Player should be number 23")

    def test_get_all(self):
        """ Tests the get_all method """
        self.assertEqual(3, len(self.player_manager.get_all()), "Team should have 3 players")
    
    def test_get_player_stats(self):
        """ Tests the get_player_stats method """
        stats = self.player_manager.get_players_stats()

        self.assertEqual(3, stats.get_total_num_players(), "Team should have 3 players")
        self.assertEqual(1, stats.get_num_guards(), "Team should have 1 guard")
        self.assertEqual(1, stats.get_num_forwards(), "Team should have 1 forward")
        self.assertEqual(1, stats.get_num_centers(), "Team should have 1 center")
        
    def test_add_player_valid_input(self):
        """ Tests the add_player method with valid inputs """
        self.assertEqual(3, self.player_manager.get_players_stats().get_total_num_players(), "Team should have 3 players")
        player4 = Guard(7, "June", "Ka", 190, 76, 2004, 909, 1203)
        self.player_manager.add_player(player4)
        self.assertEqual(4, self.player_manager.get_players_stats().get_total_num_players(), "Team should have 4 players")
    
    def test_add_player_invalid_input(self):
        """ Tests the add_player method with invalid inputs """
        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Forward, "STRING", "Lebron", "James", 201, 81, 2003, "forward", 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots took should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, "forward", -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots made should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, "forward", 1028, -690)

        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Guard, "STRING", "Lebron", "James", 201, 81, 2003, "forward", 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of steals made should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, "forward", -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of assists should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, "forward", 1028, -690)

        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Center, "STRING", "Lebron", "James", 201, 81, 2003, "forward", 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of rebounds should be positive", Center, 12, "Lebron", "James", 201, 81, 2003, "forward", -1028, 690)
        self.assertRaisesRegex(ValueError, "Play-type should be a string", Center, 12, "Lebron", "James", 201, 81, 2003, "forward", 1028, -690)
        
    def test_delete_player_valid_input(self):
        """ Tests the delete_player with valid inputs """
        self.assertEqual(3, self.player_manager.get_player_stats().get_total_num_players(), "Team should have 3 players")
        player4 = Guard(4, "June", "Ka", 190, 76, 2004, 909, 1203)
        self.player_manager.add_player(player4)
        self.assertEqual(4, self.player_manager.get_player_stats().get_total_num_players(), "Team should have 4 players")
        self.player_manager.delete_player(4)
        self.assertEqual(3, self.player_manager.get_player_stats().get_total_num_players(), "Team should have 3 players")

    def test_delete_player_invalid_input(self):
        """ Tests the delete_player with invalid inputs """
        self.assertEqual("Player ID should be an integer value", self.player_manager.delete_player("STRING"), "Input should be an integer value")
        
    def test_get_team_name(self):
        """ Tests the get_team_name method """
        self.assertEqual("Los Angeles Lakers", self.player_manager.get_team_name(), "Team name should be Los Angeles Lakers")

    def test_update_valid_input(self):
        """ Tests the update method with valid inputs """
        string = "3: Rajon Rondo is 190.00 cm tall, weighs 76.00 kg, drafted on 2004, has 909 steals and 1203 assists"
        self.assertEqual(string, self.player3.get_description(), "These two strings should be equal")
        
        self.player3 = Guard(3, "June", "Ka", 180, 81, 2019, 0, 0)
        self.player_manager.update_player(self.player3)
        string2 = "3: June Ka is 180.00 cm tall, weighs 81.00 kg, drafted on 2019, has 0 steals and 0 assists"
        self.assertEqual(string2, self.player3.get_description(), "These two strings should be equal")
    
    def test_get_all_by_type(self):
        """ Tests get_all_by_type method """
        string = self.player_manager.get_all_by_type()
        self.assertEqual(string, self.player_manager.get_all_by_type(), "These two strings should be equal")

    def test_update_invalid_input(self):
        """ Tests update method with invalid inputs """
        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Forward, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots took should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of shots made should be positive", Forward, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)

        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Guard, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of steals made should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Number of assists should be positive", Guard, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)

        self.assertRaisesRegex(ValueError, "Player number should be an integer value", Center, "STRING", "Lebron", "James", 201, 81, 2003, 1028, 690)
        self.assertRaisesRegex(ValueError, "Number of rebounds should be positive", Center, 12, "Lebron", "James", 201, 81, 2003, -1028, 690)
        self.assertRaisesRegex(ValueError, "Play-type should be a string", Center, 12, "Lebron", "James", 201, 81, 2003, 1028, -690)

        

if __name__ == "__main__":
    unittest.main()
