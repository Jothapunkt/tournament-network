from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
from tournament_organizer import Tournament
import copy

tournament = Tournament()

fname = "networks/usable/" + "16384_51424.network"

tournament.import_tournament(fname, 12)

