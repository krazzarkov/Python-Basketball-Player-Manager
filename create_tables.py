import sqlite3

conn = sqlite3.connect('players.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE players
          (player_id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(100) NOT NULL,
           last_name VARCHAR(100) NOT NULL,
           height INTEGER NOT NULL,
           weight INTEGER NOT NULL,
           year_drafted INTEGER NOT NULL,
           player_type VARCHAR(100) NOT NULL,
           num_shots_took INTEGER,
           num_shots_made INTEGER,
           num_steals INTEGER,
           num_assists INTEGER,
           num_rebounds INTEGER,
           play_type VARCHAR(100))
          ''')

conn.commit()
conn.close()
