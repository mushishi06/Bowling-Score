# Bowling-Score

This project is coded using Python3 (NOT Tested with python2).

All the code comply with [PEP 8](https://www.python.org/dev/peps/pep-0008/ "Official Docs").


### Rule:

Ten-pin bowling scoring rules: http://en.wikipedia.org/wiki/Ten-pin_bowling#Scoring

### Goal:

Create a Python class that will keep accurate score in a ten-pin bowling match
for a single player, with unit tests in place to prove the accuracy of your scoring
mechanism.

Feel free to use any 3rd party libraries if they’re beneficial to the overall
solution.

## Testing:

All the test are writen using [unittest](https://docs.python.org/3/library/unittest.html#module-unittest "Unittest Docs") Framework.

Execute the commande: `python3 test_bowling_game.py` to run the test suite.


## Play in Python console:

After Downloaded/clone this repo, go in the folder `Bowling-Score`.

Launch the python3 console `python3`.

Import the main class:
>from bowling_game import BowlingGame

Intanciation of the class:
>mygame = BowlingGame()

PS: Your can pass your Name as string `mygame = BowlingGame("Romain")`

Then to Print the scoreboard:
>mygame.scoresheet()

#### Then play with the falowwing function:

`mygame.roll(pins)` for launch the ball.

`mygame.ranroll()` for launch randomly the ball.

`mygame.total_score()` give you your current score.


