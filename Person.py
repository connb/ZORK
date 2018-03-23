from Monster import Monster

###########################################
# Stats for the person
# Persons give the player health
#
# @param Monster
###########################################
class Person(Monster):
	
	def __init__(self):
		self.hp = 1
		self.atk = -5
		self.name = "Person"
		self.dead = False
		self.observers = []
	
	def attacked(self, hit, item):
		pass
	

