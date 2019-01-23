from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
import copy

game = GameSim()
mutator = Mutator()

game.make_players(5)
mutator = Mutator()
print("Networks identical: " + str(mutator.compare_nets(game.players[0].controller, game.players[1].controller)))
print("Players created: " + str(len(game.players)))
print("Survivors exist: " + str(game.has_survivors()))
#game.train(10)

playerA = RemotePlayer()
playerB = RemotePlayer()

inputs = []
inputs.append(random())
inputs.append(random())
for i in range(50):
	if (random() > 0.5):
		inputs.append(1)
	else:
		inputs.append(0)
		
playerA.controller.setInputs(inputs)
playerB.controller.setInputs(inputs)

print("Networks identical: " + str(mutator.compare_nets(playerA.controller, playerB.controller)))

playerA.controller.print_net()
playerB.controller.print_net()



