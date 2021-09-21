#! Python3
import random
import time
import os
import sys

if __name__ == "__main__":
	cwd = os.getcwd()
else:
	cwd = os.path.dirname(__file__)
sys.path.insert(0, cwd)
import game
import printouts


def number_strategy(print_=True):
	"""
	Computer playing the pig game
	Strategy: roll 5

	Returns total score at the end of the turn.
	"""

	roll_counter = 0
	cumulative_score = 0
	r = game.roll()
	roll_counter = roll_counter + 1
	cumulative_score = cumulative_score + r
	printouts.print_roll(roll_counter, r, print_)
	if r == 1:
		if print_ is True:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(0.5)
		return 0
	while roll_counter < 5:
		r = game.roll()
		roll_counter = roll_counter + 1
		cumulative_score = cumulative_score + r
		printouts.print_roll(roll_counter, r, print_)
		if r == 1:
			if print_ is True:
				print("Sorry, zero points this turn.")
				time.sleep(0.5)
			return 0

	# if computer rolls 5 times successfully:
	if print_ is True:
		print("Total score this turn =", cumulative_score)
	return cumulative_score


def score_strategy(print_=True):
	"""
	Computer playing the pig game
	Strategy: roll iff cumulative_score < 20

	Returns total score at the end of the turn.
	"""

	roll_counter = 0
	cumulative_score = 0
	
	r = game.roll()
	roll_counter = roll_counter + 1
	cumulative_score = cumulative_score + r
	printouts.print_roll(roll_counter, r, print_)
	if r == 1:
		if print_ is True:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(0.5)
		return 0
	while cumulative_score < 20:
		# roll again only if the score for this round is < 20
		r = game.roll()
		roll_counter = roll_counter + 1
		cumulative_score = cumulative_score + r
		if print_ is True:
			print("Roll", roll_counter, "is", r)
			time.sleep(1)
		if r == 1:
			if print_ is True:
				print("Sorry, zero points this turn.")
				time.sleep(0.5)
			return 0

	# if computer rolls 5 times successfully:
	if print_ is True:
		print("Total score this turn =", cumulative_score)
	return cumulative_score


def score_strategy_improved(target_score, print_=True):
	"""
	Computer playing the pig game.
	Uses score strategy without overshooting the target score (100).

	Returns total score at the end of the turn.
	"""

	roll_counter = 0 
	cumulative_score = 0
	
	r = game.roll()
	roll_counter = roll_counter + 1
	cumulative_score = cumulative_score + r
	printouts.print_roll(roll_counter, r, print_)
	if r == 1:
		if print_ is True:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(0.5)
		return 0
	
	min_ = 20 # minimum score to bank, 20 by default
	if 100 - target_score < 20:
		min_ = 100 - target_score
	while cumulative_score < min_:
		r = game.roll()
		roll_counter = roll_counter + 1
		cumulative_score = cumulative_score + r
		printouts.print_roll(roll_counter, r, print_)
		if r == 1:
			if print_ is True:
				print("Sorry, zero points this turn.")
				time.sleep(0.5)
			return 0

	if print_ is True:
		print(f"Total score this turn = {cumulative_score}.")
	return cumulative_score


def random_play(print_=True):
	"""
	Computer playing the pig game
	Less naive

	Returns total score at the end of the turn.
	"""

	roll_counter = 0
	cumulative_score = 0

	r = game.roll()
	roll_counter = roll_counter + 1
	cumulative_score = cumulative_score + r
	printouts.print_roll(roll_counter, r, print_)
	if r == 1:
		if print_ is True:
			print("Sorry, zero points this turn. Better luck next time!")
			time.sleep(0.5)
		return 0
	
	num_rolls = random.randint(1, 10) # number of turns to take
	while roll_counter < num_rolls:
		# roll again only if the score for this round is < min_
		r = game.roll()
		roll_counter = roll_counter + 1
		cumulative_score = cumulative_score + r
		printouts.print_roll(roll_counter, r, print_)
		if r == 1:
			if print_ is True:
				print("Sorry, zero points this turn.")
				time.sleep(0.5)
			return 0

	# if computer rolls 5 times successfully:
	if print_ is True:
		print("Total score this turn =", cumulative_score)
	return cumulative_score