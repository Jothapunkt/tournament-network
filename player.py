from network import Network
from random import *
import math

class RemotePlayer(object):
	def __init__(self):
		self.score = 0
		self.x = 150
		self.hspeed = 6
		self.width = 30
		self.height = 30
		self.dead = False
		self.id = math.floor(random() * 100000)
		
		self.controller = Network()
		self.controller.createNet(5,3)
	
	def tick(self, game_data):
		inputs = []
		for input in game_data["inputs"]:
			inputs.append(input)
			
		inputs.append(self.x / game_data["board_width"])
		
		self.controller.setInputs(inputs)
		movements = self.controller.calcNetwork()
		
		hdiff = 0
		if (movements[0] > movements[1] and movements[0] >= movements[2]):
			hdiff = -self.hspeed
		if (movements[2] > movements[1] and movements[2] >= movements[0]):
			hdiff = self.hspeed
			
		self.x += hdiff
		
		#print("Player " + str(self.id) + ": X" + str(self.x) + " (" + str(hdiff) + ")")