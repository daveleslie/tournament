This application is designed to be run from a linux OS with python and a postgreSQL server installed. a PostgreSQL database client (like psql for linux) is required to run the SQL code in tournament.sql

Follow these steps to run the application:

1. From the psql database client, create a new tournament database:
	CREATE DATABASE TOURNAMENT;
2. Connect to the database:
	\c tournament
3. Import the database schema from the tournament.sql file:
	\i tournament.sql
4. Exit the psql database client and run the unit tests from the command 		line with python:
	python tournament_test.py 