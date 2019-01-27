from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
import copy

game = GameSim()
game.make_players(10)
game.train(100)
game.players[0].export_player()


