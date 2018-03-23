from Monster import Monster
import random

###########################################
# Stats for the Werewolf
#
# @param Monster
###########################################
class Werewolf(Monster):
	
	def __init__(self):
		self.hp = 200 
		self.atk = random.randint(0,40)
		self.name = "Werewolf"
		self.dead = False
		self.observers = []

	def attacked(self, hit, item):
		if item == "Chocolate Bar" or item == "chocolate bar" or item =="sour straw" or item == "Sour Straw":
			pass
		
		else:
			self.hp = self.hp - hit
		if self.hp <= 0:
			self.die()

