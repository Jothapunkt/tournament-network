from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
import copy

game = GameSim()
mutator = Mutator()

old_players = [900,800,700,600,500,400,300,200,100,5]

weights = []
for old_p_index,old_p in enumerate(old_players):
	w = (1 / ((old_p_index + 1) * (old_p_index + 1)))
	weights.append(w)
	
for i in range(30):
	print(old_players[game.weighted_pick(weights)])

