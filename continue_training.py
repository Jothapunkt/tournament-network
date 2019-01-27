from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
import copy

game = GameSim()
game.make_players(10)
game.players[0].import_player("networks/128988_95931.network")
game.train(1000)
game.players[0].export_player()


