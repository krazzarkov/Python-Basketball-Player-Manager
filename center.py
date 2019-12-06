from abstract_player import AbstractPlayer
from sqlalchemy import Column, String, Integer

class Center(AbstractPlayer):

    num_rebounds = Column(Integer)
    play_type = Column(String(100))

    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, player_type, num_rebounds, play_type):
        super().__init__(player_id, first_name, last_name, height, weight, year_drafted, player_type)
        AbstractPlayer._validate_int("Number Rebounds", num_rebounds)
        AbstractPlayer._validate_string("Play Type", play_type)
        self.num_rebounds = num_rebounds
        self.play_type = play_type

    def get_description(self):
        """ Gets description of Center """
        details = ("%d: %s %s is %.2f cm tall, weighs %.2f kg, drafted on %d, has %d rebounds and plays %s") % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._num_rebounds, self._play_type)
        return details

    def get_num_rebounds(self):
        """ Gets number of rebounds """
        return self.num_rebounds

    def get_play_type(self):
        """ Gets play type """
        return self.play_type

    def get_type(self):
        """ Gets player type """
        return AbstractPlayer.CENTER_TYPE

    def to_dict(self):
        """ Returns a dictionary representation of a Center """
        dict = {}
        dict['player_id'] = self.player_id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['height'] = self.height
        dict['weight'] = self.weight
        dict['year_drafted'] = self.year_drafted
        dict['player_type'] = self.player_type
        dict['num_rebounds'] = self.num_rebounds
        dict['play_type'] = self.play_type

        return dict
