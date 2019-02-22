import copy

from game_data import *
from gamesim import GameSim

game = GameSim()

left = "networks/usable/" + "8192_7148.network"
right = "networks/usable/" + "8192_59044.network"
switch = True

if (switch):
	buffer = left
	left = right
	right = buffer

game.import_left(left)
game.import_right(right)

game.play_match(record=True)

