from gamesim import GameSim
from network import Network
from player import RemotePlayer
from mutator import Mutator
from random import *
from tournament_organizer import Tournament
import copy

tournament = Tournament()
tournament.random_tournament(13)
