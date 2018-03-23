from Monster import Monster
import random

###########################################
# Stats for the Ghoul
#
# @param Monster
###########################################
class Ghoul(Monster):
	
	def __init__(self):
		self.hp = random.randint(40,80)
		self.atk = random.randint(15,30)
		self.name = "Ghoul"
		self.dead = False
		self.observers = []
	
	def attacked(self, hit, item):
		if item == "Nerd Bomb" or item == "nerd bomb":
			self.hp = self.hp - 5*hit
		
		else:
			self.hp = self.hp - hit
		
		if self.hp <= 0:
			self.die()

	
