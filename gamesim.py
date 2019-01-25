import math
from random import *
from player import RemotePlayer
from mutator import Mutator
import copy

class GameSim(object):
	def __init__(self):
		self.mutator = Mutator()
		self.levels = []
		self.players = []
		self.dead_players = []
		self.gen = 0
		self.active_level = []
		self.active_level_index = 2
		self.vspeed = 6
		self.y = 0
		self.current_tick = 0
		self.block_size = 50
		self.board_width = 500

		self.levels = []
		
		l1 = []
		l1.append("1000000001");
		l1.append("1000000001");
		l1.append("1100000011");
		l1.append("1110000111");
		l1.append("1110001111");
		l1.append("1110011111");
		l1.append("1110011111");
		l1.append("1111001111");
		l1.append("1000000001");
		l1.append("1111101111");
		l1.append("1000000001");
		l1.append("1000000001");
		l1.append("1000000001");
		l1.append("1111011111");
		l1.append("1000000001");
		l1.append("1000000001");
		l1.append("1000000001");
		l1.append("1000100001");
		l1.append("1111111111");
		
		l2 = []
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000100001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1110000111");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1010000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1111110011");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1100000011");
		l2.append("1110000111");
		l2.append("1110001111");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1110011111");
		l2.append("1110011111");
		l2.append("1111001111");
		l2.append("1000000001");
		l2.append("1111101111");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1111011111");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000000001");
		l2.append("1000100001");
		l2.append("1111111111");
		
		l3 = []
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1111011111");
		l3.append("1111011111");
		l3.append("1111011111");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1111111001");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1001111111");
		l3.append("1000000001");
		l3.append("1000000001");
		l3.append("1110000001");
		l3.append("1111111111");
		
		terrain_table1 = []
		for row in l1:
			r = []
			for char in row:
				if char is '0':
					r.append(False)
				else:
					r.append(True)
			terrain_table1.append(r)
		
		terrain_table2 = []
		for row in l2:
			r = []
			for char in row:
				if char is '0':
					r.append(False)
				else:
					r.append(True)
			terrain_table2.append(r)
				
		terrain_table3 = []
		for row in l3:
			r = []
			for char in row:
				if char is '0':
					r.append(False)
				else:
					r.append(True)
			terrain_table3.append(r)
		
		self.levels.append(terrain_table1)
		self.levels.append(terrain_table2)
		self.levels.append(terrain_table3)
		
		self.active_level = self.levels[self.active_level_index]
		
	def train(self, max_gen):
		self.gen = 0
		while(self.gen < max_gen):
			self.tick()
			
	'''
	Checks if a block is at the given position
	'''
	def collides_at_position(self, x, y):
		x_index = math.floor(x/self.block_size)
		y_index = math.floor(y/self.block_size)
		
		if (x_index < 0 or y_index < 0):
			return True
			
		if (y_index > len(self.active_level) or x_index > len(self.active_level[y_index])):
			return True
		
		return (self.active_level[y_index][x_index])
		
	def collides(self, p):
		#top-left corner
		if (self.collides_at_position(p.x, self.y)):
			return True
		#top-right corner
		if (self.collides_at_position(p.x + p.width, self.y)):
			return True
		
		#bottom-left corner
		if (self.collides_at_position(p.x, self.y + p.height)):
			return True
		#bottom-right corner
		if (self.collides_at_position(p.x + p.width, self.y + p.height)):
			return True
		
		return False
	
	def has_survivors(self):
		all_dead = True
		for p in self.players:
			if not p.dead:
				all_dead = False
		return (not all_dead)
	
	def tick(self):
		self.current_tick += 1
		#print(self.current_tick)
		
		#Make game data
		game_data = {}
		game_data["inputs"] = []
		
		min_row = math.floor(self.y/self.block_size)
		game_data["board_width"] = self.board_width
		
		#Append 5 rows of blocks as inputs
		for i in range(5):
			if ((min_row + i) >= len(self.active_level)):
				for i in range(int(game_data["board_width"]/self.block_size)):
					game_data["inputs"].append(1)
			else:
				row = self.active_level[min_row + i]
				for block in row:
					if block:
						game_data["inputs"].append(1)
					else:
						game_data["inputs"].append(0)
		
		game_data["inputs"].append((self.y % self.block_size)/self.block_size)
		
		#Execute player movement		
		for p in self.players:
			if (p.dead is False):
				p.tick(game_data)
		
		#Check player collision
		for p in self.players:
			if (p.dead is False):	
				if (self.collides(p)):
					p.score = self.score(p)
					p.dead = True
					self.dead_players.append(p)					
		#Check for surviving players
		if not self.has_survivors():
			self.next_gen()
			
		#Move field
		self.y += self.vspeed
	
	def sort_players(self, players):
		done = False
		while not done:
			done = True
			for index in range(len(players) - 1):
				if players[index].score < players[index+1].score:
					#Swap players
					done = False
					buffer_player = players[index]
					players[index] = players[index+1]
					players[index+1] = buffer_player
		return players
		
	
	def next_gen(self):
		self.gen += 1
		old_players = self.sort_players(self.players)
		
		population_size = len(old_players)
		
		self.players = []
		
		#Keep best candidate
		self.players.append(old_players[0])
		
		#Append random players
		while(len(self.players) < 0.2*len(old_players)):
			self.players.append(RemotePlayer())
		
		weights = []
		for old_p_index,old_p in enumerate(old_players):
			w = (1 / ((old_p_index + 1) * (old_p_index + 1)))
			weights.append(w)
		
		#Fill rest of slots with mutated versions of old players
		#Selection of players to mutate is made via a weighted pick. Better players have far better chances to be picked
		while(len(self.players) < population_size):
			to_mutate = old_players[self.weighted_pick(weights)]
			self.players.append(self.mutate_player(to_mutate))
		
		scores = []
		for p in old_players:
			scores.append(p.score)
		print(scores)
		
		self.restart_level()
		
	def restart_level(self):
		self.y = 0
		startX = 150
		self.current_tick = 0
		self.dead_players = []
		
		for player in self.players:
			player.dead = False
			player.x = startX
	
	def mutate_player(self, p):
		new_p = copy.deepcopy(p)
		new_p.controller = self.mutator.mutate(new_p.controller)
		return new_p
			
	def players_alive(self):
		sum = 0
		for p in self.players:
			if not p.dead:
				sum += 1
		return sum
	
	def players_dead(self):
		sum = 0
		for p in self.players:
			if p.dead:
				sum += 1
		return sum
		
	def weighted_pick(self, weights):
		sum = 0
		for weight in weights:
			sum += weight
		r = random() * sum
		
		index = 0
		weight_sum = weights[0]
		while(weight_sum < r):
			index += 1
			weight_sum += weights[index]
		return index
		
	def score(self, p):
		#Scores players fitness by how long they survived and how far they were from the nearest edge
		s = self.current_tick * 1000
		x_buffer = p.x
		
		dist_left = 999
		dist_right = 999
		
		#Find nearest edge to the left. If no edge is found, dist_left remains at 999
		while(self.collides(p) and p.x >= 0):
			p.x -= p.hspeed
		
		if not self.collides(p):
			dist_left = x_buffer - p.x
		
		p.x = x_buffer #Reset x
		
		#Find nearest edge to the left. If no edge is found, dist_left remains at 999
		while(self.collides(p) and p.x <= self.board_width - self.block_size):
			p.x += p.hspeed
		
		if not self.collides(p):
			dist_right = p.x - x_buffer
		
		p.x = x_buffer
		
		#The smaller of the two distances is used in final score
		dist = dist_right
		if (dist_left < dist_right):
			dist = dist_left
		
		#print("Dead: " + str(p.id))
		return (s - dist)	
		
	def make_players(self, count):
		if (count < 1):
			return
		self.players = []
		for i in range(count):
			rem = RemotePlayer()
			self.players.append(rem)