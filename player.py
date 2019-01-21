from network import Network

class RemotePlayer(object):
	x = 150
	hspeed = 6
	width = 30
	height = 30
	dead = False
	
	controller = Network()
	def tick(self, game_data):
		inputs = game_data["inputs"]
		inputs.append(self.x / game_data["board_width"])
		
		self.controller.setInputs(inputs)
	