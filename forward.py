from abstract_player import AbstractPlayer
from sqlalchemy import *

class Forward(AbstractPlayer):

    num_shots_took = Column(Integer)
    num_shots_made = Column(Integer)

    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, player_type, num_shots_took, num_shots_made):
        super().__init__(player_id, first_name, last_name, height, weight, year_drafted,player_type)
        AbstractPlayer._validate_int("Number Shots Took", num_shots_took)
        AbstractPlayer._validate_int("Number Shots Made", num_shots_made)
        self.num_shots_took = num_shots_took
        self.num_shots_made = num_shots_made

    def get_description(self):
        """ Gets description of Forward """
        details = ("%d: %s %s is %.2f cm tall, weighs %.2f kg, drafted on %d, took %d shots and made %d") % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._num_shots_took, self._num_shots_made)
        return details

    def get_num_shots_took(self):
        """ Gets number of shots took """
        return self.num_shots_took

    def get_num_shots_made(self):
        """ Gets number of shots made """
        return self.num_shots_made
    
    def get_type(self):
        """ Gets player type """
        return AbstractPlayer.FORWARD_TYPE

    def to_dict(self):
        """ Returns a dictionary representation of a Forward """
        dict = {}
        dict['player_id'] = self.player_id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['height'] = self.height
        dict['weight'] = self.weight
        dict['year_drafted'] = self.year_drafted
        dict['player_type'] = self.player_type
        dict['num_shots_took'] = self.num_shots_took
        dict['num_shots_made'] = self.num_shots_made
        return dict