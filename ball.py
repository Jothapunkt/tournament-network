from network import Network
from random import *
import math
import json
from game_data import *

class Ball(object):
	def __init__(self):
		self.data = GameData()
		self.radius = 5
		self.acceleration = 1.001
		self.minSpeed = 4
		self.speedCapUpper = 100
		self.speedCapLower = 1
		
		self.board_width = 1000
		self.board_height = 500
		
		self.reset_ball()
	
	def reset_ball(self):
		self.x = 0.5 * self.board_width
		self.y = 0.5 * self.board_height
		
		self.vspeed = 0.3 * self.minSpeed
		self.hspeed = self.minSpeed
		
		if (self.data.get("last_score", "left") == "right"):
			self.hspeed = -self.hspeed
	
	def tick(self):
		targetX = self.x + self.hspeed
		targetY = self.y + self.vspeed
		
		self.hspeed *= self.acceleration
		self.vspeed *= self.acceleration
		
		if (targetY < 0):
			self.y = 0
			self.vspeed = -self.vspeed
		elif (targetY > self.board_height):
			self.y = self.board_height
			self.vspeed = -self.vspeed
		else:
			self.y = targetY
			
		if (targetX < self.data.get("playerLeft").width):
			if (targetY + self.radius >= self.data.get("playerLeft").y and targetY - self.radius <= self.data.get("playerLeft").y + self.data.get("playerLeft").height): #Did the ball hit the left paddle?
				self.x = self.data.get("playerLeft").width
				self.hspeed = -self.hspeed
				self.data.set("numberParries", self.data.get("numberParries",0)+1)
				
				if (self.data.get("playerLeft").last_move == "up"):
					self.vspeed = self.vspeed * (0.5 if self.vspeed < 0 else 1.5)
				elif (self.data.get("playerLeft").last_move == "down"):
					self.vspeed = self.vspeed * (0.5 if self.vspeed > 0 else 1.5)
				
			elif (targetX < 0):
				self.data.set("scoreRight", self.data.get("scoreRight", 0) + 1)
				self.data.set("lastScore", "right")
				self.reset_ball()
			else:
				self.x = targetX
		elif (targetX > self.board_width - self.data.get("playerRight").width):
			if (targetY + self.radius >= self.data.get("playerRight").y and targetY - self.radius <= self.data.get("playerRight").y + self.data.get("playerRight").height): #Did the ball hit the right paddle?
				self.x = self.board_width - self.data.get("playerRight").width
				self.hspeed = -self.hspeed
				self.data.set("numberParries", self.data.get("numberParries",0)+1)
				
				if (self.data.get("playerRight").last_move == "up"):
					self.vspeed = self.vspeed * (0.5 if self.vspeed < 0 else 1.5)
				elif (self.data.get("playerRight").last_move == "down"):
					self.vspeed = self.vspeed * (0.5 if self.vspeed > 0 else 1.5)
			elif (targetX > self.board_width):
				self.data.set("scoreLeft", self.data.get("scoreLeft", 0) + 1)
				self.data.set("lastScore", "left")
				self.reset_ball()
			else:
				self.x = targetX
		else:
			self.x = targetX
		
		if (self.vspeed > self.speedCapUpper):
			self.vspeed = self.speedCapUpper
		if (self.vspeed < -self.speedCapUpper):
			self.vspeed = -self.speedCapUpper
		
		if (self.hspeed > self.speedCapUpper):
			self.hspeed = self.speedCapUpper
		if (self.hspeed < -self.speedCapUpper):
			self.hspeed = -self.speedCapUpper
		
		if (self.vspeed > -self.speedCapLower and self.vspeed <= 0):
			self.vspeed = -self.speedCapLower
		if (self.vspeed < self.speedCapLower and self.vspeed > 0):
			self.vspeed = self.speedCapLower