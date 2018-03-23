from Monster import Monster
import random

###########################################
# Stats for the Vampire
#
# @param Monster
###########################################
class Vampire(Monster):
	
	def __init__(self):
		self.hp = random.randint(100,200)
		self.atk = random.randint(10,20)
		self.name = "Vampire"
		self.dead = False
		self.observers = []

	def attacked(self, hit, item):
		if item == "Chocolate Bar" or item == "chocolate bar":
			pass
		else:
			self.hp = self.hp - hit
		if self.hp <= 0:
			self.die()

