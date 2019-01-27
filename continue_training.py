from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
import copy

game = GameSim()
game.make_players(10)

base = "networks/"
dir = ""
name = "203964_85377"

gens = 2000

game.players[0].import_player(base + dir + name + ".network")
game.train(gens)

if (gens%500 != 0):
	game.players[0].export_player()


