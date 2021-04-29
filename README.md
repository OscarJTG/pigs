# pigs
## Pigs dice game in Python.

Based on the Numberphile video called "The Math of Being a Pig - Numberphile",
uploaded to YouTube on 28 April 2021 (see https://www.youtube.com/watch?v=ULhRLGzoXQ0)

### Game instructions
Players roll a die (1-6). 
Rolling a 1 immediately ends the turn and gives zero points.
Rolling 2-6 gives the player the corresponding number of points (2 points if they roll a 2, etc...).
The player can end their turn and bank that score, or roll again to add more points to their score for that turn.
However, if the players rolls a 1, their turn immediately ends and they get zero points for that turn.

After that comes the other player's turn, which proceeds in the same way.

The player's total score is the sum of all the points that the player had at the end of their turn.

Play continues until one player manages to bank a total score of at least 100 - then this player wins!

### Information about the Python script

There are five game modes:

[0] - player vs player

[1] - player vs computer

[2] - computer vs player

[3] - computer vs computer

[4] - rapid computer vs computer

------------

Game modes [0] through to [3] print the results of each turn and have some delays added to inrease suspense before each "dice" roll.

[4] suppresses the output and has no delays, so that thousands of games can be played by the computers, to test which uses the best strategy.

By playing the same computer against itself 100,000 times, I found that Player 1 wins about 6.5% more games than player 2,
so being the first player confers a non-negligible advantage (which is not too surprising).

The computer playing strengths (from 29/04/2021) are in the following order:

E << A < B < C

from weakest to strongest.
