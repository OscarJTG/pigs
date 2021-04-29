#->pigs.py

import numpy as np 
from numpy import random
import time

def roll():
	return random.randint(1,7)



def humanTurn(print_=1):
	"""
	Human playing the pig game
	Printing output is default, but can be removed by setting argument != 1.

	Returns total score at the end of the turn.
	"""

	counter = 0 # keeps track of number of rolls in this turn
	scoretotal = 0 # keeps track of total score
	r = roll()
	counter = counter + 1
	scoretotal = scoretotal + r
	if print_ == 1:
		# print by default
		print("Roll", counter, "is", r)
		time.sleep(2)

	if r == 1:
		if print_ == 1:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(3)
		return 0
	while r < 7:
		rollagain = input("Would you like to roll again? [y/n]: ")
		if rollagain == "n":
			if print_ == 1:
				print("Total score this turn =", scoretotal)
				time.sleep(2)
			return scoretotal
		else:
			r = roll()
			counter = counter + 1
			scoretotal = scoretotal + r
			if print_ == 1:
				time.sleep(1)
				print("Roll", counter, "is", r)
				time.sleep(2)
			if r == 1:
				if print_ == 1:
					print("Sorry, zero points this turn.")
					time.sleep(3)
				return 0
		



def computerTurnA(print_ = 1):
	"""
	Computer playing the pig game
	Strategy: roll 5

	Returns total score at the end of the turn.
	"""

	counter = 0 # keeps track of number of rolls in this turn
	scoretotal = 0 # keeps track of total score
	r = roll()
	counter = counter + 1
	scoretotal = scoretotal + r
	if print_ == 1:
		print("Roll", counter, "is", r)
		time.sleep(1)
	if r == 1:
		if print_ == 1:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(3)
		return 0
	while counter < 5:
		r = roll()
		counter = counter + 1
		scoretotal = scoretotal + r
		if print_ == 1:
			print("Roll", counter, "is", r)
			time.sleep(1)
		if r == 1:
			if print_ == 1:
				print("Sorry, zero points this turn.")
				time.sleep(3)
			return 0

	# if computer rolls 5 times successfully:
	if print_ == 1:
		print("Total score this turn =", scoretotal)
	return scoretotal




def computerTurnB(print_ = 1):
	"""
	Computer playing the pig game
	Strategy: roll iff scoretotal < 20

	Returns total score at the end of the turn.
	"""

	counter = 0 # keeps track of number of rolls in this turn
	scoretotal = 0 # keeps track of total score
	r = roll()
	counter = counter + 1
	scoretotal = scoretotal + r
	if print_ == 1:
		print("Roll", counter, "is", r)
		time.sleep(1)
	if r == 1:
		if print_ == 1:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(3)
		return 0
	while scoretotal < 20:
		# roll again only if the score for this round is < 20
		r = roll()
		counter = counter + 1
		scoretotal = scoretotal + r
		if print_ == 1:
			print("Roll", counter, "is", r)
			time.sleep(1)
		if r == 1:
			if print_ == 1:
				print("Sorry, zero points this turn.")
				time.sleep(3)
			return 0

	# if computer rolls 5 times successfully:
	if print_ == 1:
		print("Total score this turn =", scoretotal)
	return scoretotal




def computerTurnC(comp_score, print_ = 1):
	"""
	Computer playing the pig game
	Less naive

	Returns total score at the end of the turn.
	"""

	counter = 0 # keeps track of number of rolls in this turn
	scoretotal = 0 # keeps track of total score
	r = roll()
	counter = counter + 1
	scoretotal = scoretotal + r
	if print_ == 1:
		print("Roll", counter, "is", r)
		time.sleep(1)
	if r == 1:
		if print_ == 1:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(3)
		return 0
	
	min_ = 20 # minimum score to bank, 20 by default
	if 100-comp_score < 20:
		min_ = 100 - comp_score # bank if computer gets enough points to win
	while scoretotal < min_:
		# roll again only if the score for this round is < min_
		r = roll()
		counter = counter + 1
		scoretotal = scoretotal + r
		if print_ == 1:
			print("Roll", counter, "is", r)
			time.sleep(1)
		if r == 1:
			if print_ == 1:
				print("Sorry, zero points this turn.")
				time.sleep(3)
			return 0

	# if computer rolls 5 times successfully:
	if print_ == 1:
		print("Total score this turn =", scoretotal)
	return scoretotal




def computerTurnRandom(print_ = 1):
	"""
	Computer playing the pig game
	Less naive

	Returns total score at the end of the turn.
	"""

	counter = 0 # keeps track of number of rolls in this turn
	scoretotal = 0 # keeps track of total score
	r = roll()
	counter = counter + 1
	scoretotal = scoretotal + r
	if print_ == 1:
		print("Roll", counter, "is", r)
		time.sleep(1)
	if r == 1:
		if print_ == 1:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(3)
		return 0
	
	num_rolls = random.randint(1,10) # number of turns to take
	while counter < num_rolls:
		# roll again only if the score for this round is < min_
		r = roll()
		counter = counter + 1
		scoretotal = scoretotal + r
		if print_ == 1:
			print("Roll", counter, "is", r)
			time.sleep(1)
		if r == 1:
			if print_ == 1:
				print("Sorry, zero points this turn.")
				time.sleep(3)
			return 0

	# if computer rolls 5 times successfully:
	if print_ == 1:
		print("Total score this turn =", scoretotal)
	return scoretotal




