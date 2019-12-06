import sqlite3

conn = sqlite3.connect('players.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE players
          ''')

conn.commit()
conn.close()
