from math import exp
from random import *

class Network(object):
	inputs = []
	inputLength = 52
	layers = []
	
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
				for i in range(len(lastResult)):
					sum += (lastResult[i] * node["weights"][i])
				sum -= node["bias"]
				currentResult.append(self.sig(sum))
			lastResult = currentResult
		return lastResult

if __name__ == "__main__":
	print("Running")
	net = Network()
	inputs = []
	inputs.append(random())
	inputs.append(random())
	for i in range(50):
		if (random() > 0.5):
			inputs.append(1)
		else:
			inputs.append(0)
	net.setInputs(inputs)
	net.createNet(5, 3)
	n = net.createRandomNode(5)
	print(n["bias"])
	print(net.calcNetwork())
