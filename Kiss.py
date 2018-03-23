import random

###########################################
# The Hershey Kiss weapon
# Usable unlimited times
# Attack modifier 1
#
###########################################
class Kiss:
	
	def __init__(self):
		self.use = "unlimited"
		self.mult = 1

	def used(self):
		pass
		
	def getMult(self):
		self.mult = 1
		return self.mult

	def getUse(self):
		return self.use

	def getString(self):
		return "Hershey Kiss"
