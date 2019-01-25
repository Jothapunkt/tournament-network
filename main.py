from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
import copy

game = GameSim()
game.make_players(35)
game.train(300)


