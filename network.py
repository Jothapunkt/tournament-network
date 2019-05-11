from math import exp
from random import *

class Network(object):
	def __init__(self):
		self.inputs = []
		self.inputLength = 9
		self.layers = []
	
	def createNet(self, *layerLengths):
		self.layers = []
		layerNum = 0
		for layerLength in layerLengths:
			l = []
			inputCount = self.inputLength
			if (layerNum > 0):
				inputCount = len(self.layers[layerNum - 1])
			layerNum += 1
			for i in range(layerLength):
				l.append(self.createRandomNode(inputCount))
			self.layers.append(l)
			
	def createRandomNode(self, weights):
		node = {}
		node["weights"] = []
		for i in range(weights):
			node["weights"].append(self.randomrange(-1,1))
		node["bias"] = self.randomrange(-1,1)
		return node
	
	def randomrange(self, min, max):
		delta = max - min
		return (min + (delta * random()))
		
	def sig(self, x):
		return 1 / (1 + exp(-x))
	
	def setInputs(self, i):
		self.inputs = i
	
	"""
	Calculates the output layer of the network
	"""
	def calcNetwork(self):
		lastResult = self.inputs
		
		for layer in self.layers:
			currentResult = []
			for node in layer:
				sum = 0
				for i in range(len(node["weights"])):
					sum += (lastResult[i] * node["weights"][i])
				sum -= node["bias"]
				currentResult.append(self.sig(sum))
			lastResult = currentResult
		return lastResult
		
	def print_net(self):
		print("--- Network Print ---")
		print("Inputs: " + str(self.inputs))
		
		for lnum,layer in enumerate(self.layers):
			print("Layer " + str(lnum) + ": " + str(len(layer)) + " Nodes")
			for nnum, node in enumerate(layer):
				weightsum = 0
				for weight in node["weights"]:
					weightsum += weight
				print("[" + str(node["bias"]) + ", " + str(weightsum) + "]")
