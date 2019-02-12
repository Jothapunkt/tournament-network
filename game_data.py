from network import Network
from random import *
import copy

class GameData(object):
	class __DataWrapper(object):
		def __init__(self):
			self.dict = {}
	instance = None
	def __init__(self):
		if not GameData.instance:
			GameData.instance = GameData.__DataWrapper()
	def set(self, key, value):
		GameData.instance.dict[key] = value
		
	def get(self, key, default=None):
		if key in GameData.instance.dict:
			return GameData.instance.dict[key]
		else:
			return default