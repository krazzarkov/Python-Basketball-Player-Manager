class PlayerStats:
    """ Statistics on a basketball team """

    #def __init__ (self, total_num_players, num_guards, num_forwards, num_centers, avg_years_played):

    _player_manager = None

    def __init__(self, player_manager):
        self._player_manager = player_manager

    def get_total_num_players(self):
        """ Returns the number of total players """
        total_num_players = self._player_manager.get_all()
        return len(total_num_players)

    def get_num_guards(self):
        """ Returns the number of guards """
        total_num_guards = self._player_manager.get_all_by_type("guard")
        return len(total_num_guards)
    
    def get_num_forwards(self):
        """ Returns the number of forwards """
        total_num_forwards = self._player_manager.get_all_by_type("forward")
        return len(total_num_forwards)

    def get_num_centers(self):
        """ Returns the number of centers """
        total_num_centers = self._player_manager.get_all_by_type("center")
        return len(total_num_centers)

    def get_avg_years_played(self):
        """ Returns the average years played """
        all_players = self._player_manager.get_all()
        for player in all_players:
            number = player.get_player_year_drafted()
            number2 = 2019 - number
            number3 = 0
            number3 = number3 + number2
        avg_years_played = number3 / len(all_players)
        return avg_years_played
