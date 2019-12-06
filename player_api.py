from flask import Flask, request
from guard import Guard
from forward import Forward
from center import Center
from player_stats import PlayerStats
from player_manager import PlayerManager
import json

app = Flask(__name__)

player_manager = PlayerManager("players.sqlite")

@app.route('/playermanager/players', methods=['POST'])
def add_player():
    """ Adds a player to the player manager """
    content = request.json

    try:
        if content["player_type"] == "center":
            center = Center(content["player_id"], content["first_name"], content["last_name"], content["height"], content["weight"], content["year_drafted"], content["player_type"], content["num_rebounds"], content["play_type"])
            player_manager.add_player(center)
        elif content["player_type"] == "forward":
            forward = Forward(content["player_id"], content["first_name"], content["last_name"], content["height"], content["weight"], content["year_drafted"], content["player_type"], content["num_shots_took"], content["num_shots_made"])
            player_manager.add_player(forward)
        elif content["player_type"] == "guard":
            guard = Guard(content["player_id"], content["first_name"], content["last_name"], content["height"], content["weight"], content["year_drafted"], content["player_type"], content["num_steals"], content["num_assists"])
            player_manager.add_player(guard)

        response = app.response_class(
            status=200,
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response

@app.route('/playermanager/players/<int:player_id>', methods=['GET'])
def get_player_by_id(player_id):
    """ Gets a player object by using player_id """

    try:
        player = player_manager.get_player(player_id)
        if player == None:
            response = app.response_class(
                response="player_id does not exist",
                status=404
            )
            return response
        response = app.response_class(
            status=200,
            response=json.dumps(player.to_dict()),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )

        return response


@app.route('/playermanager/players/<int:player_id>', methods=['DELETE'])
def remove_player_by_id(player_id):
    """ Removes a Player object by using player_id """

    try:
        player_manager.delete_player(player_id)

        response = app.response_class(
            status=200
        )

        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )

        return response

@app.route('/playermanager/playerstats', methods=['GET'])
def get_player_stats():
    """ Gets player stats """
    player_stats = player_manager.get_player_stats()
    num_players = player_stats.get_total_num_players()
    num_guards = player_stats.get_num_guards()
    num_forwards = player_stats.get_num_forwards()
    num_centers = player_stats.get_num_centers()
    avg_years_played = player_stats.get_avg_years_played()

    data = {}
    data["num_players"] = num_players
    data["num_guards"] = num_guards
    data["num_forwards"] = num_forwards
    data["num_centers"] = num_centers
    data["avg_years_played"] = avg_years_played

    response = app.response_class(
        status=200,
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

@app.route('/playermanager/players/all', methods=['GET'])
def get_all_players():
    """ Gets all players"""

    players = player_manager.get_all()
    player_list = []

    for player in players:
        data_json = player.to_dict()
        player_list.append(data_json)


    response = app.response_class(
        status=200,
        response=json.dumps(player_list),
        mimetype='application/json'
    )
    return response

@app.route('/playermanager/players/all/<string:type>', methods=['GET'])
def get_all_players_by_type(type):
    """ Gets all players by type"""

    try:
        print("type", type)
        players = player_manager.get_all_by_type(type)
        player_list = []

        for player in players:
            data_json = player.to_dict()
            player_list.append(data_json)


        response = app.response_class(
            status=200,
            response=json.dumps(player_list),
            mimetype='application/json'
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


@app.route('/playermanager/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    """ Updates an existing player"""

    content = request.json
    player = player_manager.get_player(player_id)
    if player == None:
        response = app.response_class(
        status=404
    )

    try:
        if content["player_type"] == "center":
            center = Center(content["player_id"], content["first_name"], content["last_name"], content["height"], content["weight"], content["year_drafted"], content["player_type"], content["num_rebounds"], content["play_type"])
            player_manager.update_player(center)
        elif content["player_type"] == "forward":
            forward = Forward(content["player_id"], content["first_name"], content["last_name"], content["height"], content["weight"], content["year_drafted"], content["player_type"], content["num_shots_took"], content["num_shots_made"])
            player_manager.update_player(forward)
        elif content["player_type"] == "guard":
            guard = Guard(content["player_id"], content["first_name"], content["last_name"], content["height"], content["weight"], content["year_drafted"], content["player_type"], content["num_steals"], content["num_assists"])
            player_manager.update_player(guard)

        response = app.response_class(
            status=200
        )

    except ValueError as e:
        response = app.response_class(
        response=str(e),
        status=404
    )
    return response


if __name__ == "__main__":
    app.run()