def computerTurn(difficulty, score, p=1):
	"""
	Play a turn as a computer of the appropriate difficulty level, 
	as inputted by the user at the start of the game.

	Arguments:
	difficulty: E,A,B,C from easiest through to hardest.
	p: if p=1, print results and apply time delays; otherwise, suppress these.
	"""
	if difficulty == "C":
		return computerTurnC(score, p)
	if difficulty == "B":
		return computerTurnB(p)
	if difficulty == "A":
		return computerTurnA(p)
	if difficulty == "R":
		return computerTurnRandom(p)



class Player:
	def __init__(self, score, human):
		self.score = score
		self.human = human



print("====================================")
print("Welcome! There are five game modes:")
print("[0] human vs human")
print("[1] human vs computer")
print("[2] computer vs human")
print("[3] computer vs computer")
print("[4] rapid computer vs computer")
print("====================================")

time.sleep(2)
gamemode = -1
while gamemode < 0 or gamemode > 4:
	try:
		gamemode = int(input("Please select a game mode (enter one integer): "))
	except ValueError:
		print("Error! To select a game mode, please enter a single digit integer from 0 to 4")

print("====================================")
print("Game starting")
print("====================================")
if gamemode != 4:
	time.sleep(2)

if gamemode != 0:
	print("Please select a difficulty level:")
	print("Random : R")
	print("Hard : A")
	print("Very Hard : B")
	print("Even Harder : C")

success_ = 0
while success_ == 0:
	if gamemode == 0:
		h1 = 1
		h2 = 1
		break
	if gamemode == 1:
		h1 = 1
		h2 = 0
		difficulty2 = input("Your selection: ")
		if difficulty2 == "R" or difficulty2 == "A" or difficulty2 == "B" or difficulty2 == "C":	
			break
		else:
			print("Please try again. Note that input is case sensitive.")	
	if gamemode == 2:
		h1 = 0
		h2 = 1
		difficulty1 = input("Your selection: ")
		if difficulty1 == "R" or difficulty1 == "A" or difficulty1 == "B" or difficulty1 == "C":
			break
		else:
			print("Please try again. Note that input is case sensitive.")	
	if gamemode == 3 or gamemode == 4:
		h1 = 0
		h2 = 0
		difficulty1 = input("Computer 1: ")
		difficulty2 = input("Computer 2: ")
		bool1_ = difficulty1 == "R" or difficulty1 == "A" or difficulty1 == "B" or difficulty1 == "C"
		bool2_ = difficulty2 == "R" or difficulty2 == "A" or difficulty2 == "B" or difficulty2 == "C"
		if bool1_ == True and bool2_ == True:
			break
		else:
			print("Please try again. Note that input is case sensitive.")


player1 = Player(0,h1)
player2 = Player(0,h2)

if player1.human == 1:
	print("Player 1 is human")
else:
	print("Player 1 is a computer")

if player2.human == 1:
	print("Player 2 is human")
else:
	print("Player 2 is a computer")


if gamemode != 4:
	turn = 0
	while player1.score < 100 and player2.score < 100:
		if turn % 2 == 0:
			print(" ")
			print("====================================")
			print("PLAYER 1")
			print("====================================")
			print(" ")
			if player1.human == 1:
				# human player turn
				player1.score = player1.score + humanTurn()
			else:
				# computer turn
				player1.score = player1.score + computerTurn(difficulty1, player1.score)
				

		if turn % 2 == 1:
			print(" ")
			print("====================================")
			print("PLAYER 2")
			print("====================================")
			print(" ")
			if player2.human == 1:
				# human player turn
				player2.score = player2.score + humanTurn()
			else:
				# computer turn
				player2.score = player2.score + computerTurn(difficulty2, player2.score)
			
		# print total player scores after each turn
		print("Player 1 total score = ", player1.score)
		print("Player 2 total score = ", player2.score)
		turn = turn + 1
		time.sleep(2)



	print("====================================")
	print("++++++++++++++++++++++++++++++++++++")
	print("====================================")
	if player1.score >= 100:
		print("PLAYER 1 WINS!!")
	if player2.score >= 100:
		print("PLAYER 2 WINS!!")
	print("====================================")
	print("++++++++++++++++++++++++++++++++++++")
	print("====================================")

else:
	# if gamemode = 4, do this instead:
	# i.e. run multiple computer vs computer games without delays and without printing intermediate results
	# only print number of wins for each computer
	N_it = int(input("Number of repeats: "))
	result = np.zeros(N_it)
	for i in range(N_it):
		# play the game N_it times
		
		# reset values
		player1.score = 0
		player2.score = 0
		turn = 0
		while player1.score < 100 and player2.score < 100:
			if turn % 2 == 0:
				player1.score = player1.score + computerTurn(difficulty1, player1.score, 0) # 0 suppresses printout

			if turn % 2 == 1:
				player2.score = player2.score + computerTurn(difficulty2, player2.score, 0)

			# increment turn counter
			turn = turn + 1

		# After loop ends, record the winner:	
		if player1.score >= 100:
			result[i] = 1
			#print("Computer 1 won", player1.score, player2.score)
		if player2.score >= 100:
			result[i] = -1
			#print("Computer 2 won", player1.score, player2.score)
		
	win1 = np.count_nonzero(result == 1)
	win2 = np.count_nonzero(result == -1)

	print("Computer 1 won", win1, "times.")
	print("Computer 2 won", win2, "times.")
	
