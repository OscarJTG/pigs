#! Python3

import time

def print_roll(roll_counter, r, print_, delay=0.2):
	if print_ is True:
		print(f"Roll #{roll_counter}: {r}.")
		time.sleep(delay)
	return


def print_loss_message(print_, delay=0.5):
	if print_ is True:
		print("Sorry, zero points this turn. Better luck next time!")
		time.sleep(delay)
	return


def print_total_score(cumulative_score, print_, delay=0.5):
	if print_ is True:
		print(f"Total score this turn:  {cumulative_score}.")
		time.sleep(delay)
	return


def introduction_text():
	print("====================================")
	print("Welcome! There are five game modes:")
	print("[0] human vs human")
	print("[1] human vs computer")
	print("[2] computer vs human")
	print("[3] computer vs computer")
	print("[4] rapid computer vs computer")
	print("====================================")
	return


def game_start_text():
	print("====================================")
	print("Game starting")
	print("====================================")
	return

def select_difficulty_text():
	print("Please select a difficulty level:")
	print("     Random : R")
	print("       Hard : A")
	print("  Very Hard : B")
	print("Even Harder : C")
	return