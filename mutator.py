from network import Network
from random import *
import copy

class Mutator(object):
	def __init__(self):
		mutation_probability = 0.1
		mutation_strength = 0.2
	
	def random_range(self, min, max):
		return(min + (random() * (max - min)))
		
	def random_mutation(self):
		return self.random_range(-self.mutation_strength,self.mutation_strength)
		
	def mutate(self, net):
		for layer in net.layers:
			for index,node in enumerate(layer):
				if (random() < self.mutation_probability):
					node["bias"] += self.random_mutation()
				for weight_index, weight in enumerate(node["weights"]):
					if (random() < self.mutation_probability):
						node["weights"][weight_index] += self.random_mutation()
		return net
	
	#Checks if two networks are identical
	def compare_nets(self, a, b):
		if len(a.layers) != len(b.layers):
			print("Different number of layers")
			return False
		
		i = 0
		while (i < len(a.layers)):
			layer_a = a.layers[i]
			layer_b = b.layers[i]
			i += 1
			
			if (len(layer_a) != len(layer_b)):
				print("Different number of nodes in layer " + str(i))
				return False
			
			j = 0
			while (j < len(layer_a)):
				node_a = layer_a[j]
				node_b = layer_b[j]
				j += 1
				
				if (node_a["bias"] != node_b["bias"]):
					print("Different biases")
					return False
					
				if (len(node_a["weights"]) != len(node_b["weights"])):
					print("Different number of weights")
					return False
					
				k = 0
				while (k < len(node_a["weights"])):
					if (node_a["weights"][k] != node_b["weights"][k]):
						print("Different weights")
						return False
						
					k += 1
		return True
		
				