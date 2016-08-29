# NBA Stats

## Part One

In `app.py`, there is provided code that loops through the CSV file
containing NBA player stats.

Modify the code in app.py to:

1. import sqlalchemy functions and classes
1. create a `Base` class
1. create a `Player` class that inherits from `Base`
1. create a `player` table
1. create a `DBSession`
1. add each player to the session
1. save each player instance to the DB

## Part Two

Reference the documentation on querying:

- http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#querying
- http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#querying
- http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators

and use `.query` to find answers to the below prompts.

The first one has been done for you.

1. All columns for all players from the New York Knicks (NYK)

> `session.query(Player).filter_by(team='NYK')`

It may help to think about the SQL being executed as well:

> `SELECT * from player WHERE team = 'NYK';`

2. All columns for all players from the Indiana Packers (IND) who are under 26 years old

> `session.query(Player).filter_by(team='IND').filter(Player.age < 26).all()`

3. All columns for all players, ordered from least points scored to most points scored

> `session.query(Player).order_by(Player.points).all()`

4. Players with the top 20 points per game

> `session.query(Player).order_by("points desc").limit(20).all()`

5. The average age for all players

> `session.query(func.avg(Player.age))`

6. The average age for all players on the Oklahoma City Thunder (OKC)

> `session.query(func.avg(Player.age)).filter_by(team='OKC').all()`

7. The average age for all players who played more than 40 games

> `session.query(func.avg(Player.age)).filter(Player.game > 40).all()`

#### Bonus

1. The team and total points scored from all players on that team (team points), ordered from most team points to least
1. Age and the average points per game for that age, ordered from youngest to oldest
1. Team and the the number of players who score above 12 points per game on that team, ordered from most to least
