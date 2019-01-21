from network import Network
from math import random

class Mutator(object):
	mutation_probability = 0.1
	mutation_strength = 0.2
	
	def random_range(self, min, max):
		return(min + (random() * (max - min)))
		
	def random_mutation(self):
		return random_range(-self.mutation_strength,self.mutation_strength)
		
	def mutate(self, net):
		for layer in net.layers:
			for node in layer:
				if (random() < self.mutation_probability):
					node["bias"] += self.random_mutation()
				for weight in node["weights"]:
					if (random() < self.mutation_probability):
						weight += self.random_mutation()
				
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
				
				
		
		
				