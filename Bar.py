import random

###########################################
# The Chocolate Bar weapon
# Usable 4 times
# Attack modifier between 2.0 and 2.4
#
###########################################
class Bar:
	
	def __init__(self):
		self.use = 4
		self.mult = 0

	def used(self):
		self.use = self.use - 1
		
	def getMult(self):
		self.mult = random.uniform(2.0, 2.4)
		return self.mult

	def getUse(self):
		return self.use

	def getString(self):
		return "Chocolate Bar"
