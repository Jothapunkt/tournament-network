import math
from random import *
from player import RemotePlayer
from mutator import Mutator
import copy
from game_data import *
from ball import *
import time

class GameSim(object):
	def __init__(self):
		self.mutator = Mutator()
		self.data = GameData() #Game Data is stored in singleton
		self.data.set("playerLeft",RemotePlayer())
		self.data.get("playerLeft").align_left()
		self.data.set("playerRight",RemotePlayer())
		self.data.get("playerRight").align_right()
		self.ball = Ball()
		self.ball2 = SecondBall()
		self.data.set("lastScore", "left")
		self.board_width = 1000
		self.board_height = 500
		self.recording = []
	
	def sig(self, x):
		return 1 / (1 + math.exp(-x))
	
	def play_point(self,max_ticks=6000,record=False): #Max 120s per point at 50tps
		current_tick = 0
		initalScoreLeft = self.data.get("scoreLeft",0)
		initialScoreRight = self.data.get("scoreRight",0) 
		while(current_tick < max_ticks and self.data.get("scoreLeft",0) == initalScoreLeft and self.data.get("scoreRight",0)  == initialScoreRight):
			self.tick()
			if (record):
				tick_data = []
				tick_data.append(self.data.get("playerLeft").x)
				tick_data.append(self.data.get("playerLeft").y)
				tick_data.append(self.ball.x)
				tick_data.append(self.ball.y)
				tick_data.append(self.ball2.x)
				tick_data.append(self.ball2.y)
				tick_data.append(self.data.get("playerRight").x)
				tick_data.append(self.data.get("playerRight").y)
				tick_data.append(self.data.get("scoreLeft",0))
				tick_data.append(self.data.get("scoreRight",0))
				self.recording.append(tick_data)
			current_tick += 1
	
	def game_info(self, extraInfo=""):
		print("--Game Info--")
		if extraInfo != "":
			print(extraInfo)
		print("Ball: x" + str(self.ball.x) + " y" + str(self.ball.y) + " hsp" + str(self.ball.hspeed) + " vsp" + str(self.ball.vspeed))
		print("Ball 2: x" + str(self.ball2.x) + " y" + str(self.ball2.y) + " hsp" + str(self.ball2.hspeed) + " vsp" + str(self.ball2s.vspeed))
		print("Player left: y" + str(self.data.get("playerLeft").y))
		print("Player right: y" + str(self.data.get("playerRight").y))
	
	def tick(self):
		self.ball.tick()
		self.ball2.tick()
		
		inputsLeft = []
		inputsLeft.append(self.data.get("playerLeft").y/self.board_height)
		inputsLeft.append(self.ball.x / self.board_width)
		inputsLeft.append(self.ball.y / self.board_height)
		inputsLeft.append(self.sig(self.ball.hspeed))
		inputsLeft.append(self.sig(self.ball.vspeed))
		inputsLeft.append(self.ball2.x / self.board_width)
		inputsLeft.append(self.ball2.y / self.board_height)
		inputsLeft.append(self.sig(self.ball2.hspeed))
		inputsLeft.append(self.sig(self.ball2.vspeed))
		inputsLeft.append(self.data.get("playerRight").y/self.board_height)
		
		inputsRight = []
		inputsRight.append(self.data.get("playerRight").y/self.board_height)
		inputsRight.append((self.board_width - self.ball.x) / self.board_width)
		inputsRight.append(self.ball.y / self.board_height)
		inputsRight.append(-self.ball.hspeed)
		inputsRight.append(self.ball.vspeed)
		inputsRight.append((self.board_width - self.ball2.x) / self.board_width)
		inputsRight.append(self.ball2.y / self.board_height)
		inputsRight.append(-self.ball2.hspeed)
		inputsRight.append(self.ball2.vspeed)
		inputsRight.append(self.data.get("playerLeft").y/self.board_height)
		
		self.data.get("playerLeft").tick(inputsLeft)
		self.data.get("playerRight").tick(inputsRight)
	
	def export_players(self):
		self.data.get("playerLeft").export_player()
		self.data.get("playerRight").export_player()
	
	def play_match(self, score_to_win=5, record=False):
		if (record):
			self.clear_recording()
		self.data.set("scoreLeft",0)
		self.data.set("scoreRight",0)
		self.data.set("numberParries",0)
		self.data.set("lastScore", "left")
		self.ball.last_side_scored = "left"
		self.ball2.last_side_scored = "left"
		self.ball.reset_ball()
		self.ball2.reset_ball()
		self.data.get("playerLeft").align_left()
		self.data.get("playerRight").align_right()
		self.data.get("playerLeft").reset_player()
		self.data.get("playerRight").reset_player()
		moves = []
		
		while (self.data.get("scoreLeft",0) < score_to_win and self.data.get("scoreRight",0) < score_to_win):
			if (record):
				self.play_point(record=True)
			else:
				self.play_point()
		
		if (record):
			print("Saved recording as " + self.export_recording())
		
		if (self.data.get("scoreLeft",0) == score_to_win):
			return "left"
		else:
			return "right"
	
	def export_recording(self):
		filename = "recordings/" + str(self.data.get("numberParries", 0)) + "_" + str(time.time()) + "_" + str(self.data.get("playerLeft").score) + "_" + str(self.data.get("playerRight").score) + "_" + str(math.floor(random() * 1000)) + ".recording"
		with open(filename, "w") as json_file:
			json.dump(self.recording, json_file)
		return filename

	def clear_recording(self):
		self.recording = []
	
	def mutate_player(self, p):
		new_p = copy.deepcopy(p)
		new_p.controller = self.mutator.mutate(new_p.controller)
		return new_p
		
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
		
	def import_left(self, fname):
		self.data.get("playerLeft").import_player(fname)
	
	def import_right(self, fname):
		self.data.get("playerRight").import_player(fname)