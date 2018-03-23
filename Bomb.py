import random

###########################################
# The Nerd Bomb weapon
# Usable 1 time
# Attack modifier between 3.5 and 5.0
#
###########################################
class Bomb:
	
	def __init__(self):
		self.use = 1
		self.mult = 1

	def used(self):
		self.use = self.use - 1
		
	def getMult(self):
		self.mult = random.uniform(3.5, 5.0)
		return self.mult

	def getUse(self):
		return self.use
	def getString(self):
		return "Nerd Bomb"
