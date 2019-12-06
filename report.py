from abstract_player import AbstractPlayer
from player_manager import PlayerManager
from player_stats import PlayerStats
from guard import Guard
from forward import Forward
from center import Center

def main():

    player_manager = PlayerManager("Los Angeles Lakers", "file.txt")
    player1 = Forward(23, "Lebron", "James", 201, 81, 2003, "forward", 1028, 690)
    player2 = Center(12, "Dwight", "Howard", 210, 90, 2002, "center", 1054, "Aggresive")
    player3 = Guard(10, "Rajon", "Rondo", 190, 76, 2004, "guard", 909, 1203)

    player_manager.add_player(player1)
    player_manager.add_player(player2)
    player_manager.add_player(player3)

    print_report(player_manager)

    player_manager.delete_player(12)
    player_manager.delete_player(10)

    print_report(player_manager)

    player1 = Forward(23, "Yeet", "James", 69, 81, 2003, "forward", 1028, 690)
    player_manager.update_player(player1)

    print_report(player_manager)

    print(player_manager.get_player(23))


def print_report(player_manager):
    stats = player_manager.get_players_stats()

    print("Report for %s" % player_manager.get_team_name())
    print("  Number of Guards: %d" % stats.get_num_guards())
    print("  Number of Forwards: %d" % stats.get_num_forwards())
    print("  Number of Centers: %d" % stats.get_num_centers())
    print(player_manager.get_all_by_type())
    
if __name__ == "__main__":
    main()