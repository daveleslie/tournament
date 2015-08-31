__author__ = 'David'

import psycopg2

def connect():
    """Connect to the PostgreSQL database and return a connection object"""
    return psycopg2.connect("dbname=tournament")

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT player_id, name, wins, matches FROM players "
              "ORDER BY wins DESC;")
    standings = c.fetchall()
    DB.close()
    print "\nRows: \n"
    for row in standings:
        print "   ", row

playerStandings()