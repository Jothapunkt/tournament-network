from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
from tournament_organizer import Tournament
import copy

tournament = Tournament()

#File name
fname = "networks/usable/" + "27118_49762_11315.network"

#Number of tournaments in the series. Negative number for infinite tournaments
rounds = -1

winner = tournament.import_tournament(fname, 8)

while(rounds != 0):
	rounds -= 1
	winner = tournament.continue_tournament(winner, 8)
