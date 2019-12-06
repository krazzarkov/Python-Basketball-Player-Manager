from abstract_player import AbstractPlayer
from sqlalchemy import Column, String, Integer


class Guard(AbstractPlayer):

    num_steals = Column(Integer)
    num_assists = Column(Integer)

    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, player_type, num_steals, num_assists):
        super().__init__(player_id, first_name, last_name, height, weight, year_drafted, player_type)
        AbstractPlayer._validate_int("Number Steals", num_steals)
        AbstractPlayer._validate_int("Number Assists", num_assists)
        self.num_steals = num_steals
        self.num_assists = num_assists

    def get_description(self):
        """ Returns a description of Guard """
        details = ("%d: %s %s is %.2f cm tall, weighs %.2f kg, drafted on %d, has %d steals and %d assists") % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._num_steals, self._num_assists)
        return details

    
    def get_num_assists(self):
        """ Returns number of assists """
        return self.num_assists

    def get_num_steals(self):
        """ Returns number of steals """
        return self.num_steals
    
    def get_type(self):
        """ Returns the type of AbstractPlayer """
        return AbstractPlayer.GUARD_TYPE

    def to_dict(self):
        """ Returns a dictionary representation of a Guard """
        dict = {}
        dict['player_id'] = self.player_id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['height'] = self.height
        dict['weight'] = self.weight
        dict['year_drafted'] = self.year_drafted
        dict['player_type'] = self.player_type
        dict['num_steals'] = self.num_steals
        dict['num_assists'] = self.num_assists

        return dict