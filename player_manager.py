from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from abstract_player import AbstractPlayer
from player_stats import PlayerStats
from guard import Guard
from forward import Forward
from center import Center
import json
import os.path

#Player manager class
class PlayerManager:
    """ Array for team """
    _filepath = None

    def __init__(self, db_name):
        """ Contructs a Player object """
        if db_name is None or db_name == "":
            raise ValueError("Database Name cannot be undefined")

        engine = create_engine("sqlite:///" + db_name)
        self._db_session = sessionmaker(bind=engine, expire_on_commit=False)

    def add_player(self, player_object):
        """adds a product"""
        session = self._db_session()

        session.add(player_object)
        session.commit()

        session.close()
    
    def get_player(self, player_id):
        """ Gets specific player based on ID """
        AbstractPlayer._validate_int(AbstractPlayer.player_id, player_id)
        session = self._db_session()

        player = session.query(Guard).filter(Guard.player_type == "guard").filter(Guard.player_id == player_id).first()

        if player is None:
            player = session.query(Forward).filter(Forward.player_type == "forward").filter(Forward.player_id == player_id).first()
            if player is None:
                player = session.query(Center).filter(Center.player_type == "center").filter(Center.player_id == player_id).first()

        session.close()
        return player


    def get_all(self):
        """ Gets all players """
        session = self._db_session()
        players1 = session.query(Guard).filter(Guard.player_type == "guard").all()
        players2 = session.query(Forward).filter(Forward.player_type == "forward").all()
        players3 = session.query(Center).filter(Center.player_type == "center").all()
        players = players1 + players2 + players3

        session.close()
        return players


    def get_all_by_type(self, type):
        """Gets all players by type"""

        session = self._db_session()

        if type == "guard":
            players = session.query(Guard).filter(Guard.player_type == "guard").all()
        elif type == "forward":
            players = session.query(Forward).filter(Forward.player_type == "forward").all()
        elif type == "center":
            players = session.query(Center).filter(Center.player_type == "center").all()

        session.close()
        return players

    def delete_player(self, player_id):
        """ Deletes Player based on Player ID """
        AbstractPlayer._validate_int(AbstractPlayer.player_id, player_id)
        session = self._db_session()

        player_in_db = session.query(AbstractPlayer).filter(AbstractPlayer.player_id == player_id).first()
        session.delete(player_in_db)
        session.commit()

        session.close()

    def update_player(self, update_player):
        """ Update Player based on Player object """
        player_id = update_player.get_player_id()

        if player_id == None:
            raise ValueError("Only existing players can be updated")

        session = self._db_session()

        existing_player = session.query(AbstractPlayer).filter(AbstractPlayer.player_id == update_player.player_id).first()


        if existing_player is None:
            raise ValueError("Player does not exist")

        session.delete(existing_player)
        session.commit()
        session.add(update_player)
        session.commit()
        session.close()

    def get_player_stats(self):
        player_stats = PlayerStats(self)
        return player_stats
        


    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """
        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

   
                
        
