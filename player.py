from network import Network
from random import *
import math
import json

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
		self.controller.createNet(20,10,10,3)
		self.gen = 0
	
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
		
	def export_player(self):
		print("Exporting player #" + str(self.id) + " with final score of " + str(self.score))
		json_data = {}
		json_data["score"] = self.score
		json_data["inputs"] = self.controller.inputs
		json_data["layers"] = self.controller.layers
		json_data["generation"] = self.gen
		
		filename = "networks/" + str(self.score) + "_" + str(self.id) + ".network"
		with open(filename, "w") as json_file:
			json.dump(json_data, json_file)
			
	def import_player(self, fname):
		with open(fname, "r") as read_file:
			json_data = json.load(read_file)
			
		self.controller.inputs = json_data["inputs"]
		self.controller.layers = json_data["layers"]
		self.score = json_data["score"]