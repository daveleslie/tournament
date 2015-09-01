## Swiss-style tournament results database

This is a project submitted for the Udacity Fullstack nanodegree online course. It sets up a PostgreSQL database and then tests the suitability of the database for facilitating the scoring of a swiss-style tournament by making use of the psyopg2 database API.

#### The following steps are required to run the application:

##### 1. Setup your environment
1. Install [Vagrant](vagrantup.com) and [VirtualBox](virtualbox.org)
2. Clone the tournament repository

##### 2. Start your vagrant session
3. type 'vagrantup' from the commandline
4. connect to virtualbox through vagrant by typing 'vagrant ssh' from the command line
5. change to the shared folder where you cloned the repository by typing 'cd /foldername' where 'foldername' is the directory of the clones repository

##### 3. Open the PostgreSQL database client and import database schema
6. from the commandline type 'psql'
7. setup the database by typing \i tournament.sql
8. exit psql by typing \q

##### 4. Run the unit tests
8. from the command line type 'python tournament_test.py'
