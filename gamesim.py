import math
from random import *

class GameSim(object):
	levels = []
	players = []
	dead_players = []
	gen = 0
	active_level = []
	active_level_index = 2
	vspeed = 6
	y = 0
	
	def make_levels(self):
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
	'''
	Checks if a block is at the given position
	'''
	def collides_at_position(self, x, y):
		x_index = math.floor(x/50)
		y_index = math.floor(y/50)
		
		#print(str(x_index) + "|" + str(y_index))
		
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
		if (self.collides_at_position(p.x, self.y + y.height)):
			return True
		#bottom-right corner
		if (self.collides_at_position(p.x + p.width, self.y + p.height)):
			return True
		
		return False
		
	def __init__(self):
		self.make_levels()
	
	def tick(self):
		#Make game data
		game_data = []
		
		min_row = math.floor(self.y/50)
		
		for i in range(5):
			
		
		
		#Execute player movement
		
		
		#Check player collision
		
		
		
	def make_players(self, count):
		self.players = []
		