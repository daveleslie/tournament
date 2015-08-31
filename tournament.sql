-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--create the database


-- create the players table
CREATE TABLE players (
  player_id SERIAL PRIMARY KEY, name TEXT, wins INTEGER NOT NULL DEFAULT 0,
  losses INTEGER NOT NULL DEFAULT 0, matches INTEGER NOT NULL DEFAULT 0
);

--create the matches table
CREATE TABLE matches (
  match_id SERIAL PRIMARY KEY, winner INTEGER, loser INTEGER
);



