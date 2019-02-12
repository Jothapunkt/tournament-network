import math
from random import *
from player import RemotePlayer
from mutator import Mutator
import copy
from gamesim import GameSim
from game_data import *
from ball import *

class Tournament(object):
	def __init__(self):
		self.mutator = Mutator()
		self.data = GameData() #Game Data is stored in singleton
		self.players = []
		self.total_players = 0
		self.matches_played = 0
		self.data = GameData()
		self.game = GameSim()
	
	def random_tournament(self,rounds): #rounds is the number of KO rounds played. There are 2^rounds random players in total, e.g. 15
		self.players = []
		self.total_players = 2 ** rounds
		self.matches_played = 0
		 
		print("-- Random Tournament --")
		print("Total players: " + str(self.total_players))
		
		for i in range(self.total_players):
			p = RemotePlayer()
			p.score = self.total_players
			
			self.players.append(p)
		
		#Non-final rounds
		while (len(self.players) > 2): 
			i = 0
			new_players = []
			while(i < len(self.players) - 1):
				self.data.set("playerLeft", self.players[i])
				self.data.set("playerRight", self.players[i+1])
				if (self.game.play_match() == "left"):
					new_players.append(self.players[i])
				else:
					new_players.append(self.players[i+1])
				self.matches_played += 1
				i += 2
				print("Matches played: " + str(self.matches_played) + "/" + str(self.total_players - 1))
			self.players = new_players