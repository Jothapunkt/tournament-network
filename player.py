from network import Network
from random import *
import math

class RemotePlayer(object):
	def __init__(self):
		score = 0
		x = 150
		hspeed = 6
		width = 30
		height = 30
		dead = False
		id = math.floor(random() * 100000)
		
		controller = Network()
		controller.createNet(5,3)
	
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