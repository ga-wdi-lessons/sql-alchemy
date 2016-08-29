# NBA Stats

## Part One

In code/03-nba-stats, there is provided code that loops through the CSV file
containing NBA player stats.

Modify the code in app.py to:

1. Create a player table
1. Create a Player model
1. Insert each of the players into the database

## Part Two

Reference the documentation

- http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#querying
- http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#querying

and use `.query` to find answers to the below prompts. The first one has been done for you.

1. All columns for all players from the New York Knicks (NYK)

> `session.query(Player).filter_by(team='NYK')`

2. All columns for all players from the Indiana Packers (IND) who are under 26 years old

3. All columns for all players, ordered from least points scored to most points scored
4. Name and Points per game (points/games), for the players with the top 20 points per game
5. The average age for all players
6. The average age for all players on the Oklahoma City Thunder (OKC)
7. The average age for all players who played more than 40 games
8. The team and total points scored from all players on that team (team points), ordered from most team points to least

#### Bonus

1. Age and the average points per game for that age, ordered from youngest to oldest
1. Team and the the number of players who score above 12 points per game on that team, ordered from most to least
