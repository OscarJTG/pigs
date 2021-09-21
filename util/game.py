#! Python3
import random
import numpy as np
import os
import sys
import time

if __name__ == "__main__":
	cwd = os.getcwd()
else:
	cwd = os.path.dirname(__file__)
sys.path.insert(0, cwd)
import printouts
import computers


def roll():
	return random.randint(1, 6)


def perform_roll(roll_counter, cumulative_score, print_=True):
	roll_result = roll()
	roll_counter += 1
	cumulative_score += roll_result
	printouts.print_roll(roll_counter, roll_result, print_)
	return roll_counter, cumulative_score, roll_result


def human_turn(print_=True):
	"""
	Human playing the pig game
	Printing output is default, but can be removed by setting argument != 1.

	Returns total score at the end of the turn.
	"""

	roll_counter = 0
	cumulative_score = 0

	roll_counter, cumulative_score, roll_result = perform_roll(roll_counter, cumulative_score)
	if roll_result != 1:
		while True:
			roll_again = input("Would you like to roll again? [y/n]: ")
			if roll_again == "n":
				break
			elif roll_again == "y":
				roll_counter, cumulative_score, roll_result = perform_roll(roll_counter, cumulative_score)
				if roll_result == 1:
					printouts.print_loss_message(print_)
					cumulative_score = 0
					break
			else:
				print("Did not understand input.")
				continue
	else:
		printouts.print_loss_message(print_)
		cumulative_score = 0
	printouts.print_total_score(cumulative_score, print_)
	return cumulative_score
	

def computer_turn(difficulty, score, print_=True):
	"""
	Play a turn as a computer of the appropriate difficulty level, 
	as inputted by the user at the start of the game.

	Arguments:
	difficulty: E,A,B,C from easiest through to hardest.
	p: if p=1, print results and apply time delays; otherwise, suppress these.
	"""
	if difficulty == "C":
		return computers.score_strategy_improved(score, print_)
	if difficulty == "B":
		return computers.score_strategy(print_)
	if difficulty == "A":
		return computers.number_strategy(print_)
	if difficulty == "R":
		return computers.random_play(print_)


def main_gameplay(player1, player2, difficulty1, difficulty2):
	turn = 0
	while player1.score < 100 and player2.score < 100:
		if turn % 2 == 0:
			player1.print_turn()
			if player1.human == 1:
				# human player turn
				player1.score = player1.score + human_turn()
			else:
				# computer turn
				player1.score = (player1.score 
					+ computer_turn(difficulty1, player1.score))
				
		if turn % 2 == 1:
			player2.print_turn()
			if player2.human == 1:
				# human player turn
				player2.score = player2.score + human_turn()
			else:
				# computer turn
				player2.score = (player2.score 
					+ computer_turn(difficulty2, player2.score))
			
		# print total player scores after each turn
		print("Player 1 total score = ", player1.score)
		print("Player 2 total score = ", player2.score)
		turn += 1
		time.sleep(0.5)

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
	return


def fast_gameplay(player1, player2, difficulty1, difficulty2):
	# if gamemode == 4, do this instead:
	# i.e. run multiple computer vs computer games without delays 
	# and without printing intermediate results.
	# Only prints number of wins for each computer.
	N_it = int(input("Number of repeats: "))
	result = np.zeros(N_it)
	for i in range(N_it):
		# reset values
		player1.score = 0
		player2.score = 0
		turn = 0
		while player1.score < 100 and player2.score < 100:
			if turn % 2 == 0:
				player1.score = (player1.score 
					+ computer_turn(difficulty1, player1.score, False))

			if turn % 2 == 1:
				player2.score = (player2.score 
					+ computer_turn(difficulty2, player2.score, False))

			turn += 1

		if player1.score >= 100:
			result[i] = 1
		if player2.score >= 100:
			result[i] = -1
		
	win1 = np.count_nonzero(result == 1)
	win2 = np.count_nonzero(result == -1)

	print(f"Computer 1 won {win1} times.")
	print(f"Computer 2 won {win2} times.")