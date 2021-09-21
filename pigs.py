#! Python3

import numpy as np 
from numpy import random
import time
from util import computers, game, printouts


class Player:
	def __init__(self, score, human, number):
		self.score = score
		self.human = human
		self.number = number

	def print_player_type(self):
		if self.human is True:
			print(f"Player {self.number} is a human.")
		else:
			print(f"Player {self.number} is a computer.")
		return

	def print_turn(self):
		print("\n====================================")
		print(f"PLAYER {self.number}")
		print("====================================\n")
		return


def select_gamemode():
	gamemode = -1
	while gamemode < 0 or gamemode > 4:
		try:
			gamemode = int(input("Please select a game mode: "))
		except ValueError:
			print("Error! To select a game mode, please enter a single digit integer from 0 to 4")
	return gamemode


def initialise_players(gamemode):
	if gamemode != 0:
		printouts.select_difficulty_text()
	difficulty1 = "R"
	difficulty2 = "R"
	success_ = 0
	while success_ == 0:
		if gamemode == 0:
			h1 = True
			h2 = True
			break
		elif gamemode == 1:
			h1 = True
			h2 = False
			difficulty2 = input("Your selection: ")
			if (difficulty2 == "R" or difficulty2 == "A" 
				or difficulty2 == "B" or difficulty2 == "C"):	
				break
			else:
				print("Please try again. Note that input is case sensitive.")	
		elif gamemode == 2:
			h1 = False
			h2 = True
			difficulty1 = input("Your selection: ")
			if (difficulty1 == "R" or difficulty1 == "A" 
				or difficulty1 == "B" or difficulty1 == "C"):
				break
			else:
				print("Please try again. Note that input is case sensitive.")	
		elif gamemode == 3 or gamemode == 4:
			h1 = False
			h2 = False
			difficulty1 = input("Computer 1: ")
			difficulty2 = input("Computer 2: ")
			bool1_ = (difficulty1 == "R" or difficulty1 == "A" 
				or difficulty1 == "B" or difficulty1 == "C")
			bool2_ = (difficulty2 == "R" or difficulty2 == "A" 
				or difficulty2 == "B" or difficulty2 == "C")
			if bool1_ == True and bool2_ == True:
				break
			else:
				print("Please try again. Note that input is case sensitive.")

	player1 = Player(0, h1, 1)
	player2 = Player(0, h2, 2)
	return player1, player2, difficulty1, difficulty2


if __name__ == "__main__":
	printouts.introduction_text()
	time.sleep(0.5)
	gamemode = select_gamemode()
	printouts.game_start_text()

	player1, player2, difficulty1, difficulty2 = initialise_players(gamemode)
	player1.print_player_type()
	player2.print_player_type()

	if gamemode != 4:
		game.main_gameplay(player1, player2, difficulty1, difficulty2)
	else:
		game.fast_gameplay(player1, player2, difficulty1, difficulty2)