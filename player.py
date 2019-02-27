from network import Network
from random import *
import math
import json

class RemotePlayer(object):
	def __init__(self):
		self.score = 0
		self.x = 0
		
		self.vspeed = 4
		self.width = 10
		self.height = 75
		self.dead = False
		self.id = math.floor(random() * 100000)
		
		self.board_width = 1000
		self.board_height = 500
		
		self.y = 0.5 * (self.board_height - self.height)
		
		self.controller = Network()
		self.controller.createNet(15,20,3)
		self.gen = 0
		
		self.last_move = "neutral"
	
	def tick(self, inputs):
		self.controller.setInputs(inputs)
		movements = self.controller.calcNetwork()
		
		vdiff = 0
		self.last_move = "neutral"
		
		if (movements[0] > movements[1] and movements[0] >= movements[2]):
			vdiff = -self.vspeed
			self.last_move = "up"
		if (movements[2] > movements[1] and movements[2] > movements[0]):
			vdiff = self.vspeed
			self.last_move = "down"
			
		self.y += vdiff
		
		if (self.y < 0):
			self.y = 0
		if (self.y > (self.board_height - self.height)):
			self.y = self.board_height - self.height
		
	def align_left(self):
		self.x = 0
		
	def align_right(self):
		self.x = self.board_width - self.width
	
	def reset_player(self):
		self.y = 0.5 * (self.board_height - self.height)
		
	def export_player(self):
		json_data = {}
		json_data["score"] = self.score
		json_data["inputs"] = self.controller.inputs
		json_data["layers"] = self.controller.layers
		json_data["generation"] = self.gen
		
		filename = "networks/" + str(self.score) + "_" + str(self.id) + "_" + str(math.floor(random() * 100000)) + ".network"
		with open(filename, "w") as json_file:
			json.dump(json_data, json_file)
			
		print("Exporting player #" + str(self.id) + " to file '" + filename + "'")
			
	def import_player(self, fname):
		with open(fname, "r") as read_file:
			json_data = json.load(read_file)
			
		self.controller.inputs = json_data["inputs"]
		self.controller.layers = json_data["layers"]
		self.score = json_data["score"]