from base import Base
from sqlalchemy import *

class AbstractPlayer(Base):
    CENTER_TYPE = "CENTER"
    GUARD_TYPE = "GUARD"
    FORWARD_TYPE = "FORWARD"

    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    height = Column(Integer)
    weight = Column(Integer)
    year_drafted = Column(Integer)
    player_type = Column(String(100))

    """ Representation of a Player on a basketball team """
    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, player_type):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.year_drafted = year_drafted
        self.player_type = player_type

    def get_description(self):
        """ Returns player details """
        details = "Number %d: %s %s is %.2f cm tall and weighs %.2f kg, was drafted on %s, and has a role of %s" % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._player_type)
        return details

    def set_player_id(self, player_id):
        """ Sets a player_id for a AbstractPlayer """
        self.player_id = player_id

    def get_player_id(self):
        """ Returns player_id """
        return self.player_id
    
    def get_player_first_name(self):
        """ Returns player's first name """
        return self.first_name

    def get_player_last_name(self):
        """ Returns player's last name """
        return self.last_name

    def get_player_height(self):
        """ Returns player's height """
        return self.height

    def get_player_weight(self):
        """ Returns player's weight """
        return self.weight
    
    def get_player_year_drafted(self):
        """ Returns player's year drafted """
        return self.year_drafted

    def get_player_type(self):
        """ Returns player's role """
        return self.player_type

    def to_dict(self):
        """ Abstract method to return the dictionary of the vehicle """
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def _validate_string(label, value):
        """ Validates an integer value """
        if value is None:
            raise ValueError("%s cannot be undefined." % label)

        if type(value) != str:
            raise ValueError("%s must be a valid String." % label)

        if value == "":
            raise ValueError("%s cannot be empty." % label)

    @staticmethod
    def _validate_int(label, value):
        """ Validates an integer value """
        if value is None:
            raise ValueError("%s cannot be undefined." % label)

        if type(value) != int:
            raise ValueError("%s must be a valid Integer." % label)

        if not value > 0:
            raise ValueError("%s must be a positive Integer." % label)

    @staticmethod
    def _validate_float(label, value):
        """ Validates an integer value """
        if value is None:
            raise ValueError("%s cannot be undefined." % label)

        if type(value) != float:
            raise ValueError("%s must be a valid Floating Point Number." % label)

        if not value > 0.0:
            raise ValueError("%s must be a positive Floating Point Number." % label)
